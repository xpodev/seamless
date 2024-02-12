class Color(dict):
  # region: Pre-defined colors
  BLACK: 'Color'
  BLUE: 'Color'
  DARK_BLUE: 'Color'
  MIDNIGHT_BLUE: 'Color'
  DARK_SLATE_BLUE: 'Color'
  SLATE_BLUE: 'Color'
  MEDIUM_SLATE_BLUE: 'Color'
  MEDIUM_BLUE: 'Color'
  ROYAL_BLUE: 'Color'
  CORNFLOWER_BLUE: 'Color'
  DODGER_BLUE: 'Color'
  DEEP_SKY_BLUE: 'Color'
  LIGHT_SKY_BLUE: 'Color'
  SKY_BLUE: 'Color'
  LIGHT_BLUE: 'Color'
  STEEL_BLUE: 'Color'
  ALICE_BLUE: 'Color'
  WHITE: 'Color'
  GAINSBORO: 'Color'
  LIGHT_GREY: 'Color'
  SILVER: 'Color'
  DIM_GREY: 'Color'
  GREY: 'Color'
  DARK_GREY: 'Color'
  SLATE_GREY: 'Color'
  LIGHT_SLATE_GREY: 'Color'
  LIGHT_STEEL_BLUE: 'Color'
  YELLOW: 'Color'
  ORANGE: 'Color'
  RED: 'Color'
  BROWN: 'Color'
  WHITE_SMOKE: 'Color'
  GREEN: 'Color'
  DARK_SLATE_GREY: 'Color'
  LAVENDER: 'Color'
  MEDIUM_PURPLE: 'Color'
  VIOLET: 'Color'
  PLUM: 'Color'
  THISTLE: 'Color'
  LAVENDER_BLUSH: 'Color'
  MISTY_ROSE: 'Color'
  ANTIQUE_WHITE: 'Color'
  LINEN: 'Color'
  BEIGE: 'Color'
  PINK: 'Color'
  # endregion

  def __init__(self, r, g, b, a=1):
    self.r = r
    self.g = g
    self.b = b
    self.a = a

  @classmethod
  def from_hex(cls, hex):
    if hex.startswith("#"):
      hex = hex[1:]
    if len(hex) == 3:
      hex = "".join([c*2 for c in hex])
    if len(hex) != 6:
      raise ValueError("Invalid hex color")
    return cls(*[int(hex[i:i+2], 16) for i in range(0, 6, 2)])
  
  @classmethod
  def from_rgb(cls, r, g, b):
    return cls(r, g, b)
  
  @classmethod
  def from_rgba(cls, r, g, b, a):
    return cls(r, g, b, a)
  
  @classmethod
  def from_hsl(cls, h, s, l):
    return cls(*Color.hsl_to_rgb(h, s, l))
  
  @classmethod
  def from_hsla(cls, h, s, l, a):
    return cls(*Color.hsl_to_rgb(h, s, l), a)
  
  def to_hex(self):
    return f"#{self.r:02x}{self.g:02x}{self.b:02x}"
  
  def to_rgb(self):
    return (self.r, self.g, self.b)
  
  def to_rgba(self):
    return (self.r, self.g, self.b, self.a)
  
  def to_hsl(self):
    return Color.rgb_to_hsl(self.r, self.g, self.b)
  
  def to_hsla(self):
    return (*Color.rgb_to_hsl(self.r, self.g, self.b), self.a)
  
  @staticmethod
  def rgb_to_hsl(r, g, b):
    r /= 255
    g /= 255
    b /= 255
    cmax = max(r, g, b)
    cmin = min(r, g, b)
    delta = cmax - cmin
    l = (cmax + cmin) / 2
    if delta == 0:
      h = 0
      s = 0
    else:
      if cmax == r:
        h = ((g - b) / delta) % 6
      elif cmax == g:
        h = (b - r) / delta + 2
      else:
        h = (r - g) / delta + 4
      s = delta / (1 - abs(2*l - 1))
    return (h*60, s, l)
  
  @staticmethod
  def hsl_to_rgb(h, s, l):
    c = (1 - abs(2*l - 1)) * s
    x = c * (1 - abs((h / 60) % 2 - 1))
    m = l - c/2
    if h < 60:
      r, g, b = c, x, 0
    elif h < 120:
      r, g, b = x, c, 0
    elif h < 180:
      r, g, b = 0, c, x
    elif h < 240:
      r, g, b = 0, x, c
    elif h < 300:
      r, g, b = x, 0, c
    else:
      r, g, b = c, 0, x
    return (int((r+m)*255), int((g+m)*255), int((b+m)*255))
  
  def __str__(self):
    return self.to_hex()

Color.BLACK = Color.from_hex("#000000")
Color.BLUE = Color.from_hex("#0000ff")
Color.DARK_BLUE = Color.from_hex("#00008b")
Color.MIDNIGHT_BLUE = Color.from_hex("#191970")
Color.DARK_SLATE_BLUE = Color.from_hex("#483d8b")
Color.SLATE_BLUE = Color.from_hex("#6a5acd")
Color.MEDIUM_SLATE_BLUE = Color.from_hex("#7b68ee")
Color.MEDIUM_BLUE = Color.from_hex("#0000cd")
Color.ROYAL_BLUE = Color.from_hex("#4169e1")
Color.CORNFLOWER_BLUE = Color.from_hex("#6495ed")
Color.DODGER_BLUE = Color.from_hex("#1e90ff")
Color.DEEP_SKY_BLUE = Color.from_hex("#00bfff")
Color.LIGHT_SKY_BLUE = Color.from_hex("#87cefa")
Color.SKY_BLUE = Color.from_hex("#87ceeb")
Color.LIGHT_BLUE = Color.from_hex("#add8e6")
Color.STEEL_BLUE = Color.from_hex("#4682b4")
Color.ALICE_BLUE = Color.from_hex("#f0f8ff")
Color.WHITE = Color.from_hex("#ffffff")
Color.GAINSBORO = Color.from_hex("#dcdcdc")
Color.LIGHT_GREY = Color.from_hex("#d3d3d3")
Color.SILVER = Color.from_hex("#c0c0c0")
Color.DIM_GREY = Color.from_hex("#696969")
Color.GREY = Color.from_hex("#808080")
Color.DARK_GREY = Color.from_hex("#a9a9a9")
Color.SLATE_GREY = Color.from_hex("#708090")
Color.LIGHT_SLATE_GREY = Color.from_hex("#778899")
Color.LIGHT_STEEL_BLUE = Color.from_hex("#b0c4de")
Color.YELLOW = Color.from_hex("#ffff00")
Color.ORANGE = Color.from_hex("#ffa500")
Color.RED = Color.from_hex("#ff0000")
Color.BROWN = Color.from_hex("#a52a2a")
Color.WHITE_SMOKE = Color.from_hex("#f5f5f5")
Color.GREEN = Color.from_hex("#00ff00")
Color.DARK_SLATE_GREY = Color.from_hex("#2f4f4f")
Color.LAVENDER = Color.from_hex("#e6e6fa")
Color.MEDIUM_PURPLE = Color.from_hex("#9370db")
Color.VIOLET = Color.from_hex("#ee82ee")
Color.PLUM = Color.from_hex("#dda0dd")
Color.THISTLE = Color.from_hex("#d8bfd8")
Color.LAVENDER_BLUSH = Color.from_hex("#fff0f5")
Color.MISTY_ROSE = Color.from_hex("#ffe4e1")
Color.ANTIQUE_WHITE = Color.from_hex("#faebd7")
Color.LINEN = Color.from_hex("#faf0e6")
Color.BEIGE = Color.from_hex("#f5f5dc")
Color.PINK = Color.from_hex("#ffc0cb")

