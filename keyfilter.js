#!/usr/bin/env node

const REPLACE_CONTENT = {
    'USERNAME': 'github.com',
    'PASSWORD': '123456'
}

process.stdin.setEncoding('utf8');

function usage() {
    console.log(`usage:
        1. for git smudge
            keyfilter.js smudge
        2. for git clean
            keyfilter.js clean
    `);
}

function smudge() {
    process.stdin.on('readable', () => {
        let chunk = process.stdin.read();
        if (chunk !== null) {
            for(let key in REPLACE_CONTENT) {
                chunk = chunk.replace(REPLACE_CONTENT[key], key);
            }
            process.stdout.write(`${chunk}`);
        }
    });
}

function clean() {
    process.stdin.on('readable', () => {
        let chunk = process.stdin.read();
        if (chunk !== null) {
            for(let key in REPLACE_CONTENT) {
                chunk = chunk.replace(key, REPLACE_CONTENT[key]);
            }
            process.stdout.write(`${chunk}`);
        }
    });
}

function main() {
    try {
        if (process.argv.length >= 3) {
            switch(process.argv[2]) {
                case 'smudge':
                    smudge();
                    break;
                case 'clean':
                    clean();
                    break;
                default:
                    usage();
            }
        } else {
            usage();
        }
    } catch (error) {
        console.log(error);
        usage();
    }
}

main()
