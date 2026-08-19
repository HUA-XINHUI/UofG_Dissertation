import archerBlueIdle from "../assets/characters/archer/blue/IDLE.png"
import archerBlueAttack from "../assets/characters/archer/blue/ATTACK.png"
import archerBlueHurt from "../assets/characters/archer/blue/HURT.png"
import archerBlueDie from "../assets/characters/archer/blue/DEATH.png"

const animationConfig = {

    archerBlue: {
        idle: {
            image: archerBlueIdle,
            frames: 14,
            frameWidth: 96,
            frameHeight: 80,
            duration: 1.4,
            loop: true,
        },
        attack: {
            image: archerBlueAttack,
            frames: 11,
            frameWidth: 96,
            frameHeight: 80,
            duration: 0.55,
            loop: false,
        },
        hurt: {
            image: archerBlueHurt,
            frames: 7,
            frameWidth: 96,
            frameHeight: 80,
            duration: 0.35,
            loop: false,
        },
        die: {
            image: archerBlueDie,
            frames: 11,
            frameWidth: 96,
            frameHeight: 80,
            duration: 0.55,
            loop: false,
        },
    },

}

export default animationConfig