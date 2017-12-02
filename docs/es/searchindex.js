Search.setIndex({docnames:["api","api/catatom","api/catatom2osm","api/compat","api/csvtools","api/download","api/hgwnames","api/layer","api/main","api/modules","api/osm","api/osmxml","api/overpass","api/report","api/setup","api/test","api/test.benchmark","api/test.check_mun_names","api/test.count_buildings","api/test.test_catatom","api/test.test_catatom2osm","api/test.test_csvtools","api/test.test_download","api/test.test_hgwnames","api/test.test_layer","api/test.test_main","api/test.test_osm","api/test.test_osmxml","api/test.test_overpass","api/test.test_report","api/test.test_setup","api/test.test_translate","api/test.unittest_main","api/translate","changes","coverage","genindex","index","install","readme"],envversion:50,filenames:["api.rst","api/catatom.rst","api/catatom2osm.rst","api/compat.rst","api/csvtools.rst","api/download.rst","api/hgwnames.rst","api/layer.rst","api/main.rst","api/modules.rst","api/osm.rst","api/osmxml.rst","api/overpass.rst","api/report.rst","api/setup.rst","api/test.rst","api/test.benchmark.rst","api/test.check_mun_names.rst","api/test.count_buildings.rst","api/test.test_catatom.rst","api/test.test_catatom2osm.rst","api/test.test_csvtools.rst","api/test.test_download.rst","api/test.test_hgwnames.rst","api/test.test_layer.rst","api/test.test_main.rst","api/test.test_osm.rst","api/test.test_osmxml.rst","api/test.test_overpass.rst","api/test.test_report.rst","api/test.test_setup.rst","api/test.test_translate.rst","api/test.unittest_main.rst","api/translate.rst","changes.rst","coverage.rst","genindex.rst","index.rst","install.rst","readme.rst"],objects:{"":{catatom2osm:[2,0,0,"-"],catatom:[1,0,0,"-"],compat:[3,0,0,"-"],csvtools:[4,0,0,"-"],download:[5,0,0,"-"],hgwnames:[6,0,0,"-"],layer:[7,0,0,"-"],main:[8,0,0,"-"],osm:[10,0,0,"-"],osmxml:[11,0,0,"-"],overpass:[12,0,0,"-"],report:[13,0,0,"-"],setup:[14,0,0,"-"],test:[15,0,0,"-"],translate:[33,0,0,"-"]},"catatom.Reader":{get_atom_file:[1,2,1,""],get_boundary:[1,2,1,""],get_layer_paths:[1,2,1,""],get_metadata:[1,2,1,""],is_empty:[1,2,1,""],read:[1,2,1,""]},"catatom2osm.CatAtom2Osm":{delete_shp:[2,2,1,""],end_messages:[2,2,1,""],exit:[2,2,1,""],export_layer:[2,2,1,""],get_building:[2,2,1,""],get_current_ad_osm:[2,2,1,""],get_current_bu_osm:[2,2,1,""],get_highway:[2,2,1,""],get_tasks:[2,2,1,""],get_translations:[2,2,1,""],get_zoning:[2,2,1,""],merge_address:[2,2,1,""],process_building:[2,2,1,""],process_parcel:[2,2,1,""],process_tasks:[2,2,1,""],process_zoning:[2,2,1,""],read_address:[2,2,1,""],read_osm:[2,2,1,""],run:[2,2,1,""],write_osm:[2,2,1,""]},"download.ProgressBar":{update:[5,2,1,""]},"layer.AddressLayer":{conflate:[7,2,1,""],create_shp:[7,4,1,""],get_highway_names:[7,2,1,""],get_image_links:[7,2,1,""],to_osm:[7,2,1,""]},"layer.BaseLayer":{"export":[7,2,1,""],append:[7,2,1,""],bounding_box:[7,2,1,""],copy_feature:[7,2,1,""],count:[7,2,1,""],create_shp:[7,4,1,""],delete_shp:[7,4,1,""],get_index:[7,2,1,""],join_field:[7,2,1,""],reproject:[7,2,1,""],search:[7,2,1,""],to_osm:[7,2,1,""],translate_field:[7,2,1,""]},"layer.ConsLayer":{append_zone:[7,2,1,""],clean:[7,2,1,""],conflate:[7,2,1,""],explode_multi_parts:[7,2,1,""],get_parts:[7,2,1,""],index_of_building_and_parts:[7,2,1,""],index_of_parts:[7,2,1,""],index_of_pools:[7,2,1,""],is_building:[7,4,1,""],is_part:[7,4,1,""],is_pool:[7,4,1,""],merge_adjacent_parts:[7,2,1,""],merge_building_parts:[7,2,1,""],move_address:[7,2,1,""],remove_inner_rings:[7,2,1,""],remove_outside_parts:[7,2,1,""],set_tasks:[7,2,1,""],to_osm:[7,2,1,""],validate:[7,2,1,""]},"layer.DebugWriter":{add_point:[7,2,1,""]},"layer.HighwayLayer":{read_from_osm:[7,2,1,""]},"layer.Point":{boundingBox:[7,2,1,""],get_angle:[7,2,1,""],get_corner_context:[7,2,1,""],get_spike_context:[7,2,1,""]},"layer.PolygonLayer":{clean:[7,2,1,""],delete_invalid_geometries:[7,2,1,""],explode_multi_parts:[7,2,1,""],get_adjacents_and_geometries:[7,2,1,""],get_area:[7,2,1,""],get_multipolygon:[7,4,1,""],get_outer_vertices:[7,4,1,""],get_parents_per_vertex_and_geometries:[7,2,1,""],get_vertices_list:[7,4,1,""],merge_adjacent_features:[7,4,1,""],merge_adjacents:[7,2,1,""],simplify:[7,2,1,""],topology:[7,2,1,""]},"layer.ZoningLayer":{append:[7,2,1,""],export_poly:[7,2,1,""],set_tasks:[7,2,1,""]},"osm.Element":{attrs:[10,5,1,""],fid:[10,5,1,""],is_new:[10,2,1,""],type:[10,5,1,""]},"osm.Node":{childs:[10,5,1,""],geometry:[10,2,1,""],lat:[10,5,1,""],lon:[10,5,1,""]},"osm.Osm":{attrs:[10,5,1,""],get:[10,2,1,""],merge_duplicated:[10,2,1,""],nodes:[10,5,1,""],relations:[10,5,1,""],remove:[10,2,1,""],replace:[10,2,1,""],ways:[10,5,1,""]},"osm.Relation":{Member:[10,1,1,""],append:[10,2,1,""],childs:[10,5,1,""],geometry:[10,2,1,""],is_valid_multipolygon:[10,2,1,""],outer_geometry:[10,2,1,""],remove:[10,2,1,""],replace:[10,2,1,""]},"osm.Relation.Member":{attrs:[10,5,1,""],ref:[10,5,1,""],type:[10,5,1,""]},"osm.Way":{append:[10,2,1,""],childs:[10,5,1,""],clean_duplicated_nodes:[10,2,1,""],geometry:[10,2,1,""],is_closed:[10,2,1,""],is_open:[10,2,1,""],remove:[10,2,1,""],replace:[10,2,1,""],search_node:[10,2,1,""],shoelace:[10,2,1,""]},"overpass.Query":{add:[12,2,1,""],download:[12,2,1,""],get_url:[12,2,1,""],read:[12,2,1,""],set_search_area:[12,2,1,""]},"report.Report":{address_stats:[13,2,1,""],cons_end_stats:[13,2,1,""],cons_stats:[13,2,1,""],fixme_stats:[13,2,1,""],get:[13,2,1,""],get_sys_info:[13,2,1,""],inc:[13,2,1,""],osm_stats:[13,2,1,""],sum:[13,2,1,""],to_file:[13,2,1,""],to_string:[13,2,1,""],validate:[13,2,1,""]},"test.benchmark":{AppendZoneTimer:[16,1,1,""],BaseBuildingTimer:[16,1,1,""],BaseConsTimer:[16,1,1,""],BaseTimer:[16,1,1,""],ConsTimer:[16,1,1,""],TimerAddressLayer2:[16,1,1,""],TimerAddressLayer:[16,1,1,""],TimerBaseLayer:[16,1,1,""],TimerBdLayer:[16,1,1,""],TimerConsLayer:[16,1,1,""],TimerFixMemUsage:[16,1,1,""],TimerFixMemUsageAd:[16,1,1,""],TimerMemLayer:[16,1,1,""],TimerOsm:[16,1,1,""],TimerPolygonLayer:[16,1,1,""],TimerShpLayer:[16,1,1,""],TimerVertices:[16,1,1,""],TimerZoningLayer:[16,1,1,""]},"test.benchmark.AppendZoneTimer":{append_task:[16,2,1,""],append_zone2:[16,2,1,""],append_zone:[16,2,1,""],test_append_zone2:[16,2,1,""],test_append_zone3:[16,2,1,""],test_append_zone_0:[16,2,1,""],test_append_zone_1:[16,2,1,""]},"test.benchmark.BaseConsTimer":{create_bd:[16,2,1,""],create_shp:[16,2,1,""]},"test.benchmark.BaseTimer":{run:[16,2,1,""],test:[16,2,1,""]},"test.benchmark.ConsTimer":{test_10_remove_outside_parts:[16,2,1,""],test_11_explode_multi_parts:[16,2,1,""],test_12_remove_parts_below_ground:[16,2,1,""],test_13_merge_duplicates:[16,2,1,""],test_14_clean_duplicated_nodes_in_polygons:[16,2,1,""],test_15_add_topological_points:[16,2,1,""],test_16_merge_building_parts:[16,2,1,""],test_17_simplify:[16,2,1,""]},"test.benchmark.TimerAddressLayer":{set_up:[16,2,1,""],test_delete_addres_without_number1:[16,2,1,""],test_delete_addres_without_number2:[16,2,1,""]},"test.benchmark.TimerAddressLayer2":{test_get_highway_names1a:[16,2,1,""],test_get_highway_names1b:[16,2,1,""],test_get_highway_names1c:[16,2,1,""],test_get_highway_names2:[16,2,1,""],test_get_highway_names2a:[16,2,1,""],test_get_highway_names2b:[16,2,1,""]},"test.benchmark.TimerBaseLayer":{test_append:[16,2,1,""],test_reproject:[16,2,1,""]},"test.benchmark.TimerBdLayer":{test_01_append_all:[16,2,1,""]},"test.benchmark.TimerConsLayer":{c:[16,5,1,""],get_features:[16,2,1,""],get_fid_by_fid:[16,2,1,""],get_fid_by_fid_mem:[16,2,1,""],get_fids_by_dict_mem:[16,2,1,""],get_fids_by_filter:[16,2,1,""],get_fids_by_filter_mem:[16,2,1,""],get_fids_by_filter_shp:[16,2,1,""],get_fids_by_loop2:[16,2,1,""],get_fids_by_loop:[16,2,1,""],get_fids_by_loop_mem2:[16,2,1,""],get_fids_by_loop_mem:[16,2,1,""],get_fids_by_select:[16,2,1,""],get_fids_by_select_mem:[16,2,1,""],get_index:[16,2,1,""],get_index_shp:[16,2,1,""],zoning_histogram:[16,2,1,""]},"test.benchmark.TimerFixMemUsage":{test_append2:[16,2,1,""],test_reproject3:[16,2,1,""]},"test.benchmark.TimerFixMemUsageAd":{join_field2:[16,4,1,""],join_field:[16,4,1,""],test_append:[16,2,1,""],test_join:[16,2,1,""]},"test.benchmark.TimerMemLayer":{test_01_append_all:[16,2,1,""]},"test.benchmark.TimerOsm":{set_up:[16,2,1,""],test_remove:[16,2,1,""]},"test.benchmark.TimerPolygonLayer":{test_explode_multi_parts:[16,2,1,""],test_get_vertices:[16,2,1,""]},"test.benchmark.TimerShpLayer":{test_02_append_building:[16,2,1,""],test_03_append_part_other:[16,2,1,""]},"test.benchmark.TimerVertices":{test_duplicates_shp2:[16,2,1,""]},"test.benchmark.TimerZoningLayer":{test_multi:[16,2,1,""]},"test.check_mun_names":{run:[17,3,1,""]},"test.count_buildings":{run:[18,3,1,""]},"test.test_catatom":{TestCatAtom:[19,1,1,""],capture:[19,3,1,""],raiseException:[19,3,1,""]},"test.test_catatom.TestCatAtom":{setUp:[19,2,1,""],test_get_atom_file:[19,2,1,""],test_get_boundary:[19,2,1,""],test_get_layer_paths:[19,2,1,""],test_get_metadata_empty:[19,2,1,""],test_get_metadata_from_xml:[19,2,1,""],test_get_metadata_from_zip:[19,2,1,""],test_init:[19,2,1,""],test_is_empty:[19,2,1,""],test_list_municipalities:[19,2,1,""],test_read:[19,2,1,""]},"test.test_catatom2osm":{TestCatAtom2Osm:[20,1,1,""],TestQgsSingleton:[20,1,1,""]},"test.test_catatom2osm.TestCatAtom2Osm":{setUp:[20,2,1,""],test_end_messages:[20,2,1,""],test_exit:[20,2,1,""],test_export_layer:[20,2,1,""],test_gdal:[20,2,1,""],test_get_building1:[20,2,1,""],test_get_building2:[20,2,1,""],test_get_current_ad_osm:[20,2,1,""],test_get_current_bu_osm:[20,2,1,""],test_get_highway:[20,2,1,""],test_get_tasks:[20,2,1,""],test_get_translations:[20,2,1,""],test_get_zoning1:[20,2,1,""],test_get_zoning2:[20,2,1,""],test_init:[20,2,1,""],test_merge_address:[20,2,1,""],test_process_building:[20,2,1,""],test_process_parcel:[20,2,1,""],test_process_tasks:[20,2,1,""],test_process_zoning:[20,2,1,""],test_read_address:[20,2,1,""],test_read_osm:[20,2,1,""],test_run1:[20,2,1,""],test_run2:[20,2,1,""],test_run3:[20,2,1,""],test_run4:[20,2,1,""],test_run5:[20,2,1,""],test_write_osm:[20,2,1,""]},"test.test_catatom2osm.TestQgsSingleton":{test_new:[20,2,1,""]},"test.test_csvtools":{TestCsvTools:[21,1,1,""]},"test.test_csvtools.TestCsvTools":{test_csv2dict:[21,2,1,""],test_dict2csv:[21,2,1,""]},"test.test_download":{TestGetResponse:[22,1,1,""],TestProgressBar:[22,1,1,""],TestWget:[22,1,1,""]},"test.test_download.TestGetResponse":{test_get_response_bad:[22,2,1,""],test_get_response_ok:[22,2,1,""]},"test.test_download.TestProgressBar":{test_init:[22,2,1,""],test_update0:[22,2,1,""],test_update100:[22,2,1,""],test_update:[22,2,1,""]},"test.test_download.TestWget":{test_wget0:[22,2,1,""],test_wget:[22,2,1,""]},"test.test_hgwnames":{TestHgwnames:[23,1,1,""]},"test.test_hgwnames.TestHgwnames":{setUp:[23,2,1,""],tearDown:[23,2,1,""],test_fuzzy_dsmatch:[23,2,1,""],test_fuzzy_match:[23,2,1,""],test_nonfuzzy_match:[23,2,1,""],test_nonfyzzy_match:[23,2,1,""],test_normalize:[23,2,1,""],test_parse:[23,2,1,""]},"test.test_layer":{TestAddressLayer:[24,1,1,""],TestBaseLayer2:[24,1,1,""],TestBaseLayer:[24,1,1,""],TestConsLayer:[24,1,1,""],TestDebugWriter:[24,1,1,""],TestHighwayLayer:[24,1,1,""],TestParcelLayer:[24,1,1,""],TestPoint:[24,1,1,""],TestPolygonLayer:[24,1,1,""],TestZoningLayer:[24,1,1,""]},"test.test_layer.TestAddressLayer":{setUp:[24,2,1,""],tearDown:[24,2,1,""],test_append:[24,2,1,""],test_conflate:[24,2,1,""],test_get_highway_names:[24,2,1,""],test_join_field:[24,2,1,""],test_join_field_size:[24,2,1,""],test_join_void:[24,2,1,""],test_to_osm:[24,2,1,""]},"test.test_layer.TestBaseLayer":{setUp:[24,2,1,""],tearDown:[24,2,1,""],test_add_delete:[24,2,1,""],test_append_all_fields:[24,2,1,""],test_append_void:[24,2,1,""],test_append_with_query:[24,2,1,""],test_append_with_rename:[24,2,1,""],test_boundig_box:[24,2,1,""],test_copy_feature_all_fields:[24,2,1,""],test_copy_feature_with_rename:[24,2,1,""],test_copy_feature_with_resolve:[24,2,1,""],test_get_index:[24,2,1,""],test_reproject:[24,2,1,""],test_translate_field:[24,2,1,""]},"test.test_layer.TestBaseLayer2":{test_export_default:[24,2,1,""],test_export_other:[24,2,1,""]},"test.test_layer.TestConsLayer":{setUp:[24,2,1,""],tearDown:[24,2,1,""],test_add_topological_points:[24,2,1,""],test_append_building:[24,2,1,""],test_append_buildingpart:[24,2,1,""],test_append_cons:[24,2,1,""],test_append_othercons:[24,2,1,""],test_append_zone:[24,2,1,""],test_conflate:[24,2,1,""],test_delete_invalid_geometries:[24,2,1,""],test_explode_multi_parts:[24,2,1,""],test_get_parts:[24,2,1,""],test_index_of_building_and_parts:[24,2,1,""],test_index_of_parts:[24,2,1,""],test_is_building:[24,2,1,""],test_is_part:[24,2,1,""],test_is_pool:[24,2,1,""],test_merge_adjacent_features:[24,2,1,""],test_merge_adjacent_parts:[24,2,1,""],test_merge_building_parts:[24,2,1,""],test_move_address:[24,2,1,""],test_remove_outside_parts:[24,2,1,""],test_remove_parts_below_ground:[24,2,1,""],test_simplify1:[24,2,1,""],test_simplify2:[24,2,1,""],test_to_osm:[24,2,1,""],test_validate:[24,2,1,""]},"test.test_layer.TestDebugWriter":{test_add_point:[24,2,1,""],test_init:[24,2,1,""]},"test.test_layer.TestHighwayLayer":{test_init:[24,2,1,""],test_read_from_osm:[24,2,1,""]},"test.test_layer.TestParcelLayer":{test_init:[24,2,1,""],test_not_empty:[24,2,1,""]},"test.test_layer.TestPoint":{test_boundigBox:[24,2,1,""],test_get_corner_context:[24,2,1,""],test_get_spike_context:[24,2,1,""],test_init:[24,2,1,""]},"test.test_layer.TestPolygonLayer":{get_duplicates:[24,2,1,""],setUp:[24,2,1,""],tearDown:[24,2,1,""],test_explode_multi_parts:[24,2,1,""],test_get_area:[24,2,1,""],test_get_multipolygon:[24,2,1,""],test_get_outer_vertices:[24,2,1,""],test_get_parents_per_vertex_and_geometries:[24,2,1,""],test_get_vertices_list:[24,2,1,""]},"test.test_layer.TestZoningLayer":{setUp:[24,2,1,""],tearDown:[24,2,1,""],test_get_adjacents_and_geometries:[24,2,1,""],test_merge_adjacents:[24,2,1,""],test_set_cons_tasks:[24,2,1,""],test_set_tasks:[24,2,1,""]},"test.test_main":{TestMain:[25,1,1,""],capture:[25,3,1,""],raiseIOError:[25,3,1,""],raiseImportError:[25,3,1,""]},"test.test_main.TestMain":{test_IOError:[25,2,1,""],test_ImportError:[25,2,1,""],test_all:[25,2,1,""],test_bad_level:[25,2,1,""],test_building:[25,2,1,""],test_debug:[25,2,1,""],test_default:[25,2,1,""],test_list:[25,2,1,""],test_list_error:[25,2,1,""],test_no_args:[25,2,1,""],test_too_many_args:[25,2,1,""],test_version:[25,2,1,""]},"test.test_osm":{OsmTestCase:[26,1,1,""],TestOsm:[26,1,1,""],TestOsmElement:[26,1,1,""],TestOsmMultiPolygon:[26,1,1,""],TestOsmNode:[26,1,1,""],TestOsmPolygon:[26,1,1,""],TestOsmRelation:[26,1,1,""],TestOsmWay:[26,1,1,""]},"test.test_osm.OsmTestCase":{setUp:[26,2,1,""]},"test.test_osm.TestOsm":{test_attrs:[26,2,1,""],test_get:[26,2,1,""],test_getattr:[26,2,1,""],test_index:[26,2,1,""],test_init:[26,2,1,""],test_merge_duplicated:[26,2,1,""],test_properties:[26,2,1,""],test_remove:[26,2,1,""],test_replace:[26,2,1,""]},"test.test_osm.TestOsmElement":{test_attrs:[26,2,1,""],test_init:[26,2,1,""],test_is_new:[26,2,1,""],test_set_attrs:[26,2,1,""]},"test.test_osm.TestOsmMultiPolygon":{test_init:[26,2,1,""]},"test.test_osm.TestOsmNode":{test_attrs:[26,2,1,""],test_childs:[26,2,1,""],test_eq:[26,2,1,""],test_geometry:[26,2,1,""],test_getitem:[26,2,1,""],test_init:[26,2,1,""],test_init_round:[26,2,1,""],test_latlon:[26,2,1,""],test_ne:[26,2,1,""],test_set_attrs:[26,2,1,""],test_str:[26,2,1,""]},"test.test_osm.TestOsmPolygon":{test_init:[26,2,1,""]},"test.test_osm.TestOsmRelation":{test_append:[26,2,1,""],test_childs:[26,2,1,""],test_eq:[26,2,1,""],test_geometry:[26,2,1,""],test_init:[26,2,1,""],test_is_valid_multipolygon:[26,2,1,""],test_member_attrs:[26,2,1,""],test_member_eq:[26,2,1,""],test_member_ne:[26,2,1,""],test_ne:[26,2,1,""],test_outer_geometry:[26,2,1,""],test_ref:[26,2,1,""],test_remove:[26,2,1,""],test_replace:[26,2,1,""],test_type:[26,2,1,""]},"test.test_osm.TestOsmWay":{test_append:[26,2,1,""],test_childs:[26,2,1,""],test_clean_duplicated_nodes:[26,2,1,""],test_eq:[26,2,1,""],test_geometry:[26,2,1,""],test_init:[26,2,1,""],test_is_open:[26,2,1,""],test_ne:[26,2,1,""],test_remove:[26,2,1,""],test_replace:[26,2,1,""],test_search_node:[26,2,1,""],test_shoelace:[26,2,1,""]},"test.test_osmxml":{OsmxmlTest:[27,1,1,""]},"test.test_osmxml.OsmxmlTest":{test_deserialize:[27,2,1,""],test_serialize:[27,2,1,""]},"test.test_overpass":{TestQuery:[28,1,1,""]},"test.test_overpass.TestQuery":{test_add:[28,2,1,""],test_download:[28,2,1,""],test_get_url:[28,2,1,""],test_init:[28,2,1,""],test_read:[28,2,1,""],test_set_search_area:[28,2,1,""]},"test.test_report":{TestReport:[29,1,1,""]},"test.test_report.TestReport":{test_address_stats:[29,2,1,""],test_cons_end_stats:[29,2,1,""],test_cons_stats:[29,2,1,""],test_fixme_stats:[29,2,1,""],test_get:[29,2,1,""],test_getattr:[29,2,1,""],test_inc:[29,2,1,""],test_init:[29,2,1,""],test_setattr:[29,2,1,""],test_to_file:[29,2,1,""],test_to_string0:[29,2,1,""],test_to_string1:[29,2,1,""],test_to_string2:[29,2,1,""],test_to_string3:[29,2,1,""],test_validate1:[29,2,1,""],test_validate2:[29,2,1,""]},"test.test_setup":{TestSetup:[30,1,1,""]},"test.test_setup.TestSetup":{test_win:[30,2,1,""]},"test.test_translate":{TestTranslate:[31,1,1,""]},"test.test_translate.TestTranslate":{test_address_tags:[31,2,1,""],test_all_tags:[31,2,1,""],test_building_tags:[31,2,1,""]},catatom2osm:{CatAtom2Osm:[2,1,1,""],QgsSingleton:[2,1,1,""]},catatom:{Reader:[1,1,1,""],list_municipalities:[1,3,1,""]},csvtools:{csv2dict:[4,3,1,""],dict2csv:[4,3,1,""]},download:{ProgressBar:[5,1,1,""],get_response:[5,3,1,""],wget:[5,3,1,""]},hgwnames:{dsmatch:[6,3,1,""],match:[6,3,1,""],normalize:[6,3,1,""],parse:[6,3,1,""]},layer:{AddressLayer:[7,1,1,""],BaseLayer:[7,1,1,""],ConsLayer:[7,1,1,""],DebugWriter:[7,1,1,""],HighwayLayer:[7,1,1,""],ParcelLayer:[7,1,1,""],Point:[7,1,1,""],PolygonLayer:[7,1,1,""],ZoningLayer:[7,1,1,""],get_attributes:[7,3,1,""],is_inside:[7,3,1,""]},main:{process:[8,3,1,""],run:[8,3,1,""]},osm:{Element:[10,1,1,""],MultiPolygon:[10,1,1,""],Node:[10,1,1,""],Osm:[10,1,1,""],Polygon:[10,1,1,""],Relation:[10,1,1,""],Way:[10,1,1,""]},osmxml:{deserialize:[11,3,1,""],serialize:[11,3,1,""],write_elem:[11,3,1,""]},overpass:{Query:[12,1,1,""]},report:{Report:[13,1,1,""],int_format:[13,3,1,""]},setup:{winenv:[14,3,1,""]},test:{benchmark:[16,0,0,"-"],check_mun_names:[17,0,0,"-"],count_buildings:[18,0,0,"-"],test_catatom2osm:[20,0,0,"-"],test_catatom:[19,0,0,"-"],test_csvtools:[21,0,0,"-"],test_download:[22,0,0,"-"],test_hgwnames:[23,0,0,"-"],test_layer:[24,0,0,"-"],test_main:[25,0,0,"-"],test_osm:[26,0,0,"-"],test_osmxml:[27,0,0,"-"],test_overpass:[28,0,0,"-"],test_report:[29,0,0,"-"],test_setup:[30,0,0,"-"],test_translate:[31,0,0,"-"],unittest_main:[32,0,0,"-"]},translate:{address_tags:[33,3,1,""],all_tags:[33,3,1,""],building_tags:[33,3,1,""]}},objnames:{"0":["py","module","Python m\u00f3dulo"],"1":["py","class","Python clase"],"2":["py","method","Python m\u00e9todo"],"3":["py","function","Python funci\u00f3n"],"4":["py","staticmethod","Python m\u00e9todo est\u00e1tico"],"5":["py","attribute","Python atributo"]},objtypes:{"0":"py:module","1":"py:class","2":"py:method","3":"py:function","4":"py:staticmethod","5":"py:attribute"},terms:{"0295603cs6109n":7,"10x":16,"123k":16,"127x":16,"15x":16,"200x":16,"246x":16,"25x":16,"32k":16,"32x":16,"36x":16,"37x":16,"4000x":16,"70k":16,"70x":16,"9000x":16,"\u00edndic":[0,37],"a\u00f1ad":34,"class":[1,2,5,7,10,12,13,16,19,20,21,22,23,24,25,26,27,28,29,30,31],"default":[1,2,7,13],"else":[1,2],"espa\u00f1ol":[34,37,39],"export":[2,7,34],"extends":7,"float":7,"for":[1,2,6,7,10,11,12,16,24,33,38],"function":[6,7],"import":39,"int":7,"new":[7,10],"null":1,"return":7,"short":1,"static":[7,16],"this":[7,10],"try":[1,5],"void":7,"with":[1,2,6,7,10,16,32],Esto:39,Por:38,_cor:[2,7],_part:7,_pi:7,a_dict:4,a_path:[1,2],abbreviations:2,able:7,abov:7,abrir:38,absolut:16,according:7,acept:38,acut:7,acute_thr:7,add:[7,12],add_point:7,address:[1,2,7,33,34,39],address_osm:[2,13],address_stats:13,address_tags:33,addresslay:7,adds:[7,10,12],adecu:38,aditional:7,adjacent:7,adjacents:7,administrativ:1,adminunitnam:1,adquir:1,advertenci:37,after:1,aka:38,algun:34,all:[2,7,18,33,39],all_tags:[7,33],allow_empty:1,aloj:37,also:7,altern:34,altur:34,always:7,and:[1,2,5,7,10],angle:7,angle_:7,angle_v:7,angles:7,any:[1,7],api:[12,37],aplic:39,app:2,append:[7,10,11,16],append_task:16,append_zon:[7,16],append_zone2:16,appendzonetim:16,application:[2,7,14],apply:7,apt:38,archiv:[34,37,38,39],are:[7,10,12,16,24,34],arg1:7,arg2:7,args:[7,8,10,12,13,19,20,22,23,24,25,28],argument:39,arguments:7,assign:7,assings:7,associat:7,atom:[1,2,34,37,39],attr_list:10,attribut:[7,10],attrs:10,au_id:7,auxiliary:7,avanz:38,avo:7,ayud:39,b1ol:39,b3n_de_edifici:39,bar:[5,7],bas:[1,2,7,10,12,13,16,19,20,21,22,23,24,25,26,27,28,29,30,31],basebuildingtim:16,baseconstim:16,baselay:7,basenam:7,basepath:16,basetim:16,basic:5,bat:38,bbox:12,bdptz:39,becous:7,befor:7,belonging:2,belongs:7,below:7,benchmark:[9,15],benchmarking:16,berlin:12,best:6,betw:7,big:[7,16],bits:38,bool:[1,7],both:7,bottom:12,boundary:1,bounding:[7,12],bounding_box:7,boundingbox:[7,16],box:[7,12],brutally:16,building:[1,2,7,18,39],building_osm:2,building_tags:33,buildingpart:1,buildings:[2,7,16],but:[7,16],cadastr:[1,2,6],cadastral:7,cadastralparcel:[1,7],cadastralzoning:[1,2,7],call:[1,7],cambi:37,captur:[19,25],carpet:38,cas:[19,20,21,22,23,24,25,26,27,28,29,30,31],catastr:[34,37,38,39],catastral:39,catastro_esp:39,catatom2osm:[0,8,38,39],catatom:9,cath_thr:7,cathetus:7,center:7,check:17,check_mun_nam:[9,15],childs:10,choic:6,christoph:38,claus:12,cle:7,clean_duplicated_nod:10,clon:38,clos:[7,10],closest:7,cobertur:[0,37],codig:[0,34,37,38,39],collection:10,com:[1,38],comand:38,combin:[7,34,39],comenz:39,command:8,compat:9,compil:38,component_href:7,comprob:34,conect:10,configuration:2,conflat:7,conflation:[2,7],conflicts:7,conjunt:[34,37,39],cons_end_stats:13,cons_stats:13,consecutiv:10,conslay:[7,34],consol:38,constant:16,constim:16,construccion:39,constructions:[7,33],constructs:7,consult:39,contain:[7,10],containd:7,contains:2,conten:37,contents:9,context:7,contorn:34,conventions:6,convert:[2,7,16,37,39],coordinat:[2,10,24],copy:[2,7],copy_featur:7,corn:7,corrections:2,correspondient:39,corrig:34,could:[7,12],count:[7,18],count_buildings:[9,15],coverag:32,cp27:38,cp27m:38,creacion:34,creat:[1,2,7,10],create_bd:16,create_shp:[7,16],critical:39,crs:7,csv2dict:4,csv:[2,4],csv_path:4,csvtools:9,cuand:38,cuestion:34,current:[2,7],current_address:7,current_bu_osm:[7,16],current_building:16,dat:[2,7,10,11,13,34,37,39],dataset:[2,6,7,18],deb:39,debug:39,debugging:7,debugwrit:7,deciding:7,defaults:[2,7],defect:38,degr:7,delet:[2,7],delete_invalid_geometri:7,delete_shp:[2,7],dependent:38,depending:16,deriv:1,desact:39,desarroll:[34,38],descarg:[34,38,39],descoment:38,desd:38,dese:38,deserializ:[11,16],deshabilit:34,desktop:38,dest:16,dest_lay:16,detect:[7,34],detects:1,determin:7,dev:38,devel:38,devuelt:[1,7],devuelv:[1,6,7],dict2csv:4,dict:[7,24],dictionary:[2,4,7,10],dicts:7,differs:7,digit:39,direccion:[34,39],directori:[38,39],discov:[0,38],displays:5,dispon:39,distanc:7,distinct:7,distribution:7,documents:38,don:[2,7,16],dond:38,dos:39,down:12,downl:[1,9,12],downloads:[1,2,12],driver_nam:[2,7],dsmatch:6,dup_thr:24,duplicat:[10,24],each:[7,24],easy_install:38,edifici:[16,34,39],edit:38,edu:38,eficient:34,eid:10,eith:12,ejecut:[0,34,38,39],ejempl:38,element:[6,10],elements:[2,10,16],elimin:34,empty:1,encim:34,encoding:4,encuentr:39,end_messag:2,ends:2,english:37,enlac:34,enough:[6,7],entorn:38,entrac:2,entrad:[34,39],entranc:[2,7],entry:[8,32],equals:7,equivalent:39,error:[34,39],escritori:38,esri:[2,7],estadist:34,etiquet:34,etype:10,every:10,exampl:[7,12,16],exception:[1,5,7],excluding:7,exist:2,existent:34,existing:7,exists:2,exit:2,exp10:16,explode_multi_parts:7,export_lay:2,export_poly:7,expression:7,fails:[1,17],fall:34,fals:[1,5,7,12,16],fast:16,feat1:7,feat2:7,feat:7,featur:[1,7,16,18,33],ficher:[34,39],fid:[7,10],fids:[7,16],fids_by_filt:16,field:7,field_nam:7,field_names_subset:[7,16],fields:[7,33],fil:[1,2,4,7],filenam:[1,2,5,7,12],filt:7,fin:39,final_attribut:7,final_valu:7,first:[1,6,10],fixm:7,fixme_stats:13,floors:7,fold:2,foo:7,footprint:7,forc:1,force_zip:1,form:7,format:[2,11,16],from:[1,2,4,6,7,10,11,33],fuent:[1,2,4,5,6,7,8,10,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,33,34],full:2,func:[7,16],functions:4,fusion:34,fuzzy:6,fuzzywuzzy:39,gdal:39,gener:34,generat:[2,11],geojson:34,geom:7,geom_typ:7,geometri:7,geometry:[7,10,16],get:[1,5,7,10,13,16],get_adjacents_and_geometri:7,get_angl:7,get_are:7,get_atom_fil:1,get_attribut:7,get_boundary:1,get_building:2,get_corner_context:7,get_current_ad_osm:2,get_current_bu_osm:2,get_duplicat:24,get_featur:16,get_fid_by_f:16,get_fid_by_fid_mem:16,get_fids_by_dict_mem:16,get_fids_by_filt:16,get_fids_by_filter_mem:16,get_fids_by_filter_shp:16,get_fids_by_loop2:16,get_fids_by_loop:16,get_fids_by_loop_mem2:16,get_fids_by_loop_mem:16,get_fids_by_select:16,get_fids_by_select_mem:16,get_highway:2,get_highway_nam:7,get_image_links:7,get_index:[7,16],get_index_shp:16,get_layer_paths:1,get_metadat:1,get_multipolygon:7,get_outer_vertic:7,get_parents_per_vertex_and_geometri:7,get_parts:7,get_respons:5,get_spike_context:7,get_sys_inf:13,get_tasks:2,get_translations:2,get_url:12,get_vertices_list:7,get_zoning:2,getfeatur:16,gets:[1,2],ggmmm:39,git:[37,38],github:[38,39],giv:[1,7,10],gml:[1,2,16],gml_path:1,gmls:16,gob:39,gohlk:38,good:6,grand:34,great:7,ground:7,group:7,groups:7,grown:16,grows:16,gui:7,hac:34,hav:7,help:[4,10,39],herramient:[37,38,39],hgwnam:9,highway:[2,6,7],highway_nam:2,highway_typ:2,highwaylay:7,highways:[2,7],html:39,http:[5,38,39],https:[38,39],hub:37,identifi:7,idiom:37,ignor:7,imagen:34,implement:10,implic:39,importaci:39,imprim:39,inc:13,includ:7,increments:5,index:[7,16,39],index_of_building_and_parts:7,index_of_parts:7,index_of_pools:7,indic:39,individual:39,infil:11,info:39,inform:34,inicial:34,initially:16,inner:[7,10],insid:7,inspire:[2,37,39],instal:38,instalacion:37,install:[38,39],instanc:2,int_format:13,intent:38,interfac:12,internet:38,intersects:16,introduc:38,inval:7,is_acut:7,is_building:7,is_clos:10,is_empty:1,is_insid:7,is_new:10,is_op:10,is_part:7,is_pool:7,is_spik:7,is_valid_multipolygon:10,is_zigzag:7,isn:2,iter:6,iterabl:6,iterator:7,its:[7,10],javi:38,javiersanp:[38,39],join:7,join_field2:16,join_field:[7,16],join_field_nam:[7,16],join_fieldsnam:7,josm:34,json:2,keeps:2,key:13,keywargs:[19,20,22,23,24,25,28],kwargs:[7,10,13,25],kwds:[19,25],kyngcha:38,label:7,lambd:7,lanz:38,lat:10,latitud:10,launch:2,lay:[1,2,9,16,33],layernam:1,layers:[7,16],leem:37,left:12,len:16,less:[7,16],level:7,levelnam:7,levels:7,levenshtein:38,lfd:38,libr:38,libs:38,limit:34,lin:[8,16],line:38,linestring:7,linux:37,list:[1,2,6,7,10,38,39],list_municipaliti:1,local:7,localid:7,locat:2,log:[12,16,39],log_level:39,lon:10,longitud:10,look:6,low:7,lug:39,mac:37,main:[2,9],mak:38,manual:39,many:[5,10],manzana:2,mark:7,mas:34,match:6,matching:6,max_level:7,maximum:7,maximun:6,may:7,md_path:1,mechanism:7,mejor:34,mem:16,memb:10,members:[7,10],memory:[7,16],menor:34,mensaj:39,merg:[2,7,10],merge_address:2,merge_adjacent_featur:7,merge_adjacent_parts:7,merge_adjacents:7,merge_building_parts:7,merge_duplicat:10,merge_greatest_part:7,met:12,metadat:1,meters:7,method:7,methodnam:[19,20,21,22,23,24,25,26,27,28,29,30,31],methods:7,metod:34,microsoft:38,min_level:7,minhap:39,minimum:[7,12],mkdir:38,mod:7,model:10,modul:9,moment:7,mor:[7,16],mov:7,move_address:[2,7],msvcrt:38,much:16,muestr:39,muev:34,multiparts:7,multipl:2,multipolgon:7,multipolygon:10,multisurfac:16,mun:16,mun_fails:17,municipaliti:1,municipality:17,municipi:[34,39],must:7,nam:[1,2,6,7,10,12,16,17],ndx:7,ndxa:7,near:7,nearest:[7,24],necesari:38,need:2,nev:[7,10],next:16,ningun:39,nivel:39,nod:[2,10,12,34],nombr:[34,39],non:[1,7,10,11,16,24],normaliz:6,not:[1,2,6,7],numb:[7,16,18],obj:16,object:[1,6,7,10,12,13,16],objects:6,obtain:6,occurenc:10,oficial:38,oficin:39,ogr:[7,16],one:[2,7,10],ones:6,only:[7,10],opcion:[34,38,39],open:[10,16],openstreetmap:[10,39],optional:7,options:[2,8],orden:38,org:[38,39],original:2,original_attribut:7,original_valu:7,orphand:10,osgeo4w:38,osm:[1,2,6,7,9,11,12,16,33,34,37,39],osm_path:16,osm_stats:13,osmosis:7,osmtestc:26,osmxml:[9,16],osmxmltest:27,otherconstruction:1,out:[7,10],outer_geometry:10,outfil:11,output:[2,7,11,12],outputh:2,outsid:7,over:7,overpass:[1,2,7,9],overriding:7,overwrit:7,packag:9,pagin:38,pair:10,pantall:38,paquet:38,par:[0,34,37,38,39],parametr:[1,2,6,7],parcel:[7,39],parcellay:7,parcels:7,parent:7,parents:[7,10],pars:[6,7],parsing:[2,6],part:[7,34,39],parts:[2,7,10,16],path:[2,7],pattern:7,pd_id:7,penultim:38,percent:5,pertenec:34,pip:38,piscin:34,point:[7,8,32],points:7,poligono:2,polygon:[7,10],polygonlay:7,polygons:[7,16],pool:7,pools:[2,7],position:[7,10,16],postaldescriptor:1,precondition:[1,2,7],predetermin:39,preferenc:14,prefix:[7,16],present:1,primer:38,print:16,proces:39,process:[2,7,8,16],process_building:2,process_parcel:2,process_tasks:2,process_zoning:2,program:[38,39],progress:5,progressb:5,projection:7,properly:2,properti:10,propuest:39,prov:39,prov_cod:1,providerlib:7,provinc:1,provincial:39,prueb:[0,34,38,39],psutil:39,punt:34,purposess:7,put:[2,7,17],pyqgis:[38,39],python:[0,38],python_levenshtein:38,pythonlibs:38,qgis:[1,2,7,38],qgsapplication:2,qgscoordinatereferencesystem:7,qgsfeatur:7,qgsfeaturerequest:[7,16],qgsfields:7,qgsgeometry:7,qgspoint:7,qgssingleton:2,qgsspatialindex:7,qgsvectorfilewrit:7,qgsvectorlay:[1,2,7],quer:38,query:[2,7,12],quickly:16,radius:7,rais:[1,5],raiseexception:19,raiseimporterror:25,raiseioerror:25,randon:16,rap:34,rati:6,read:[1,2,4,12],read_address:2,read_from_osm:7,read_osm:2,reads:2,receiv:7,reconstru:34,red:38,reduc:[7,34],reescrib:34,ref:[2,10,24],referenc:7,referent:37,registr:[37,39],relat:4,relation:10,relations:[7,10],relativ:2,remov:[7,10],remove_inner_rings:7,remove_outside_parts:7,renam:7,renaming:7,rep:34,repart:39,replac:[7,10],report:9,repositori:38,reproject:[7,16],request:[7,16],requests:39,requisit:[37,38],resolution:17,resolv:7,resolving:7,respons:5,rest:7,result:[6,12,38,39],results:1,returns:[1,2,6,7,10,12,24],right:12,ring:[7,10],rings:[7,10],rol:10,run:[2,8,16,17,18,32],runtest:[19,20,21,22,23,24,25,26,27,28,29,30,31],rustic:[2,7],rut:[38,39],rzoning:7,sal:39,sam:[2,7,10],script:7,sdgc:7,search:[6,7,12],search_are:12,search_nod:10,see:7,segment:7,segments:7,seleccion:[16,38,39],selecction:16,select:16,selection:16,self:[1,10,16],ser:38,serializ:11,servic:[1,2],servici:[37,39],set:[2,7,10,11,12],set_search_are:12,set_tasks:7,set_up:16,setfilterfids:16,sets:2,setup:[9,17,19,20,23,24,26],setuptools:38,shapefil:[2,7],shar:7,shoelac:10,simetry:10,simil:16,simplif:34,simplific:34,simplify:7,sistem:38,siz:16,slow:16,small:7,softwar:38,sol:39,solicit:38,som:[7,16],soport:34,sourc:[1,2,7,16,33],source_dat:7,source_lay:[7,16],spanish:2,spec:7,specification:7,speedup:39,spik:7,split:7,splits:2,sport:34,standalon:7,statement:12,statements:12,statistics:13,step:[5,13],still:16,str:[1,2,6,7],straight:7,straight_thr:7,stream:5,street:[2,6,7],string:[6,10],strings:7,sub:39,submodul:9,sud:38,suff:16,suger:38,sugier:38,sum:13,tabl:7,tag:2,tags:[2,7,10,33],tags_translation:7,tambien:34,tar:[34,39],target:7,target_crs:7,target_field_nam:[7,16],task:[7,16],tasks:39,teardown:[23,24],termin:39,test:[7,9,38],test_01_append_all:16,test_02_append_building:16,test_03_append_part_oth:16,test_10_remove_outside_parts:16,test_11_explode_multi_parts:16,test_12_remove_parts_below_ground:16,test_13_merge_duplicat:16,test_14_clean_duplicated_nodes_in_polygons:16,test_15_add_topological_points:16,test_16_merge_building_parts:16,test_17_simplify:16,test_add:28,test_add_delet:24,test_add_point:24,test_add_topological_points:24,test_address_stats:29,test_address_tags:31,test_all:25,test_all_tags:31,test_append2:16,test_append:[16,24,26],test_append_all_fields:24,test_append_building:24,test_append_buildingpart:24,test_append_cons:24,test_append_othercons:24,test_append_v:24,test_append_with_query:24,test_append_with_renam:24,test_append_zon:24,test_append_zone2:16,test_append_zone3:16,test_append_zone_0:16,test_append_zone_1:16,test_attrs:26,test_bad_level:25,test_boundig_box:24,test_boundigbox:24,test_building:25,test_building_tags:31,test_catatom2osm:[9,15],test_catatom:[9,15],test_childs:26,test_clean_duplicated_nod:26,test_conflat:24,test_cons_end_stats:29,test_cons_stats:29,test_copy_feature_all_fields:24,test_copy_feature_with_renam:24,test_copy_feature_with_resolv:24,test_csv2dict:21,test_csvtools:[9,15],test_debug:25,test_default:25,test_delete_addres_without_number1:16,test_delete_addres_without_number2:16,test_delete_invalid_geometri:24,test_deserializ:27,test_dict2csv:21,test_downl:[9,15,28],test_duplicates_mem:16,test_duplicates_shp2:16,test_end_messag:20,test_eq:26,test_exit:20,test_explode_multi_parts:[16,24],test_export_default:24,test_export_lay:20,test_export_oth:24,test_fixme_stats:29,test_fuzzy_dsmatch:23,test_fuzzy_match:23,test_gdal:20,test_geometry:26,test_get:[26,29],test_get_adjacents_and_geometri:24,test_get_are:24,test_get_atom_fil:19,test_get_boundary:19,test_get_building1:20,test_get_building2:20,test_get_corner_context:24,test_get_current_ad_osm:20,test_get_current_bu_osm:20,test_get_highway:20,test_get_highway_nam:24,test_get_highway_names1:16,test_get_highway_names1b:16,test_get_highway_names1c:16,test_get_highway_names2:16,test_get_highway_names2b:16,test_get_index:24,test_get_layer_paths:19,test_get_metadata_empty:19,test_get_metadata_from_xml:19,test_get_metadata_from_zip:19,test_get_multipolygon:24,test_get_outer_vertic:24,test_get_parents_per_vertex_and_geometri:24,test_get_parts:24,test_get_response_b:22,test_get_response_ok:22,test_get_spike_context:24,test_get_tasks:20,test_get_translations:20,test_get_url:28,test_get_vertic:16,test_get_vertices_list:24,test_get_zoning1:20,test_get_zoning2:20,test_getattr:[26,29],test_getitem:26,test_hgwnam:[9,15],test_importerror:25,test_inc:29,test_index:26,test_index_of_building_and_parts:24,test_index_of_parts:24,test_init:[19,20,22,24,26,28,29],test_init_round:26,test_ioerror:25,test_is_building:24,test_is_empty:19,test_is_new:26,test_is_op:26,test_is_part:24,test_is_pool:24,test_is_valid_multipolygon:26,test_join:16,test_join_field:24,test_join_field_siz:24,test_join_v:24,test_latlon:26,test_lay:[9,15],test_list:25,test_list_error:25,test_list_municipaliti:19,test_main:[9,15],test_member_attrs:26,test_member_eq:26,test_member_n:26,test_merge_address:20,test_merge_adjacent_featur:24,test_merge_adjacent_parts:24,test_merge_adjacents:24,test_merge_building_parts:24,test_merge_duplicat:26,test_move_address:24,test_multi:16,test_n:26,test_new:20,test_no_args:25,test_nonfuzzy_match:23,test_nonfyzzy_match:23,test_normaliz:23,test_not_empty:24,test_osm:[9,15],test_osmxml:[9,15],test_outer_geometry:26,test_overpass:[9,15],test_p:23,test_process_building:20,test_process_parcel:20,test_process_tasks:20,test_process_zoning:20,test_properti:26,test_r:[19,28],test_read_address:20,test_read_from_osm:24,test_read_osm:20,test_ref:26,test_remov:[16,26],test_remove_outside_parts:24,test_remove_parts_below_ground:24,test_replac:26,test_report:[9,15],test_reproject3:16,test_reproject:[16,24],test_run1:20,test_run2:20,test_run3:20,test_run4:20,test_run5:20,test_search_nod:26,test_serializ:27,test_set_attrs:26,test_set_cons_tasks:24,test_set_search_are:28,test_set_tasks:24,test_setattr:29,test_setup:[9,15],test_shoelac:26,test_simplify1:24,test_simplify2:24,test_str:26,test_to_fil:29,test_to_osm:24,test_to_string0:29,test_to_string1:29,test_to_string2:29,test_to_string3:29,test_too_many_args:25,test_translat:[9,15],test_translate_field:24,test_typ:26,test_updat:22,test_update0:22,test_update100:22,test_validat:24,test_validate1:29,test_validate2:29,test_version:25,test_wget0:22,test_wget:22,test_win:30,test_write_osm:20,testaddresslay:24,testbaselay:24,testbaselayer2:24,testc:[19,20,21,22,23,24,25,26,27,28,29,30,31],testcatatom2osm:20,testcatatom:19,testconslay:24,testcsvtools:21,testdebugwrit:24,testgetrespons:22,testhgwnam:23,testhighwaylay:24,testing:7,testmain:25,testosm:26,testosmelement:26,testosmmultipolygon:26,testosmnod:26,testosmpolygon:26,testosmrelation:26,testosmway:26,testparcellay:24,testpoint:24,testpolygonlay:24,testprogressb:22,testqgssingleton:20,testquery:28,testreport:29,tests:[2,16],testsetup:30,testtranslat:31,testwget:22,testzoninglay:24,text:[5,6],than:[7,16,24],that:[2,7],the:[1,2,5,6,7,10,12,16],them:7,ther:2,they:24,thoroughfarenam:1,threshold:7,tim:5,timeraddresslay:16,timeraddresslayer2:16,timerbaselay:16,timerbdlay:16,timerconslay:16,timerfixmemusag:16,timerfixmemusagead:16,timermemlay:16,timerosm:16,timerpolygonlay:16,timershplay:16,timervertic:16,timerzoninglay:16,tip:[1,7],tn_id:7,to_fil:13,to_osm:7,to_string:13,tod:39,too:7,tool:2,top:12,topolog:34,topological:7,topology:7,total:[5,7],traduccion:34,transform:[6,7],translat:[7,9],translate_field:7,translati:33,translation:7,translations:[2,7,33],tri:1,tru:[2,7,10,12],tupl:10,two:24,txt:38,type:[2,10],types:2,uci:38,underscor:7,uniqu:[2,7,10],unittest:[0,19,20,21,22,23,24,25,26,27,28,29,30,31,38],unittest_main:[9,15],updat:5,uplo:[7,10],urban:[2,7],url:[1,2,5,12],usag:16,usand:38,usar:38,use:[1,12],used:7,users:38,using:2,uso:37,usually:1,utf:4,utility:7,uzoning:7,val:[1,7,10],valid:34,validat:[7,13],valor:[1,7],valu:[2,7],van:38,vari:34,vcpython27:38,vector:[1,2],ver:39,version:[34,39],vertex:7,vertexs:7,vertic:[7,24,34],very:16,vial:34,visual:38,warning:39,way:10,ways:10,webinspir:39,wget:5,when:16,whl:38,wiki:39,will:7,win_amd64:38,windows:[34,37],winenv:14,winn:16,witch:7,without:[7,12],witn:10,wkbmultipolygon:7,wkbpolygon:7,work:7,writ:[2,4,7],write_elem:11,write_osm:2,wrongly:16,www:[38,39],xlink:7,xml:[2,11,12,34],you:7,zag:[7,34],zig:[7,34],zip:1,zip_cod:1,zip_path:1,zon:[7,16],zonif:39,zoning:[1,7,16,39],zoning_gml:16,zoning_histogram:16,zoninglay:7},titles:["Referencia API","catatom module","catatom2osm module","compat module","csvtools module","download module","hgwnames module","layer module","main module","CatAtom2Osm","osm module","osmxml module","overpass module","report module","setup module","test package","test.benchmark module","test.check_mun_names module","test.count_buildings module","test.test_catatom module","test.test_catatom2osm module","test.test_csvtools module","test.test_download module","test.test_hgwnames module","test.test_layer module","test.test_main module","test.test_osm module","test.test_osmxml module","test.test_overpass module","test.test_report module","test.test_setup module","test.test_translate module","test.unittest_main module","translate module","Registro de cambios","Cobertura del c\u00f3digo","\u00cdndice","\u00a1Bienvenido a la documentaci\u00f3n de CatAtom2Osm!","Instalaci\u00f3n","L\u00e9eme"],titleterms:{"\u00edndic":36,advertenci:39,api:0,benchmark:16,bienven:37,cambi:34,catatom2osm:[2,9,37],catatom:1,check_mun_nam:17,cobertur:35,codig:35,compat:3,contents:15,count_buildings:18,csvtools:4,document:[37,39],downl:5,hgwnam:6,instalacion:[38,39],lay:7,leem:39,linux:38,mac:38,main:8,modul:[1,2,3,4,5,6,7,8,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33],osm:10,osmxml:11,overpass:12,packag:15,referent:0,registr:34,report:13,requisit:39,setup:14,submodul:15,test:[15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32],test_catatom2osm:20,test_catatom:19,test_csvtools:21,test_downl:22,test_hgwnam:23,test_lay:24,test_main:25,test_osm:26,test_osmxml:27,test_overpass:28,test_report:29,test_setup:30,test_translat:31,translat:33,unittest_main:32,uso:39,windows:38}})