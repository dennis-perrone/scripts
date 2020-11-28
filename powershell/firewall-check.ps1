####################################################################
# Script Name : firewall-check.ps1
# Description : Checks to see if ports are open on a firewall
# Args :
# Author : Dennis Perrone 
# GitHub : www.github.com/dennis-perrone
####################################################################

function ping-test{

$desthost = Read-Host 'What is the destination address?'
$destport = Read-Host 'What port is being checked?'

Test-NetConnection -InformationLevel "Detailed" -Port $destport -ComputerName $desthost | Select ComputerName, TcpTestSucceeded

}

ping-test
