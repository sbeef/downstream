def create_watershed(sample, flow_dir_raster=None, out_folder=None,
                     override_flow_snap=False, verbose=False):
    #unless you ask it not to, it will check to see if you have snapped the
    #point to a flow direction raster before continuing
    if not override_flow_snap:
        try:
            if dsample.flow_snapped(sample):
                print ("%s has not been snapped to flow direction, so no "
                       "watershed was created.  set 'override_flow_snap' to "
                       "True to create watershed anyway"
                       % dsample.get_name(sample))
        except AttributeError:
            if verbose:
                print ("sample has no information on flow snapping, proceding "
                       "with watershed creation anyway")
