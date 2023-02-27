"""
This data utility module provides functions to perform the following operations.

Functions:
- read_shp_to_gdf: read shapefile to
- plot_route_map_flow: capitalizes the first letter of each word in the input string
"""


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


def plot_route_map_flow(dict_gdf: dict):
    list_plots = []
    for gdf_key, gdf_value in dict_gdf.items():
        gdf_value.head(5)
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
