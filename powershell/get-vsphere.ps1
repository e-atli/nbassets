#!/usr/bin/pwsh

$VCENTER = $args[0]
$CREDFILE = $args[1]
$PATHPREFIX = $args[2]

If ($VCENTER -eq $Null) { Exit }
If ($CREDFILE -eq $Null) { Exit }
If ($PATHPREFIX -eq $Null) { $PATHPREFIX = "." }

$CREDENTIAL = Import-Clixml -Path $CREDFILE
Connect-VIServer -Server $VCENTER -Credential $CREDENTIAL | Out-Null

# Cluster ermitteln
$CLUSTERS = Get-Cluster

Foreach ($CLUSTER in $CLUSTERS) {
  # Save Cluster Information
  "TYPE = 'VMware vSphere'" | Out-File -FilePath "$PATHPREFIX/clusters/cl_$CLUSTER.py"
  "NAME = '$CLUSTER'" | Out-File -FilePath "$PATHPREFIX/clusters/cl_$CLUSTER.py" -Append

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

    # Netzwerkkarten ermitteln
    $NICS = Get-NetworkAdapter -VM $VM

    Foreach ($NIC in $NICS) {
      $INTERFACE = $NIC.Name
      $MAC_ADDRESS = $NIC.MacAddress

      Write-Output "INTERFACE = '$INTERFACE'",
        "MAC_ADDRESS = '$MAC'" | Out-File -FilePath "$PATHPREFIX/virtual_machines/vm_$CLUSTER.py" -Append
    }
  }
}
