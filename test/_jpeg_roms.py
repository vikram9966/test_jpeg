
# luminance table
rom_lum = \
[
    # 100% @ 0x00
    0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 
    0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 
    0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 
    0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 
    0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 
    0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 
    0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 
    0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 

    # 50% @ 0x40 (64)
    0x05, 0x03, 0x04, 0x04, 0x04, 0x03, 0x05, 0x04, 
    0x04, 0x04, 0x05, 0x05, 0x05, 0x06, 0x07, 0x0C,
    0x08, 0x07, 0x07, 0x07, 0x07, 0x0F, 0x0B, 0x0B, 
    0x09, 0x0C, 0x11, 0x0F, 0x12, 0x12, 0x11, 0x0F,
    0x11, 0x11, 0x13, 0x16, 0x1C, 0x17, 0x13, 0x14, 
    0x1A, 0x15, 0x11, 0x11, 0x18, 0x21, 0x18, 0x1A,
    0x1D, 0x1D, 0x1F, 0x1F, 0x1F, 0x13, 0x17, 0x22, 
    0x24, 0x22, 0x1E, 0x24, 0x1C, 0x1E, 0x1F, 0x1E,

    # 75% @ 0x80 (128)
    0x08, 0x06, 0x06, 0x07, 0x06, 0x05, 0x08, 0x07, 
    0x07, 0x07, 0x09, 0x09, 0x08, 0x0A, 0x0C, 0x14,
    0x0D, 0x0C, 0x0B, 0x0B, 0x0C, 0x19, 0x12, 0x13, 
    0x0F, 0x14, 0x1D, 0x1A, 0x1F, 0x1E, 0x1D, 0x1A,
    0x1C, 0x1C, 0x20, 0x24, 0x2E, 0x27, 0x20, 0x22, 
    0x2C, 0x23, 0x1C, 0x1C, 0x28, 0x37, 0x29, 0x2C,
    0x30, 0x31, 0x34, 0x34, 0x34, 0x1F, 0x27, 0x39, 
    0x3D, 0x38, 0x32, 0x3C, 0x2E, 0x33, 0x34, 0x32,   
    
    # 50% @ 0xC0 (192)
    0x10, 0x0B, 0x0C, 0x0E, 0x0C, 0x0A, 0x10, 0x0E, 
    0x0D, 0x0E, 0x12, 0x11, 0x10, 0x13, 0x18, 0x28,
    0x1A, 0x18, 0x16, 0x16, 0x18, 0x31, 0x23, 0x25, 
    0x1D, 0x28, 0x3A, 0x33, 0x3D, 0x3C, 0x39, 0x33,
    0x38, 0x37, 0x40, 0x48, 0x5C, 0x4E, 0x40, 0x44, 
    0x57, 0x45, 0x37, 0x38, 0x50, 0x6D, 0x51, 0x57,
    0x5F, 0x62, 0x67, 0x68, 0x67, 0x3E, 0x4D, 0x71, 
    0x79, 0x70, 0x64, 0x78, 0x5C, 0x65, 0x67, 0x63
]


# chrominance table
rom_chr = \
[
    # 100%  @ 0x00
    0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 
    0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 
    0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 
    0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 
    0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 
    0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 
    0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 
    0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 

    # 85%  @ 0x40
    0x08, 0x06, 0x06, 0x07, 0x06, 0x05, 0x08, 0x07, 
    0x07, 0x07, 0x09, 0x09, 0x08, 0x0A, 0x0C, 0x14,
    0x0D, 0x0C, 0x0B, 0x0B, 0x0C, 0x19, 0x12, 0x13, 
    0x0F, 0x14, 0x1D, 0x1A, 0x1F, 0x1E, 0x1D, 0x1A,
    0x1C, 0x1C, 0x20, 0x24, 0x2E, 0x27, 0x20, 0x22, 
    0x2C, 0x23, 0x1C, 0x1C, 0x28, 0x37, 0x29, 0x2C,
    0x30, 0x31, 0x34, 0x34, 0x34, 0x1F, 0x27, 0x39, 
    0x3D, 0x38, 0x32, 0x3C, 0x2E, 0x33, 0x34, 0x32,

    # 75%  @ 0x80
    0x09, 0x09, 0x09, 0x0C, 0x0B, 0x0C, 0x18, 0x0D, 
    0x0D, 0x18, 0x32, 0x21, 0x1C, 0x21, 0x32, 0x32, 
    0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 
    0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 
    0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 
    0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 
    0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 
    0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32,
                                     
    # 50%  @ 0xC0                        
    0x11, 0x12, 0x12, 0x18, 0x15, 0x18, 0x2F, 0x1A, 
    0x1A, 0x2F, 0x63, 0x42, 0x38, 0x42, 0x63, 0x63,
    0x63, 0x63, 0x63, 0x63, 0x63, 0x63, 0x63, 0x63, 
    0x63, 0x63, 0x63, 0x63, 0x63, 0x63, 0x63, 0x63,
    0x63, 0x63, 0x63, 0x63, 0x63, 0x63, 0x63, 0x63, 
    0x63, 0x63, 0x63, 0x63, 0x63, 0x63, 0x63, 0x63,
    0x63, 0x63, 0x63, 0x63, 0x63, 0x63, 0x63, 0x63, 
    0x63, 0x63, 0x63, 0x63, 0x63, 0x63, 0x63, 0x63
]

