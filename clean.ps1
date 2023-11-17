Remove-Item -Path ".\source\auto_gallery_output\*" -Recurse
Remove-Item -Path ".\source\api_index\generated\*"

# Delete temp file in main repository
$local_path = Get-Location
Set-Location ..\easyclimate
python -u .\delete_pycache.py
Set-Location $local_path