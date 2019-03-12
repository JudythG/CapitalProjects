import json

fiscalYear = 2018
startDate = ''
area = ''
assetType = ''
planningStatus = ''

capProjsAPI = {'fiscal_year': [fiscalYear], 'start_date': [startDate], 'area': [area], 'asset_type': [assetType], 'planning_status': [planningStatus]}
print (json.dumps (capProjsAPI))

jsonStruct = json.dumps (capProjsAPI)
print (json.loads (jsonStruct))

