const assert = require('node:assert/strict')
const {test} = require('node:test')
const Prism = require('prismjs')

globalThis.Prism = Prism
require('./prism-qsp.js')

const highlight = (code) => Prism.highlight(code, Prism.languages.qsp, 'qsp')

test('tokenizes QSP expressions inside interpolated strings', () => {
    const html = highlight(`msg "<<len('x') + #args[0] + $name>>"`)

    assert.ok(html.includes('<span class="token interpolation-punctuation punctuation">&lt;&lt;</span>'))
    assert.ok(html.includes('<span class="token builtin">len</span>'))
    assert.ok(html.includes('<span class="token sys-variable">#args</span>'))
    assert.ok(html.includes('<span class="token number">0</span>'))
    assert.ok(html.includes('<span class="token user-variable">$name</span>'))
})

test('does not close interpolation on >> inside a quoted literal', () => {
    const html = highlight(`msg "<<len('a''>>b') + #args[0]>>"`)

    assert.equal((html.match(/class="token interpolation"/g) || []).length, 1)
    assert.equal((html.match(/class="token interpolation-punctuation punctuation"/g) || []).length, 2)
    assert.ok(html.includes('<span class="token builtin">len</span>'))
    assert.ok(html.includes('<span class="token sys-variable">#args</span>'))
})

test('keeps comments and labels in their statement contexts', () => {
    const html = highlight('msg 0 & :retry & ! ignored\nmsg 1')

    assert.ok(html.includes('<span class="token label">retry </span>'))
    assert.ok(html.includes('<span class="token comment">! ignored\n</span>'))
    assert.ok(html.includes('<span class="token keyword">msg</span>'))
    assert.ok(!html.includes('qspregionplaceholder'))
})

test('highlights notes after END without consuming the next statement', () => {
    const html = highlight('end note & *pl "run"')

    assert.ok(html.includes('<span class="token keyword">end</span>'))
    assert.ok(html.includes('<span class="token comment">note </span>'))
    assert.ok(html.includes('<span class="token keyword">*pl</span>'))
})

test('distinguishes location markers from typed variables and leaves brackets ordinary', () => {
    const html = highlight('# room\n#counter = 1\n-- room\nmsg #args[0]')

    assert.ok(html.includes('<span class="token start-location"># room</span>'))
    assert.ok(html.includes('<span class="token sys-variable">#counter</span>'))
    assert.ok(html.includes('<span class="token end-location">-- room</span>'))
    assert.ok(html.includes('<span class="token sign-punctuation">[</span>'))
    assert.ok(html.includes('<span class="token number">0</span>'))
    assert.ok(!html.includes('token tuple'))
})

test('keeps @ and @@ calls distinct from built-in function tokens', () => {
    const html = highlight('@foo(1) & @@ bar')

    assert.ok(html.includes('<span class="token user-call function">@foo</span>'))
    assert.ok(html.includes('<span class="token user-call function">@@ bar</span>'))
})
