"use strict";(self.webpackChunkhowdo_faq=self.webpackChunkhowdo_faq||[]).push([[3081],{7362:(n,r,S)=>{S.r(r),S.d(r,{assets:()=>i,contentTitle:()=>_,default:()=>o,frontMatter:()=>t,metadata:()=>P,toc:()=>Q});var e=S(4848),a=S(8453);const t={sidebar_position:1},_="\u041f\u0440\u043e\u0441\u0442\u043e\u0439 \u043a\u043e\u043d\u0441\u043e\u043b\u044c\u043d\u044b\u0439 QSP-\u043f\u043b\u0435\u0435\u0440",P={id:"informarch/extrqsp/console_player",title:"\u041f\u0440\u043e\u0441\u0442\u043e\u0439 \u043a\u043e\u043d\u0441\u043e\u043b\u044c\u043d\u044b\u0439 QSP-\u043f\u043b\u0435\u0435\u0440",description:"qsp.h.txt",source:"@site/docs/informarch/extrqsp/console_player.md",sourceDirName:"informarch/extrqsp",slug:"/informarch/extrqsp/console_player",permalink:"/howdo_faq/docs/informarch/extrqsp/console_player",draft:!1,unlisted:!1,tags:[],version:"current",sidebarPosition:1,frontMatter:{sidebar_position:1},sidebar:"informArchSidebar",previous:{title:"\u041a\u0430\u043a \u0441\u0434\u0435\u043b\u0430\u0442\u044c StandAlone-\u0441\u0431\u043e\u0440\u043a\u0443 \u043d\u0430 \u043a\u043b\u0430\u0441\u0441\u0438\u0447\u0435\u0441\u043a\u043e\u043c \u043f\u043b\u0435\u0435\u0440\u0435?",permalink:"/howdo_faq/docs/informarch/general/standalone_classic"},next:{title:"\u0410\u0432\u0442\u043e\u043c\u0430\u0442\u043d\u043e\u0435 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0432 QSP",permalink:"/howdo_faq/docs/informarch/extrqsp/automat_programming/"}},i={},Q=[{value:"qsp.h.txt",id:"qsphtxt",level:3}];function s(n){const r={code:"code",h1:"h1",h3:"h3",p:"p",pre:"pre",strong:"strong",...(0,a.R)(),...n.components};return(0,e.jsxs)(e.Fragment,{children:[(0,e.jsx)(r.h1,{id:"\u043f\u0440\u043e\u0441\u0442\u043e\u0439-\u043a\u043e\u043d\u0441\u043e\u043b\u044c\u043d\u044b\u0439-qsp-\u043f\u043b\u0435\u0435\u0440",children:"\u041f\u0440\u043e\u0441\u0442\u043e\u0439 \u043a\u043e\u043d\u0441\u043e\u043b\u044c\u043d\u044b\u0439 QSP-\u043f\u043b\u0435\u0435\u0440"}),"\n",(0,e.jsx)(r.pre,{children:(0,e.jsx)(r.code,{className:"language-js",children:'/* Copyright (C) 2005-2010 Valeriy Argunov (nporep AT mail DOT ru) */\r\n\r\n#include "qsp.h"\r\n#include <stdio.h>\r\n#include <stdlib.h>\r\n#include <string.h>\r\n\r\nvoid refresh_int(QSP_BOOL isRedraw)\r\n{\r\n    long i;\r\n    QSP_CHAR *strVal, *imgPath;\r\n    const QSP_CHAR *mainDesc = QSPGetMainDesc();\r\n    const QSP_CHAR *varsDesc = QSPGetVarsDesc();\r\n    // -------------------------------\r\n    if (QSPIsMainDescChanged()) printf("%s\\n", mainDesc);\r\n    if (QSPIsVarsDescChanged()) printf("%s\\n", varsDesc);\r\n    if (QSPIsActionsChanged())\r\n    {\r\n        long actionsCount = QSPGetActionsCount();\r\n        for (i = 0; i < actionsCount; ++i)\r\n        {\r\n            QSPGetActionData(i, &imgPath, &strVal);\r\n            printf("%d. %s\\n", i + 1, strVal);\r\n        }\r\n    }\r\n}\r\n\r\nvoid msg(const QSP_CHAR *str)\r\n{\r\n    printf("%s\\n", str);\r\n}\r\n\r\nvoid init_callbacks()\r\n{\r\n    QSPSetCallBack(QSP_CALL_REFRESHINT, (QSP_CALLBACK)&refresh_int);\r\n    QSPSetCallBack(QSP_CALL_SHOWMSGSTR, (QSP_CALLBACK)&msg);\r\n}\r\n\r\nint main()\r\n{\r\n    QSPInit();\r\n    char str[1000];\r\n\r\n    init_callbacks();\r\n\r\n    QSPLoadGameWorld((const char *)"chukcha.gam");\r\n    QSPRestartGame(QSP_TRUE);\r\n\r\n    while (1)\r\n    {\r\n        scanf("%s", str);\r\n        if (!strcmp(str, "quit"))\r\n            break;\r\n        int ind = atoi(str) - 1;\r\n        if (ind >= 0 && ind < QSPGetActionsCount())\r\n        {\r\n            QSPSetSelActionIndex(ind, QSP_FALSE);\r\n            QSPExecuteSelActionCode(QSP_TRUE);\r\n        }\r\n    }\r\n\r\n    QSPDeInit();\r\n    return 0;\r\n}\n'})}),"\n",(0,e.jsx)(r.h3,{id:"qsphtxt",children:"qsp.h.txt"}),"\n",(0,e.jsx)(r.pre,{children:(0,e.jsx)(r.code,{className:"language-js",children:'\r\n/* Copyright (C) 2005-2010 Valeriy Argunov (nporep AT mail DOT ru) */\r\n/*\r\n* This library is free software; you can redistribute it and/or modify\r\n* it under the terms of the GNU Lesser General Public License as published by\r\n* the Free Software Foundation; either version 2.1 of the License, or\r\n* (at your option) any later version.\r\n*\r\n* This library is distributed in the hope that it will be useful,\r\n* but WITHOUT ANY WARRANTY; without even the implied warranty of\r\n* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the\r\n* GNU Lesser General Public License for more details.\r\n*\r\n* You should have received a copy of the GNU Lesser General Public License\r\n* along with this library; if not, write to the Free Software\r\n* Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.\r\n*/\r\n\r\n#ifndef QSP_H\r\n    #define QSP_H\r\n\r\n    #ifdef _FLASH\r\n        #include <AS3.h>\r\n    #endif\r\n\r\n    #ifdef EXPORT\r\n        #ifdef _WIN\r\n            #define QSP_EXTERN __declspec(dllexport)\r\n        #else\r\n            #define QSP_EXTERN extern\r\n        #endif\r\n    #else\r\n        #define QSP_EXTERN\r\n    #endif\r\n\r\n    enum\r\n    {\r\n        QSP_ERR_DIVBYZERO = 100,\r\n        QSP_ERR_TYPEMISMATCH,\r\n        QSP_ERR_STACKOVERFLOW,\r\n        QSP_ERR_TOOMANYITEMS,\r\n        QSP_ERR_FILENOTFOUND,\r\n        QSP_ERR_CANTLOADFILE,\r\n        QSP_ERR_GAMENOTLOADED,\r\n        QSP_ERR_COLONNOTFOUND,\r\n        QSP_ERR_CANTINCFILE,\r\n        QSP_ERR_CANTADDACTION,\r\n        QSP_ERR_EQNOTFOUND,\r\n        QSP_ERR_LOCNOTFOUND,\r\n        QSP_ERR_ENDNOTFOUND,\r\n        QSP_ERR_LABELNOTFOUND,\r\n        QSP_ERR_NOTCORRECTNAME,\r\n        QSP_ERR_QUOTNOTFOUND,\r\n        QSP_ERR_BRACKNOTFOUND,\r\n        QSP_ERR_BRACKSNOTFOUND,\r\n        QSP_ERR_SYNTAX,\r\n        QSP_ERR_UNKNOWNACTION,\r\n        QSP_ERR_ARGSCOUNT,\r\n        QSP_ERR_CANTADDOBJECT,\r\n        QSP_ERR_CANTADDMENUITEM,\r\n        QSP_ERR_TOOMANYVARS,\r\n        QSP_ERR_INCORRECTREGEXP,\r\n        QSP_ERR_CODENOTFOUND\r\n    };\r\n\r\n    enum\r\n    {\r\n        QSP_WIN_ACTS,\r\n        QSP_WIN_OBJS,\r\n        QSP_WIN_VARS,\r\n        QSP_WIN_INPUT\r\n    };\r\n\r\n    enum\r\n    {\r\n        QSP_CALL_DEBUG, /* void func(const QSP_CHAR *str) */\r\n        QSP_CALL_ISPLAYINGFILE, /* QSP_BOOL func(const QSP_CHAR *file) */\r\n        QSP_CALL_PLAYFILE, /* void func(const QSP_CHAR *file, int volume) */\r\n        QSP_CALL_CLOSEFILE, /* void func(const QSP_CHAR *file) */\r\n        QSP_CALL_SHOWIMAGE, /* void func(const QSP_CHAR *file) */\r\n        QSP_CALL_SHOWWINDOW, /* void func(int type, QSP_BOOL isShow) */\r\n        QSP_CALL_DELETEMENU, /* void func() */\r\n        QSP_CALL_ADDMENUITEM, /* void func(const QSP_CHAR *name, const QSP_CHAR *imgPath) */\r\n        QSP_CALL_SHOWMENU, /* void func() */\r\n        QSP_CALL_SHOWMSGSTR, /* void func(const QSP_CHAR *str) */\r\n        QSP_CALL_REFRESHINT, /* void func(QSP_BOOL isRedraw) */\r\n        QSP_CALL_SETTIMER, /* void func(int msecs) */\r\n        QSP_CALL_SETINPUTSTRTEXT, /* void func(const QSP_CHAR *text) */\r\n        QSP_CALL_SYSTEM, /* void func(const QSP_CHAR *str) */\r\n        QSP_CALL_OPENGAMESTATUS, /* void func(const QSP_CHAR *file) */\r\n        QSP_CALL_SAVEGAMESTATUS, /* void func(const QSP_CHAR *file) */\r\n        QSP_CALL_SLEEP, /* void func(int msecs) */\r\n        QSP_CALL_GETMSCOUNT, /* int func() */\r\n        QSP_CALL_INPUTBOX, /* void func(const QSP_CHAR *text, QSP_CHAR *buffer, int maxLen) */\r\n        QSP_CALL_DUMMY\r\n    };\r\n\r\n    #ifdef _UNICODE\r\n        #ifndef _FLASH\r\n            typedef wchar_t QSP_CHAR;\r\n        #else\r\n            typedef unsigned short QSP_CHAR;\r\n        #endif\r\n        #define QSP_FMT2(x) L##x\r\n        #define QSP_FMT(x) QSP_FMT2(x)\r\n    #else\r\n        typedef char QSP_CHAR;\r\n        #define QSP_FMT(x) x\r\n    #endif\r\n\r\n    typedef int QSP_BOOL;\r\n\r\n    #define QSP_TRUE 1\r\n    #define QSP_FALSE 0\r\n\r\n    #ifndef _FLASH\r\n        #ifdef __cplusplus\r\n            typedef int (*QSP_CALLBACK)(...);\r\n        #else\r\n            typedef int (*QSP_CALLBACK)();\r\n        #endif\r\n    #else\r\n        typedef struct\r\n        {\r\n            QSP_BOOL IsSet;\r\n            AS3_Val ThisVal;\r\n            AS3_Val FuncVal;\r\n        } QSP_CALLBACK;\r\n    #endif\r\n\r\n    #ifdef __cplusplus\r\n    extern "C"\r\n    {\r\n    #endif\r\n\r\n    #ifndef _FLASH\r\n\r\n        QSP_EXTERN QSP_BOOL QSPIsInCallBack();\r\n        QSP_EXTERN void QSPEnableDebugMode(QSP_BOOL isDebug);\r\n        QSP_EXTERN void QSPGetCurStateData(QSP_CHAR **loc, int *actIndex, int *line);\r\n        QSP_EXTERN const QSP_CHAR *QSPGetVersion();\r\n        QSP_EXTERN const QSP_CHAR *QSPGetCompiledDateTime();\r\n        QSP_EXTERN int QSPGetFullRefreshCount();\r\n        QSP_EXTERN const QSP_CHAR *QSPGetQstFullPath();\r\n        QSP_EXTERN const QSP_CHAR *QSPGetCurLoc();\r\n        QSP_EXTERN const QSP_CHAR *QSPGetMainDesc();\r\n        QSP_EXTERN QSP_BOOL QSPIsMainDescChanged();\r\n        QSP_EXTERN const QSP_CHAR *QSPGetVarsDesc();\r\n        QSP_EXTERN QSP_BOOL QSPIsVarsDescChanged();\r\n        QSP_EXTERN QSP_BOOL QSPGetExprValue(const QSP_CHAR *str, QSP_BOOL *isString, int *numVal, QSP_CHAR *strVal, int strValBufSize);\r\n        QSP_EXTERN void QSPSetInputStrText(const QSP_CHAR *str);\r\n        QSP_EXTERN int QSPGetActionsCount();\r\n        QSP_EXTERN void QSPGetActionData(int ind, QSP_CHAR **imgPath, QSP_CHAR **desc);\r\n        QSP_EXTERN QSP_BOOL QSPExecuteSelActionCode(QSP_BOOL isRefresh);\r\n        QSP_EXTERN QSP_BOOL QSPSetSelActionIndex(int ind, QSP_BOOL isRefresh);\r\n        QSP_EXTERN int QSPGetSelActionIndex();\r\n        QSP_EXTERN QSP_BOOL QSPIsActionsChanged();\r\n        QSP_EXTERN int QSPGetObjectsCount();\r\n        QSP_EXTERN void QSPGetObjectData(int ind, QSP_CHAR **imgPath, QSP_CHAR **desc);\r\n        QSP_EXTERN QSP_BOOL QSPSetSelObjectIndex(int ind, QSP_BOOL isRefresh);\r\n        QSP_EXTERN int QSPGetSelObjectIndex();\r\n        QSP_EXTERN QSP_BOOL QSPIsObjectsChanged();\r\n        QSP_EXTERN void QSPShowWindow(int type, QSP_BOOL isShow);\r\n        QSP_EXTERN QSP_BOOL QSPGetVarValuesCount(const QSP_CHAR *name, int *count);\r\n        QSP_EXTERN QSP_BOOL QSPGetVarValues(const QSP_CHAR *name, int ind, int *numVal, QSP_CHAR **strVal);\r\n        QSP_EXTERN int QSPGetMaxVarsCount();\r\n        QSP_EXTERN QSP_BOOL QSPGetVarNameByIndex(int ind, QSP_CHAR **name);\r\n        QSP_EXTERN QSP_BOOL QSPExecString(const QSP_CHAR *str, QSP_BOOL isRefresh);\r\n        QSP_EXTERN QSP_BOOL QSPExecCounter(QSP_BOOL isRefresh);\r\n        QSP_EXTERN QSP_BOOL QSPExecUserInput(QSP_BOOL isRefresh);\r\n        QSP_EXTERN QSP_BOOL QSPExecLocationCode(const QSP_CHAR *name, QSP_BOOL isRefresh);\r\n        QSP_EXTERN void QSPGetLastErrorData(int *errorNum, QSP_CHAR **errorLoc, int *errorActIndex, int *errorLine);\r\n        QSP_EXTERN const QSP_CHAR *QSPGetErrorDesc(int errorNum);\r\n        QSP_EXTERN QSP_BOOL QSPLoadGameWorld(const QSP_CHAR *file);\r\n        QSP_EXTERN QSP_BOOL QSPLoadGameWorldFromData(const char *data, int dataSize, const QSP_CHAR *file);\r\n        QSP_EXTERN QSP_BOOL QSPSaveGame(const QSP_CHAR *file, QSP_BOOL isRefresh);\r\n        QSP_EXTERN QSP_BOOL QSPSaveGameAsString(QSP_CHAR *strBuf, int strBufSize, int *realSize, QSP_BOOL isRefresh);\r\n        QSP_EXTERN QSP_BOOL QSPOpenSavedGame(const QSP_CHAR *file, QSP_BOOL isRefresh);\r\n        QSP_EXTERN QSP_BOOL QSPOpenSavedGameFromString(const QSP_CHAR *str, QSP_BOOL isRefresh);\r\n        QSP_EXTERN QSP_BOOL QSPRestartGame(QSP_BOOL isRefresh);\r\n        QSP_EXTERN void QSPSelectMenuItem(int ind);\r\n        QSP_EXTERN void QSPSetCallBack(int type, QSP_CALLBACK func);\r\n        QSP_EXTERN void QSPInit();\r\n        QSP_EXTERN void QSPDeInit();\r\n\r\n    #else\r\n\r\n        QSP_EXTERN AS3_Val QSPIsInCallBack(void *param, AS3_Val args);\r\n        QSP_EXTERN AS3_Val QSPEnableDebugMode(void *param, AS3_Val args);\r\n        QSP_EXTERN AS3_Val QSPGetCurStateData(void *param, AS3_Val args);\r\n        QSP_EXTERN AS3_Val QSPGetVersion(void *param, AS3_Val args);\r\n        QSP_EXTERN AS3_Val QSPGetCompiledDateTime(void *param, AS3_Val args);\r\n        QSP_EXTERN AS3_Val QSPGetFullRefreshCount(void *param, AS3_Val args);\r\n        QSP_EXTERN AS3_Val QSPGetQstFullPath(void *param, AS3_Val args);\r\n        QSP_EXTERN AS3_Val QSPGetCurLoc(void *param, AS3_Val args);\r\n        QSP_EXTERN AS3_Val QSPGetMainDesc(void *param, AS3_Val args);\r\n        QSP_EXTERN AS3_Val QSPIsMainDescChanged(void *param, AS3_Val args);\r\n        QSP_EXTERN AS3_Val QSPGetVarsDesc(void *param, AS3_Val args);\r\n        QSP_EXTERN AS3_Val QSPIsVarsDescChanged(void *param, AS3_Val args);\r\n        QSP_EXTERN AS3_Val QSPGetExprValue(void *param, AS3_Val args);\r\n        QSP_EXTERN AS3_Val QSPSetInputStrText(void *param, AS3_Val args);\r\n        QSP_EXTERN AS3_Val QSPGetActionsCount(void *param, AS3_Val args);\r\n        QSP_EXTERN AS3_Val QSPGetActionData(void *param, AS3_Val args);\r\n        QSP_EXTERN AS3_Val QSPExecuteSelActionCode(void *param, AS3_Val args);\r\n        QSP_EXTERN AS3_Val QSPSetSelActionIndex(void *param, AS3_Val args);\r\n        QSP_EXTERN AS3_Val QSPGetSelActionIndex(void *param, AS3_Val args);\r\n        QSP_EXTERN AS3_Val QSPIsActionsChanged(void *param, AS3_Val args);\r\n        QSP_EXTERN AS3_Val QSPGetObjectsCount(void *param, AS3_Val args);\r\n        QSP_EXTERN AS3_Val QSPGetObjectData(void *param, AS3_Val args);\r\n        QSP_EXTERN AS3_Val QSPSetSelObjectIndex(void *param, AS3_Val args);\r\n        QSP_EXTERN AS3_Val QSPGetSelObjectIndex(void *param, AS3_Val args);\r\n        QSP_EXTERN AS3_Val QSPIsObjectsChanged(void *param, AS3_Val args);\r\n        QSP_EXTERN AS3_Val QSPShowWindow(void *param, AS3_Val args);\r\n        QSP_EXTERN AS3_Val QSPGetVarValuesCount(void *param, AS3_Val args);\r\n        QSP_EXTERN AS3_Val QSPGetVarValues(void *param, AS3_Val args);\r\n        QSP_EXTERN AS3_Val QSPGetMaxVarsCount(void *param, AS3_Val args);\r\n        QSP_EXTERN AS3_Val QSPGetVarNameByIndex(void *param, AS3_Val args);\r\n        QSP_EXTERN AS3_Val QSPExecString(void *param, AS3_Val args);\r\n        QSP_EXTERN AS3_Val QSPExecCounter(void *param, AS3_Val args);\r\n        QSP_EXTERN AS3_Val QSPExecUserInput(void *param, AS3_Val args);\r\n        QSP_EXTERN AS3_Val QSPExecLocationCode(void *param, AS3_Val args);\r\n        QSP_EXTERN AS3_Val QSPGetLastErrorData(void *param, AS3_Val args);\r\n        QSP_EXTERN AS3_Val QSPGetErrorDesc(void *param, AS3_Val args);\r\n        QSP_EXTERN AS3_Val QSPLoadGameWorld(void *param, AS3_Val args);\r\n        QSP_EXTERN AS3_Val QSPLoadGameWorldFromData(void *param, AS3_Val args);\r\n        QSP_EXTERN AS3_Val QSPSaveGame(void *param, AS3_Val args);\r\n        QSP_EXTERN AS3_Val QSPSaveGameAsString(void *param, AS3_Val args);\r\n        QSP_EXTERN AS3_Val QSPOpenSavedGame(void *param, AS3_Val args);\r\n        QSP_EXTERN AS3_Val QSPOpenSavedGameFromString(void *param, AS3_Val args);\r\n        QSP_EXTERN AS3_Val QSPRestartGame(void *param, AS3_Val args);\r\n        QSP_EXTERN AS3_Val QSPSelectMenuItem(void *param, AS3_Val args);\r\n        QSP_EXTERN AS3_Val QSPSetCallBack(void *param, AS3_Val args);\r\n        QSP_EXTERN AS3_Val QSPInit(void *param, AS3_Val args);\r\n        QSP_EXTERN AS3_Val QSPDeInit(void *param, AS3_Val args);\r\n        QSP_EXTERN AS3_Val QSPReturnValue(void *param, AS3_Val args);\r\n\r\n    #endif\r\n\r\n    #ifdef __cplusplus\r\n    }\r\n    #endif\r\n\r\n#endif\r\n\n'})}),"\n",(0,e.jsxs)(r.p,{children:["\u0410\u0432\u0442\u043e\u0440: ",(0,e.jsx)(r.strong,{children:"NTROPY"}),"\r\n12.05.2010 17:25"]})]})}function o(n={}){const{wrapper:r}={...(0,a.R)(),...n.components};return r?(0,e.jsx)(r,{...n,children:(0,e.jsx)(s,{...n})}):s(n)}},8453:(n,r,S)=>{S.d(r,{R:()=>_,x:()=>P});var e=S(6540);const a={},t=e.createContext(a);function _(n){const r=e.useContext(t);return e.useMemo((function(){return"function"==typeof n?n(r):{...r,...n}}),[r,n])}function P(n){let r;return r=n.disableParentContext?"function"==typeof n.components?n.components(a):n.components||a:_(n.components),e.createElement(t.Provider,{value:r},n.children)}}}]);