(function(mod) {
    if (typeof exports == "object" && typeof module == "object")
      mod(require("../../lib/codemirror"))
    else if (typeof define == "function" && define.amd)
      define(["../../lib/codemirror"], mod)
    else
      mod(CodeMirror)
  })(function(CodeMirror) {
    "use strict";
    let kw_operators = 'inclib|freelib|addqst|killqst|openqst|opengame|savegame|addobj|delobj|killobj|unsel|unselect|cls|cla|delact|cmdclr|cmdclear|play|close|all|jump|dynamic|goto|gt|xgoto|xgt|gosub|gs|menu|exit|showobjs|showstat|showacts|showinput|refint|copyarr|killvar|killall|view|msg|settimer|wait|exec';
    let kw_controls = 'act|if|elseif|else|loop|while|step|end';
    let kw_text_operators = '\\*(pl?|nl|clr|clear)|(pl?|nl|clr|clear)';
  
    let functions_string = '\\$(desc|user_text|usrtxt|maintxt|stattxt|curloc|selobj|selact|mid|(u|l)case|trim|replace|str|strfind|input|qspver|curacts|getobj|iif|dyneval|func|max|min|arritem)\\b';
    let functions_num = '\\b(loc|obj|isnum|isplay|len|val|instr|strcomp|strpos|arrsize|arrpos|arrcomp|msecscount|rgb|countobj|ra?nd|iif|dyneval|func|max|min|arritem)\\b';
  
    let system_vars_string = '\\$(counter|ongload|ongsave|onnewloc|onactsel|onobjsel|onobjadd|onobjdel|usercom|fname|backimage|args|result)\b';
    let system_vars_num = '\\b(nosave|disablescroll|disablesubex|debug|usehtml|(b|f|l)color|fsize|args|result)\\b';
    CodeMirror.defineSimpleMode("qsp", {
      start: [
        { token: 'start-location', regex: /^\#\s*\S+.*$/im },
        { token: 'end-location', regex: /^\-.*$/im },
        { regex: /\d+/, token: "number" },
        { regex: /((^\s*?)|(\&\s*?))(!.*$)/m, token: "comment" },
        { regex: RegExp(`(?:((${kw_text_operators})\b)|${kw_operators}|${kw_controls})`, 'i'), token: "keyword" },
        { regex: /[<>\+\-\*\/]=|<>|\+|-|<|>|=|\/|\*|!|and|or|mod/i, token: "operator" },
        { regex: RegExp(`(?:(${functions_string}|${functions_num}))`, 'i'), token: "builtin"},
        { regex: /("|')(?:[\s\S]*?)\1/i, token: "string" },
        { token: 'sys-variable', regex: RegExp(`(?:${system_vars_string}|${system_vars_num})`, 'i') },
        { regex: RegExp(`(?:${system_vars_string}|${system_vars_num})`, 'i'), token: 'sys-variable' },
        
  
      ],
      definition: [
        { regex: /(\w+)/, token: "attribute", pop: true }
      ]
    })
  });
  