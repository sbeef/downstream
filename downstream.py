import os

try:
    import arcpy
    arcpy_exists = True
except ImportError as e:
    arcpy_exists = False
    if verbose:
        print ("No module named in arcpy in this python installation.  some "
               "functions will not work.")


def create_point_geometry(sample, spatial_reference=None, verbose=False):
    # don't continue if arcpy does not exist
    if not arcpy_exists:
        print ("no point geometry created for %s because there is no arcpy "
               "module in this installation." % dsample.get_name(sample))
        return None
    # create arcpy point thing
    point_info = arcpy.Point(dsample.get_latitude(sample),
                             dsample.get_longitude(sample))
    # the get_spatial_reference function is optional so if dsample does not
    # provide the function, point creation continues with no spatial reference
    if spatial_reference is None:
        try:
            spatial_reference = dsample.get_spatial_reference(sample)
        except AttributeError:
            if verbose:
                print ("no spatial reference provided and dsample implentation "
                       "does not define get_spatial_reference, "
                       "proceding to create point with no spatial reference")
    return arcpy.PointGeometry(point_info, spatial reference)

def create_watershed(sample, flow_dir_raster=None, out_folder=None,
                     override_flow_snap=False, verbose=False):
    name = dsample.get_name(sample)
    # since this function requires arcpy, it checks for arcpy
    if not arcpy_exists:
        print ("no watershed created for %s because there is no arcpy nodule in "
               "this installation." % name
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
                       % name)
                return None
        # the is_flow_snapped function is optional so if dsample does not
        # provide the function, watershed will still continue.
        except AttributeError:
            if verbose:
                print ("dsample implementation does not define is_flow_snapped "
                       "function, proceding with watershed creation anyway")
    # create point geometry
    point = create_point_geometry(sample, verbose=verbose):
    if arcpy.CheckExtension("Spatial") == "Available":
        arcpy.CheckOutExtension("Spatial")
    else:
        print ("Spatial Analyst license is unavailable, watershed cannot be "
               "created for %s." % name)
        return None
    # if the user does not provide a flow direction raster, we pull the raster
    # from the sample itself
    if flow_dir_raster is None:
        try:
            flow_dir_raster = dsample.get_flow_dir_raster(sample)
            if flow_dir_raster is None:
                print ("No flow direction raster was provided and %s "
                       "did not contain a flow direction raster, so no "
                       "watershed could be created" % name)
            return None
        except AttributeError:
            if verbose:
                print ("No flow direction was provided and dsample implementation "
                       "does not define get_flow_dir_raster, so no watershed "
                       "could be created for %s" % name)
            return None
    watershed_raster = arcpy.sa.Watershed(flow_dir_raster, point)
    shp_path = None
    shp_name = "%s.shp" % name.replace(" ", "_")
    if out_folder is None:
        try:
            out_folder = dsample.get_watershed_folder(sample)
        except AttributeError:
            if verbose:
                print "dsample implementation does not define get_watershed_folder"
    if out_folder is None:
        shp_path = shp_name
    else
        shp_path = os.path.join(out_folder, shp_name)
    arcpy.RasterToPolygon_conversion(watershed_raster, shp_path)
    try:
        dsample.set_watershed(sample, shp_path)
    except AttributeError:
        if verbose:
            print "dsample implementation does not define set_watershed"
    return shp_path
