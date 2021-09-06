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
    stack.add_execgroup("bill12252016:::demo-repo::presentation", "presentation")

    # Add stack
    stack.add_substack("bill12252016:::vegan_muffin")

    # init the stack namespace
    stack.init_variables()
    stack.init_execgroups()
    stack.init_shelloutconfigs()
    stack.init_substacks()

    stack.set_variable("group_dest_dir","/var/tmp/share/{}".format(stack.build_dir))

    # Execute substack
    default_values = { "build_dir":stack.build_dir }
    overide_values = { "entry_point":False }

    inputargs = {"default_values":default_values,
                 "overide_values":overide_values}

    inputargs["human_description"] = 'Executing substack "{}"'.format(stack.almond_croissants.name)
    stack.vegan_muffin.insert(display=True,**inputargs)

    # Add presentation 
    inputargs = {"display":True}
    inputargs["env_vars"] = json.dumps({"COOKING_DIR":stack.group_dest_dir})
    inputargs["group_dest_dir"] = stack.group_dest_dir
    inputargs["human_description"] = "Creating with presentation {}".format(stack.presentation.name)
    stack.presentation.insert(**inputargs)

    # if this is the parent or top level of the entry point, then we print out
    if stack.entry_point:

        env_vars = {"COOKING_DIR":os.path.join(stack.group_dest_dir,"var","tmp","demo")}
        inputargs = {"display":True}
        inputargs["human_description"] = 'Shows the cooking configuration with {}'.format(stack.show_configuration.name)
        inputargs["env_vars"] = json.dumps(env_vars)
        stack.show_configuration.execute(**inputargs)

    return stack.get_results()
