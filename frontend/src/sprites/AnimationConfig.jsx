import archerBlueIdle from "../assets/characters/archer/blue/IDLE.png"
import archerBlueAttack from "../assets/characters/archer/blue/ATTACK.png"
import archerBlueHurt from "../assets/characters/archer/blue/HURT.png"
import archerBlueDie from "../assets/characters/archer/blue/DEATH.png"

import warriorRedIdle from "../assets/characters/warrior/red/IDLE.png"
import warriorRedAttack from "../assets/characters/warrior/red/ATTACK1.png"
import warriorRedHurt from "../assets/characters/warrior/red/HURT.png"
import warriorRedDie from "../assets/characters/warrior/red/DEATH.png"

import rogueGreenIdle from "../assets/characters/rogue/green/IDLE.png"
import rogueGreenAttack from "../assets/characters/rogue/green/ATTACK1.png"
import rogueGreenHurt from "../assets/characters/rogue/green/HURT.png"
import rogueGreenDie from "../assets/characters/rogue/green/DEATH.png"

import alchemistPandaIdle from "../assets/characters/alchemist/panda/IDLE.png"
import alchemistPandaAttack from "../assets/characters/alchemist/panda/ATTACK1.png"
import alchemistPandaHurt from "../assets/characters/alchemist/panda/HURT.png"
import alchemistPandaDie from "../assets/characters/alchemist/panda/DEATH.png"

import enemyWolfIdle from "../assets/characters/enemies/wolf/IDLE.png"
import enemyWolfAttack from "../assets/characters/enemies/wolf/ATTACK1.png"
import enemyWolfHurt from "../assets/characters/enemies/wolf/HURT.png"
import enemyWolfDie from "../assets/characters/enemies/wolf/DEATH.png"

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

    warriorRed: {
        idle: {
            image: warriorRedIdle,
            frames: 5,
            frameWidth: 96,
            frameHeight: 64,
            duration: 1,
            loop: true,
        },
        attack: {
            image: warriorRedAttack,
            frames: 5,
            frameWidth: 96,
            frameHeight: 64,
            duration: 0.5,
            loop: false,
        },
        hurt: {
            image: warriorRedHurt,
            frames: 3,
            frameWidth: 96,
            frameHeight: 64,
            duration: 0.3,
            loop: false,
        },
        die: {
            image: warriorRedDie,
            frames: 10,
            frameWidth: 96,
            frameHeight: 64,
            duration: 1,
            loop: false,
        },
    },

    rogueGreen: {
        idle: {
            image: rogueGreenIdle,
            frames: 5,
            frameWidth: 96,
            frameHeight: 64,
            duration: 0.5,
            loop: true,
        },
        attack: {
            image: rogueGreenAttack,
            frames: 6,
            frameWidth: 96,
            frameHeight: 64,
            duration: 0.6,
            loop: false,
        },
        hurt: {
            image: rogueGreenHurt,
            frames: 4,
            frameWidth: 96,
            frameHeight: 64,
            duration: 0.4,
            loop: false,
        },
        die: {
            image: rogueGreenDie,
            frames: 10,
            frameWidth: 96,
            frameHeight: 64,
            duration: 1,
            loop: false,
        },
    },

    alchemistPanda: {
        idle: {
            image: alchemistPandaIdle,
            frames: 8,
            frameWidth: 128,
            frameHeight: 64,
            duration: 0.8,
            loop: true,
        },
        attack: {
            image: alchemistPandaAttack,
            frames: 7,
            frameWidth: 128,
            frameHeight: 64,
            duration: 0.7,
            loop: false,
        },
        hurt: {
            image: alchemistPandaHurt,
            frames: 4,
            frameWidth: 128,
            frameHeight: 64,
            duration: 0.4,
            loop: false,
        },
        die: {
            image: alchemistPandaDie,
            frames: 9,
            frameWidth: 128,
            frameHeight: 64,
            duration: 0.9,
            loop: false,
        },
    },

    enemyWolf: {
        idle: {
            image: enemyWolfIdle,
            frames: 6,
            frameWidth: 192,
            frameHeight: 58,
            duration: 0.6,
            loop: true,
        },
        attack: {
            image: enemyWolfAttack,
            frames: 6,
            frameWidth: 192,
            frameHeight: 58,
            duration: 0.6,
            loop: false,
        },
        hurt: {
            image: enemyWolfHurt,
            frames: 6,
            frameWidth: 192,
            frameHeight: 58,
            duration: 0.6,
            loop: false,
        },
        die: {
            image: enemyWolfDie,
            frames: 8,
            frameWidth: 192,
            frameHeight: 58,
            duration: 0.8,
            loop: false,
        },
    },
}

export default animationConfig