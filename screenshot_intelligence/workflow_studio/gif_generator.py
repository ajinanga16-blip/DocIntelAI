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

        image = Image.open(screenshot).convert("RGB")

        draw = ImageDraw.Draw(image)

        try:
            font = ImageFont.truetype(
                "arial.ttf",
                32
            )
        except:
            font = ImageFont.load_default()

        draw.rounded_rectangle(

            (20, 20, 220, 70),

            radius=10,

            fill="black"

        )

        draw.text(

            (35, 32),

            f"Step {len(frames)+1}",

            fill="white",

            font=font

        )

        frames.append(image)

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