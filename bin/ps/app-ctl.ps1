
$scriptpath = split-path -parent $MyInvocation.MyCommand.Definition
$apppath = $scriptpath + '\..\venv\Scripts\python ' + $scriptpath + '\..\app.py'
Invoke-Expression $apppath

