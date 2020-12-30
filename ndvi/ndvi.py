import rasterio as rio
import numpy as np
import fiona

def read_image(url: str, poly_geom: dict):
    """
    Download an image masked by a polygon geometry.

    :param url: URL to the GeoTIFF
    :param poly_geom: Geometry used to mask (clip) the image as a GeoJSON-like dict
    :returns: A masked image and the transform that was applied to it, along with the image metadata
    """
    # Download the masked area of the image and give it back
    with rio.open(url) as src:
        meta = src.meta
        masked, mask_transform = rio.mask.mask(dataset=src, shapes=poly_geom, crop=True)
        return meta, masked, mask_transform

# main
if __name__ == '__main__':
    # URLs for the imagery bands
    b4_url = 'http://landsat-pds.s3.amazonaws.com/c1/L8/037/024/LC08_L1TP_037024_20200824_20200905_01_T1/LC08_L1TP_037024_20200824_20200905_01_T1_B4.TIF'
    b3_url = 'http://landsat-pds.s3.amazonaws.com/c1/L8/037/024/LC08_L1TP_037024_20200824_20200905_01_T1/LC08_L1TP_037024_20200824_20200905_01_T1_B3.TIF'

    # Path for the boundary file
    boundary_file = 'data/mask_boundary.shp'

    # Calculate NDVI for the section of the image within the masked area
    with fiona.open(boundary_file, 'r') as polygons:
        for poly in polygons:
            b3_meta, b3_masked, b3_transform = read_image(b3_url, poly)
            b4_meta, b4_masked, b4_transform = read_image(b4_url, poly)

            # Allow division by zero
            np.seterr(divide='ignore', invalid='ignore')

            # Calculate the NDVI
            ndvi = (b4_masked.astype(float) - b3_masked.astype(float)) / (b4_masked + b3_masked)

            # Define spatial characteristics of output object from the input
            kwargs = b3_meta
            # Update kwargs (change in data type)
            kwargs.update(
                dtype=rio.float32,
                count = 1)
            
            # write the output
            poly_id = poly['properties']['id']
            with rio.open(f'data/ndvi_{poly_id}.tif', 'w', **kwargs) as dst:
                dst.write_band(1, ndvi.astype(rio.float32))
