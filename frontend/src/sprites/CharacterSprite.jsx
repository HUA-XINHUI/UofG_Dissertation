import animationConfig from "./AnimationConfig"
import "./CharacterSprite.css"


function CharacterSprite({
    character,
    state,
    facing = "right",
    onAnimationEnd,
}) {
    const animation = animationConfig[character][state]
    const sheetWidth =
        animation.frameWidth * animation.frames
    const lastFrameOffset =
        animation.frameWidth * (animation.frames - 1)
    const spriteStyle = {
        backgroundImage: `url(${animation.image})`,
        width: `${animation.frameWidth}px`,
        height: `${animation.frameHeight}px`,

        "--sheet-width": `${sheetWidth}px`,
        "--last-frame-offset": `${lastFrameOffset}px`,

        "--frame-count": animation.frames,
        "--animation-duration": `${animation.duration}s`,
        "--animation-iteration": animation.loop
            ? "infinite"
            : "1",
    }

    function handleAnimationEnd() {
        if (!animation.loop && onAnimationEnd) {
            onAnimationEnd()
        }
    }

    return (
        <div className="sprite-actor">
            <div
                className={`sprite-facing ${facing}`}
            >
                <div
                    key={`${character}-${state}`}
                    className="sprite"
                    style={spriteStyle}
                    onAnimationEnd={handleAnimationEnd}
                />
            </div>
        </div>
    )
}


export default CharacterSprite