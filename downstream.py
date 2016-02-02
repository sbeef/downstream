def create_watershed(sample, flow_dir_raster=None, out_folder=None,
                     override_flow_snap=False, verbose=False):
    # unless you ask it not to, it will check to see if you have snapped the
    # point to a flow direction raster before continuing
    if not override_flow_snap:
        try:
            # calls the is_flow_snapped function from the dsample library
            if not dsample.is_flow_snapped(sample):
                # watershed creation has been skipped since point is not ready
                # so notify the user and return
                print ("%s has not been snapped to flow direction, so no "
                       "watershed was created.  set 'override_flow_snap' to "
                       "True to create watershed anyway"
                       % dsample.get_name(sample))
                return None
        # the is_flow_snapped function is optional so if dsample does not
        # provide the function, watershed will still continue.
        except AttributeError:
            if verbose:
                print ("dsample implementation does not define is_flow_snapped "
                       "function, proceding with watershed creation anyway")
