$scriptpath = split-path -parent $MyInvocation.MyCommand.Definition

$venvpath = $scriptpath + '\..\venv'

# echo $venvpath

if (test-path $venvpath) {
    remove-item $venvpath -recurse -force
}

C:\Python34\python -m venv $venvpath

echo ""
echo "---------------------------------------------------------------------------------"
echo "Virtual Environment installed... to activate the environment in your shell run:"
echo "---------------------------------------------------------------------------------"
echo ".\venv\Scripts\Activate.ps1"
echo ""
