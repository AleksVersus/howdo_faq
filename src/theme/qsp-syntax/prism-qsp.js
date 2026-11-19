const statements = [
    'play', 'close', 'view', 'exit', 'jump',
    'gosub', 'gs', 'goto', 'gt', 'xgoto', 'xgt',
    'pl', 'p', 'nl', 'clear', 'clr',
    '\\*pl', '\\*p', '\\*nl', '\\*clear', '\\*clr',
    'msg', 'wait', 'addobj', 'delobj', 'modobj', 'resetobj', 'killobj',
    'unselect', 'unsel', 'killall', 'cla', 'delact', 'cls',
    'cmdclear', 'cmdclr', 'menu', 'settimer', 'dynamic',
    'setvar', 'insvar', 'killvar', 'copyarr', 'movearr', 'sortarr', 'scanstr', 'unpackarr',
    'opengame', 'savegame', 'openqst', 'inclib', 'freelib', 'refint',
    'showacts', 'showinput', 'showobjs', 'showstat',
].join('|')

const controls = 'act|if|elseif|else|loop|while|step|end'

const functions = [
    'desc', 'max', 'min', 'rand', 'rnd', 'val', 'iif', 'dyneval', 'func',
    'input', 'usrtxt', 'user_text', 'maintxt', 'stattxt',
    'getobj', 'countobj', 'selobj', 'curloc', 'curobjs', 'selact', 'curacts',
    'arrsize', 'arrtype', 'arrkey', 'arritem', 'arrpack', 'arrpos', 'arrcomp',
    'strcomp', 'strfind', 'strpos', 'instr', 'isnum',
    'trim', 'ucase', 'lcase', 'len', 'mid', 'replace', 'str',
    'isplay', 'rgb', 'msecscount', 'qspver',
].join('|')

const system_vars = [
    'counter', 'ongload', 'ongsave', 'onnewloc', 'onactsel', 'onobjsel', 'onobjadd', 'onobjdel',
    'usercom', 'fname', 'backimage', 'args', 'result',
    'nosave', 'disablescroll', 'disablesubex', 'debug', 'usehtml',
    'bcolor', 'fcolor', 'lcolor', 'fsize',
].join('|')

const delimiter_chars = "\\s&'\"(){}\\[\\],:=!<>+\\-/*\\\\;^@?"
const name_char = `[^${delimiter_chars}.]`
const name_start = `[^${delimiter_chars}.0-9#$%]`
const type_prefix = '[#$%]'
const named_token = (pattern) => ({
    pattern: RegExp(`(^|[${delimiter_chars}.])(?:${pattern})(?!${name_char})`, 'i'),
    lookbehind: true,
})

const interpolated_string = (quote) => {
    const inner_quote = quote === '"' ? "'" : '"'
    const literal = `${inner_quote}(?:[^${inner_quote}]|${inner_quote}${inner_quote})*${inner_quote}(?!${inner_quote})`

    return {
        pattern: RegExp(`${quote}(?:[^${quote}]|${quote}${quote})*${quote}`),
        greedy: true,
        inside: {
            interpolation: {
                pattern: RegExp(`<<(?:(?!>>)[^"']|${literal})*>>`),
                greedy: true,
                inside: {
                    'interpolation-punctuation': {
                        pattern: /^<<|>>$/,
                        alias: 'punctuation',
                    },
                },
            },
        },
    }
}

Prism.languages.qsp = {
    'comment': {
        pattern: /((^\s*?)|(\&\s*?)|(\:\s*?))(![^\n{'"]*$)/m,
        lookbehind: true,
        greedy: true,
    },
    'braced-comment': {
        pattern: /((^\s*?)|(\&\s*?)|(\:\s*?))(![^\n{'"]*\{[^\}]*\}.*?$)/m,
        alias: 'comment',
        lookbehind: true,
        greedy: true,
    },
    'quoted-comment': {
        pattern: /((^\s*?)|(\&\s*?)|(\:\s*?))((![^\n{'"]*"[^"]*".*?$)|(![^'\n\r]*'[^']*?'.*?$))/m,
        alias: 'comment',
        lookbehind: true,
        greedy: true,
    },
    'string': [interpolated_string('"'), interpolated_string("'")],
    'function': {
        pattern: RegExp(`(^|[${delimiter_chars}.])(@@?\\s*[^${delimiter_chars}]+)`, 'i'),
        lookbehind: true,
        greedy: true,
    },
    'start-location': /^[ \t]*#[ \t]+\S.*$/m,
    'end-location': /^[ \t]*--.*$/m,
    'label': {
        pattern: /^\s*:[^&\n]*(?=\&|$)/im,
        lookbehind: true,
        greedy: true,
    },
    'sys-variable': named_token(`${type_prefix}?(?:${system_vars})`),
    'builtin': named_token(`${type_prefix}?(?:${functions})`),
    'number': [named_token('\\d+'), /\?/],
    'keyword': [
        named_token('else\\s+if'),
        named_token(`${controls}|${statements}`),
    ],
    'declarator': named_token('alias|local|set|let'),
    'operator': [
        /<=|>=|<>|=<|=>|\+=|-=|\*=|\/=|[+\-*/=<>!&]/,
        named_token('and|or|mod|no|obj|loc'),
    ],
    'sign-punctuation': /[{}[\]();,:.]/,
    'user-variable': named_token(`${type_prefix}?${name_start}${name_char}*`),
};

const interpolation_tokens = { ...Prism.languages.qsp }
for (const token of ['comment', 'braced-comment', 'quoted-comment', 'start-location', 'end-location', 'label']) {
    delete interpolation_tokens[token]
}
for (const string of Prism.languages.qsp.string) {
    string.inside.interpolation.inside.rest = interpolation_tokens
}