# Capture a window by handle with PrintWindow(PW_RENDERFULLCONTENT), which includes composited child views
# (Electron BrowserView/WebContentsView overlays) that page-level screenshots miss.
param([Parameter(Mandatory)][string]$Hwnd, [Parameter(Mandatory)][string]$Out)
Add-Type -AssemblyName System.Drawing
Add-Type @"
using System; using System.Runtime.InteropServices;
public static class PW {
  [StructLayout(LayoutKind.Sequential)] public struct RECT { public int L, T, R, B; }
  [DllImport("user32.dll")] public static extern bool SetProcessDPIAware();
  [DllImport("user32.dll")] public static extern bool PrintWindow(IntPtr h, IntPtr hdc, uint flags);
  [DllImport("dwmapi.dll")] public static extern int DwmGetWindowAttribute(IntPtr h, int attr, out RECT r, int size);
}
"@
[PW]::SetProcessDPIAware() | Out-Null
$h = [IntPtr][Int64]$Hwnd
$r = New-Object PW+RECT
[PW]::DwmGetWindowAttribute($h, 9, [ref]$r, 16) | Out-Null   # 9 = DWMWA_EXTENDED_FRAME_BOUNDS (no invisible borders)
$w = $r.R - $r.L; $ht = $r.B - $r.T
$bmp = New-Object System.Drawing.Bitmap $w, $ht
$g = [System.Drawing.Graphics]::FromImage($bmp)
$hdc = $g.GetHdc(); [PW]::PrintWindow($h, $hdc, 2) | Out-Null; $g.ReleaseHdc($hdc); $g.Dispose()
$bmp.Save($Out, [System.Drawing.Imaging.ImageFormat]::Png); $bmp.Dispose()
"saved $Out ${w}x${ht}"
