Write-Output "Delete odd files in main and subset repository"
Remove-Item -Path ".\build\*" -Recurse
Remove-Item -Path "..\easyclimate\docs\*" -Recurse

Write-Output "Build docs"
.\make html

Write-Output "Copy docs from subset repository to main repository"
Copy-Item -Path ".\build\html\*" -Destination "..\easyclimate\docs\" -Recurse
Remove-Item -Path ".\build\*" -Recurse

Write-Output "Finished!"