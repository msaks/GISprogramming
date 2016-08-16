import arcpy
mxd = arcpy.mapping.MapDocument("CURRENT")
fields = ["CITY_NAME", "STATE_NAME", "POP1990"]
for df in arcpy.mapping.ListDataFrames(mxd):
    for layer in arcpy.mapping.ListLayers(mxd,"",df):
        if layer.isFeatureLayer and not (layer.isBroken):
            if layer.name == "CITIES":
                exp = "CAPITAL = " + "'" + "Y" + "'"
                print exp
                with arcpy.da.SearchCursor(layer, fields, where_clause=exp) as cursor:
                    for row in cursor:
                        print('{0}, {1}, {2}'.format(row[0], row[1], row[2]))
            if layer.name == "CITIES":
                fields = ["CITY_NAME", "SHAPE@X", "SHAPE@Y"]
                exp = "CITY_NAME = " + "'" + "Derby" + "'" + "AND" + " " + "STATE_NAME = " + "'" + "Kansas" + "'"
                xOffset = .02
                yOffset = .03
                #print exp
                with arcpy.da.SearchCursor(layer, fields, where_clause=exp) as cursor:
                    for row in cursor:
                        row_values = ['Shangri-La', ((row[1] + xOffset),), ((row[2] + yOffset),)]
                with arcpy.da.InsertCursor(layer, fields) as cursor:
                    cursor.insertRow([row_values])
                    del cursor
                        
                    
                        

                        
