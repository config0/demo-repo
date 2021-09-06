def run(stackargs):

    import os
    import json

    # instantiate stack
    stack = newStack(stackargs)

    # Add variables
    stack.parse.add_optional(key="build_dir",default="_random")
    stack.parse.add_optional(key="entry_point",default="null")

    # Add shelloutconfigs
    stack.add_shelloutconfig('bill12252016:::demo-repo::show_configuration')

    # Add hostgroups
    stack.add_execgroup("bill12252016:::demo-repo::flavor", "flavor")
    stack.add_execgroup("bill12252016:::demo-repo::dough", "dough")

    # init the stack namespace
    stack.init_variables()
    stack.init_execgroups()
    stack.init_shelloutconfigs()

    stack.set_variable("group_dest_dir","/var/tmp/share/{}".format(stack.build_dir))

    env_vars = {"COOKING_DIR":stack.group_dest_dir}

    inputargs = {"display":True}
    inputargs["env_vars"] = json.dumps(env_vars)
    inputargs["group_dest_dir"] = stack.group_dest_dir
    inputargs["human_description"] = "Creating flavor with {}".format(stack.flavor.name)
    stack.flavor.insert(**inputargs)

    inputargs = {"display":True}
    inputargs["env_vars"] = json.dumps(env_vars)
    inputargs["group_dest_dir"] = stack.group_dest_dir
    inputargs["human_description"] = "Creating dough with {}".format(stack.dough.name)
    stack.dough.insert(**inputargs)

    # if this is the parent or top level of the entry point, then we print out
    if stack.entry_point:

        env_vars = {"COOKING_DIR":os.path.join(stack.group_dest_dir,"var","tmp","demo")}
        inputargs = {"display":True}
        inputargs["human_description"] = 'Shows the ingredients with {}'.format(stack.show_configuration.name)
        inputargs["env_vars"] = json.dumps(env_vars)
        stack.show_configuration.execute(**inputargs)

    return stack.get_results()
