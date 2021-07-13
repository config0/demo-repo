def run(stackargs):

    import os
    import json

    # instantiate stack
    stack = newStack(stackargs)

    # Add variables
    stack.parse.add_optional(key="build_dir",default="_random")
    stack.parse.add_optional(key="entry_point",default="null")

    # Add shelloutconfigs
    stack.add_shelloutconfig('williaumwu:::demo-repo::show_configuration')

    # Add hostgroups
    stack.add_execgroup("bill12252016:::formula1::red_wheels", "wheels")
    stack.add_execgroup("bill12252016:::formula1::ashton_martin_core", "core")

    # init the stack namespace
    stack.init_variables()
    stack.init_execgroups()
    stack.init_shelloutconfigs()

    stack.set_variable("group_dest_dir","/var/tmp/share/{}".format(stack.build_dir))

    env_vars = {"F1_DIR":stack.group_dest_dir}

    inputargs = {"display":True}
    inputargs["env_vars"] = json.dumps(env_vars)
    inputargs["group_dest_dir"] = stack.group_dest_dir
    inputargs["human_description"] = "Creating platform with wheels {}".format(stack.wheels.name)
    stack.wheels.insert(**inputargs)

    inputargs = {"display":True}
    inputargs["env_vars"] = json.dumps(env_vars)
    inputargs["group_dest_dir"] = stack.group_dest_dir
    inputargs["human_description"] = "Creating platform with core {}".format(stack.core.name)
    stack.core.insert(**inputargs)

    # if this is the parent or top level of the entry point, then we print out
    if stack.entry_point:

        env_vars = {"F1_DIR":os.path.join(stack.group_dest_dir,"var","tmp","demo")}
        inputargs = {"display":True}
        inputargs["human_description"] = 'Shows the F1 configuration with {}'.format(stack.show_configuration.name)
        inputargs["env_vars"] = json.dumps(env_vars)
        stack.show_configuration.execute(**inputargs)

    return stack.get_results()
