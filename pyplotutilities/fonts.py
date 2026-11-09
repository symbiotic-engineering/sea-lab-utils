import matplotlib.pyplot as plt


def get_fonts(usetex=True):
    """Use a LaTeX-like serif font style for plots.

    usetex=True renders all text with LaTeX, which needs MiKTeX or TeX Live
    installed. usetex=False uses the Computer Modern fonts and math renderer
    that ship with Matplotlib, so figures look like LaTeX with no TeX install.
    Math like $\\alpha$ still works, but text outside $...$ is not LaTeX, so
    write % rather than \\%.
    """
    if usetex:
        plt.rcParams.update({"font.family": "serif", "text.usetex": True})
    else:
        plt.rcParams.update(
            {
                # cmr10 has no minus sign, so text like a PercentFormatter's
                # tick labels takes it from STIX, and scalar tick labels use
                # mathtext's
                "font.family": ["cmr10", "STIXGeneral"],
                "mathtext.fontset": "cm",
                "axes.formatter.use_mathtext": True,
                # Embed TrueType rather than Type 3 fonts, which some
                # journals reject
                "pdf.fonttype": 42,
                "ps.fonttype": 42,
                "text.usetex": False,
            }
        )
