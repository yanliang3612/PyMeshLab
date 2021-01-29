import pymeshlab


def example_apply_filter_parameters_check_default_values():
    # lines needed to run this specific example
    print('\n')
    from . import samples_common
    output_path = samples_common.test_output_path()

    # create a new MeshSet
    ms = pymeshlab.MeshSet()

    ms.load_new_mesh(output_path + 'colored_airplane.ply')

    # returns a dictionary which binds, for each parameter (a string with its name) the
    # default value that would be used if the given filter would be applied at the current
    # status of the MeshSet (e.g. current selected mesh)
    default_params = ms.filter_parameter_values('per_vertex_quality_histogram')

    print(default_params['histmax'])