try:
    import arcpy
    arcpy_exists = True
except ImportError as e:
    arcpy_exists = False
    if verbose:
        print ("No module named in arcpy in this python installation.  some "
               "functions will not work.")


def create_point_geometry(sample, verbose=False):
    # don't continue if arcpy does not exist
    if not arcpy_exists:
        print ("no point geometry created for %s because there is no arcpy "
               "module in this installation." % dsample.get_name(sample))
        return None
    else:
        # create arcpy point thing
        point_info = arcpy.Point(dsample.get_latitude(sample),
                                 dsample.get_longitude(sample))
        # the get_spatial_reference function is optional so if dsample does not
        # provide the function, point creation continues with no spatial reference
        try:
            spatial_reference = dsample.get_spatial_reference(sample)
        except AttributeError:
            if verbose:
                print ("dsample implentation does not define get_spatial_reference, "
                       "proceding to create point with no spatial reference")
                spatial_reference = None
        return arcpy.PointGeometry(point_info, spatial reference)

def create_watershed(sample, flow_dir_raster=None, out_folder=None,
                     override_flow_snap=False, verbose=False):
    # since this function requires arcpy, it checks for arcpy
    if not arcpy_exists:
        print ("no watershed created for %s because there is no arcpy nodule in "
               "this installation." % dsample.get_name(sample))
        return None
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
        c

