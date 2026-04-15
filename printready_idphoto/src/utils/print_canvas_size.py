"""
Inches = Pixels / PPI
Pixels = Inches × PPI
Inches = Centimeters / 2.54
1 cm = 0.393701 inches
1 inch = 25.4 mm
Centimeters = Inches × 2.54
Centimeters = (Pixels / PPI) × 2.54
Pixels = (Centimeters / 2.54) × PPI
"""


def mm_to_inches(mm):
    return mm / 25.4


def inches_to_pixels(inches, ppi=96):
    return int(inches * ppi)


def getsize_a4_canvas(ppi):
    """A4 paper size is 210 x 297 mm.
        - Width: 210 mm / 25.4 mm/inch ≈ 8.27 inches
        - Height: 297 mm / 25.4 mm/inch ≈ 11.69 inches
        - Width in pixels: 8.27 inches * 96 PPI ≈ 796 pixels
        - Height in pixels: 11.69 inches * 96 PPI ≈ 1120 pixels

    Therefore, the A4 paper size in inches is approximately 8.27 x 11.69 inches, and in pixels (assuming 96 PPI) it would be approximately 796 x 1120 pixels.
    """
    # A4 paper size in mm
    width_mm = 210
    height_mm = 297
    # Convert mm to inches
    width_inches = mm_to_inches(width_mm)
    height_inches = mm_to_inches(height_mm)
    # Convert inches to pixels
    width_pixels = inches_to_pixels(width_inches, ppi)
    height_pixels = inches_to_pixels(height_inches, ppi)

    print("A4 paper size in inches:")
    print(f"Width: {width_inches:.2f} inches")
    print(f"Height: {height_inches:.2f} inches")

    print(f"\nA4 paper size in pixels ({ppi} PPI):")
    print(f"Width: {width_pixels} pixels")
    print(f"Height: {height_pixels} pixels")
    return (width_pixels, height_pixels)


def getsize_passport_2x2_inch(ppi):
    """Indian Passport Photo
    - Size of photo: 2 x 2 inch, 35 x 45 mm or 35 x 35 mm (5 x 5 cm, 3.5 x 4.5 cm, 3.5 x 3.5 cm).
    - Color of background: white or off-white.
    - The model has to look towards the camera. Tilted head is not allowed.
    - Profile or three quarter photo is not allowed.
    """
    return (
        inches_to_pixels(2, ppi),
        inches_to_pixels(2, ppi),
    )


def getsize_oci_passport_35x35_mm(ppi):
    """Indian OCI (Overseas Citizenship of India).
    - Size of photo: 35x35 mm. (3.5 x 3.5 cm)
    - Two ID photos must be enclosed for OCI application.
    - Color of background: white is not allowed, usually light blue is used.
    """
    return (
        inches_to_pixels(mm_to_inches(35), ppi),
        inches_to_pixels(mm_to_inches(35), ppi),
    )


def getsize_visa_35x45_mm(ppi):
    """Indian Visa Photo
    - Size of photo: 3.5 x 4.5 cm.
    - Color of background: white or light coloured.
    """
    return (
        inches_to_pixels(mm_to_inches(35), ppi),
        inches_to_pixels(mm_to_inches(45), ppi),
    )


def getsize_pan_25x35_mm(ppi):
    """Indian PAN Card Photo
    - Size of photo: 2.5 x 3.5 cm.
    """
    return (
        inches_to_pixels(mm_to_inches(25), ppi),
        inches_to_pixels(mm_to_inches(35), ppi),
    )


def getsize_stamp_20x25_mm(ppi):
    """Indian Stamp Size Photo photo's size
    - Size of Photo: 2 x 2.5 cm.
    """
    return (
        inches_to_pixels(mm_to_inches(20), ppi),
        inches_to_pixels(mm_to_inches(25), ppi),
    )
