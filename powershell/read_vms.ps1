#!/usr/bin/pwsh

Connect-VIServer -Server $args[0] -User $args[1] -Password $args[2] | Out-Null

# Cluster ermitteln
$CLUSTER = Get-Cluster | ForEach { $_.Name }
#Write-Host "CLUSTER = '$CLUSTER'"

$VMS = Get-VM | Foreach { $_.Name }

$VMS | ForEach {
  Write-Host "CLUSTER = '$CLUSTER'"
  Write-Host "NAME = '$_'"

  $VCPUS = Get-VM -Name $_ | ForEach { $_.NumCpu }
  Write-Host "VCPUS = '$VCPUS'"

  $MEMORY = Get-VM -Name $_ | ForEach { $_.MemoryMB }
  Write-Host "MEMORY = '$MEMORY'"

  $DISK = [math]::round((Get-HardDisk -vm $_ | Measure-Object -Sum CapacityGB).Sum)
  Write-Host "DISK = '$DISK'"

  $STATUS = Get-VM -Name $_ | ForEach { $_.PowerState }
  Write-Host "STATUS = '$STATUS'"

  $ROLE = ''
  $ROLE = Get-TagAssignment -Entity $_ -Category 'Role' | foreach { $_.Tag.Name }
  #$ROLE = (Get-Annotation -CustomAttribute 'Role' -Entity $_).Value
  IF ($ROLE) {
    Write-Host "ROLE = '$ROLE'"
    }

  Write-Host ""
  }
