"""
The `analysis` package offers comprehensive tools for investment and startup analysis. It includes modules for investor analysis, startup evaluation, and overall market performance assessment.

Modules:
- `investor`: Analyzes investor data, including profiles and investment patterns.
- `startup`: Evaluates startups, focusing on financial health and growth potential.
- `overall`: Provides a holistic analysis of the market by combining investor and startup data.

Usage:
To leverage this package, import the required modules as shown below:

from analysis.investor import Investor
from analysis.startup import Startup
from analysis.overall import Overall

Refer to individual module docstrings for detailed usage instructions.
"""

from .investor import Investor
from .startup import Startup
from .overall import Overall
