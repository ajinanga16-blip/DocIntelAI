from PIL import Image
from io import BytesIO


def generate_workflow_gif(
    screenshots,
    duration=2500
):
    """
    Generate an animated GIF
    from uploaded workflow screenshots.
    """

    frames = []

    for screenshot in screenshots:

        from PIL import ImageDraw, ImageFont

        image = Image.open(
            screenshot
        ).convert("RGB")

        draw = ImageDraw.Draw(
            image
        )

        #
        # Small Step Label
        #

        try:

            font = ImageFont.truetype(
                "arial.ttf",
                18
            )

        except:

            font = ImageFont.load_default()

        #
        # Small black rounded box
        #

        draw.rounded_rectangle(

            (
                12,
                12,
                115,
                42
            ),

            radius=6,

            fill="black"

        )

        #
        # Step text
        #

        draw.text(

            (
                22,
                18
            ),

            f"Step {len(frames) + 1}",

            fill="white",

            font=font

        )

        frames.append(
            image
        )

    #
    # Create GIF
    #

    output = BytesIO()

    frames[0].save(

        output,

        format="GIF",

        save_all=True,

        append_images=frames[1:],

        duration=duration,

        loop=0

    )

    output.seek(0)

    return output