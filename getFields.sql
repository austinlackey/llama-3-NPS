SELECT        Parks.Name AS ParkName, Parks.UnitCode, FieldNames.Name AS FieldName, FieldNames.Label AS FieldCode, FieldNames.Formula
FROM            FieldNames INNER JOIN
                         Parks ON FieldNames.ParkId = Parks.ParkId