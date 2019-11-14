#!/usr/bin/pwsh

$VCENTER = $args[0]
$USER = $args[1]
$PASS = $args[2]
$PATHPREFIX = $args[3]

If ($VCENTER -eq $Null) { Exit }
If ($USER -eq $Null) { Exit }
If ($PASS -eq $Null) { Exit }
If ($PATHPREFIX -eq $Null) { $PATHPREFIX = "." }

Connect-VIServer -Server $VCENTER -User $USER -Password $PASS | Out-Null

# Cluster ermitteln
$CLUSTERS = Get-Cluster

Foreach ($CLUSTER in $CLUSTERS) {
  # Save Cluster Information
  "TYPE = 'VMware vSphere'" | Out-File -FilePath "$PATHPREFIX/clusters/cl_$CLUSTER.py"
  "CLUSTER = '$CLUSTER'" | Out-File -FilePath "$PATHPREFIX/clusters/cl_$CLUSTER.py" -Append
  
  # Save VM Information
  "CLUSTER = '$CLUSTER'" | Out-File -FilePath "$PATHPREFIX/virtual_machines/vm_$CLUSTER.py"
  
  $VMS = Get-VM -Location $CLUSTER

  Foreach ($VM in $VMS) {
    $NAME = $VM.Name
    $VCPUS = $VM.NumCpu
    $MEMORY = $VM.MemoryMB
    $DISK = [math]::round((Get-HardDisk -vm $VM | Measure-Object -Sum CapacityGB).Sum)
    $STATUS = $VM.PowerState
    $ROLE = ((Get-TagAssignment -Entity $VM -Category 'Role')).Tag.Name

    Write-Output "",
      "NAME = '$NAME'",
      "VCPUS = '$VCPUS'",
      "MEMORY = '$MEMORY'",
      "DISK = '$DISK'",
      "STATUS = '$STATUS'" | Out-File -FilePath "$PATHPREFIX/virtual_machines/vm_$CLUSTER.py" -Append

    IF ($ROLE) { "ROLE = '$ROLE'" | Out-File -FilePath "$PATHPREFIX/virtual_machines/vm_$CLUSTER.py" -Append }
    
#    "NAME = '$NAME'" | Out-File -FilePath "$PATHPREFIX/virtual_machines/vm_$CLUSTER.py" -Append
#    "VCPUS = '$VCPUS'" | Out-File -FilePath "$PATHPREFIX/virtual_machines/vm_$CLUSTER.py" -Append
#    "MEMORY = '$MEMORY'" | Out-File -FilePath "$PATHPREFIX/virtual_machines/vm_$CLUSTER.py" -Append
#    "DISK = '$DISK'" | Out-File -FilePath "$PATHPREFIX/virtual_machines/vm_$CLUSTER.py" -Append
#    "STATUS = '$STATUS'" | Out-File -FilePath "$PATHPREFIX/virtual_machines/vm_$CLUSTER.py" -Append
#    IF ($ROLE) { "ROLE = '$ROLE'" | Out-File -FilePath "$PATHPREFIX/virtual_machines/vm_$CLUSTER.py" -Append }
#    "" | Out-File -FilePath "$PATHPREFIX/virtual_machines/vm_$CLUSTER.py" -Append
  }

"" | Out-File -FilePath "$PATHPREFIX/virtual_machines/vm_$CLUSTER.py" -Append
}
