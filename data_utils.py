"""
This data utility module provides functions to perform the following operations.

Functions:
- coordinate_to_geometry:
- plot_route_map_flow: capitalizes the first letter of each word in the input string
"""

import geopandas as gpd
from shapely.geometry import Point


def shp_to_gdf(shp_list):
    """
    shp_list is list of shapefile path
    return list of gdf
    """
    gdf_results = []
    for shp in shp_list:
        shp_gdf = gpd.read_file(shp)
        gdf_results.append(shp_gdf)
    return gdf_results


def coordinate_to_geometry(df, lon_col="lon", lat_col="lat", desired_crs="EPSG:4019"):
    """
    Convert coordiante to geometry with crs and output is gdf
    :param df: pandas.DataFrame,
    :param lon_col: str, longitude
    :param lat_col: str, latitude
    :param desired_crs: str, crs
    :return: geopandas.GeoDataFrame, including geometry column
    """
    if "lon" not in df.columns or "lat" not in df.columns:
        raise KeyError(
            "The input dataframe must contain '{}' and '{}'.".format(lon_col, lat_col)
        )
    if "geometry" not in df.columns:
        geometry = [Point(xy) for xy in zip(df[lon_col], df[lat_col])]
        gdf = gpd.GeoDataFrame(df, crs=desired_crs, geometry=geometry)
    else:
        gdf = df.copy()
    return gdf


def plot_route_map_flow(dict_gdf: dict):
    pass
    # fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(10, 10), layout="constrained")
    # color_column = 'TOT_VOL'
    # cmap = 'RdYlBu_r'
    # gdf_value.plot(column=color_column, cmap=cmap, linewidth=5, ax=ax1)
    # ctx.add_basemap(ax=ax1, zoom=13, crs='EPSG:4019', source=ctx.providers.Esri.WorldStreetMap)

    # # set up xlabel, ylabel, and title for ax1
    # ax1.set_xlabel('long')
    # ax1.set_ylabel('lat')
    # ax1.set_title('Map of SR74')
    # # set up legend
    # # vmin, vmax = SR74_BY2019_gdf[color_column].min(), SR74_BY2019_gdf[color_column].max()
    # # sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=vmin, vmax=vmax))
    # # cbar = fig.colorbar(sm)

    # ax2.plot(SR74_BY2019_pm['PM'], SR74_BY2019_pm['TOT_VOL'])

    # ax2.set_xlabel('Postmile')
    # ax2.set_ylabel('Total flow')
    # ax2.set_title('SR74 Total Flow BY2019')
    # plt.show()
