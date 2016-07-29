#! /usr/bin/env node

var fs = require('fs');
var esprima = require('esprima');

function traversal(ast, hooks) {
    if (ast == null) {
    } else if (ast instanceof Array) {
        for (i in ast) {
            traversal(ast[i], hooks);
        }
    } else if (typeof(ast) == 'object') {
        switch (ast['type']) {
        case 'AssignmentExpression':
            if ('AssignmentExpression' in hooks) {
                hooks['AssignmentExpression'](ast);
            }
            traversal(ast['left'], hooks);
            traversal(ast['right'], hooks);
            break;
        case 'AssignmentPattern':
            break;
        case 'ArrayExpression':
            if ('ArrayExpression' in hooks) {
                hooks['ArrayExpression'](ast);
            }
            traversal(ast['elements'], hooks);
            break;
        case 'ArrayPattern':
            break;
        case 'ArrowFunctionExpression':
            break;
        case 'BlockStatement':
            if ('BlockStatement' in hooks) {
                hooks['BlockStatement'](ast);
            }
            traversal(ast['body'], hooks);
            break;
        case 'BinaryExpression':
            if ('BinaryExpression' in hooks) {
                hooks['BinaryExpression'](ast);
            }
            traversal(ast['left'], hooks);
            traversal(ast['right'], hooks);
            break;
        case 'BreakStatement':
            break;
        case 'CallExpression':
            if ('CallExpression' in hooks) {
                hooks['CallExpression'](ast);
            }
            traversal(ast['callee'], hooks);
            traversal(ast['arguments'], hooks);
            break;
        case 'CatchClause':
            break;
        case 'ClassBody':
            break;
        case 'ClassDeclaration':
            break;
        case 'ClassExpression':
            break;
        case 'ConditionalExpression':
            if ('ConditionalExpression' in hooks) {
                hooks['ConditionalExpression'](ast);
            }
            traversal(ast['test'], hooks);
            traversal(ast['consequent'], hooks);
            traversal(ast['alternate'], hooks);
            break;
        case 'ContinueStatement':
            break;
        case 'DoWhileStatement':
            if ('DoWhileStatement' in hooks) {
                hooks['DoWhileStatement'](ast);
            }
            traversal(ast['consequent'], hooks);
            traversal(ast['test'], hooks);
            break;
        case 'DebuggerStatement':
            break;
        case 'EmptyStatement':
            break;
        case 'ExportAllDeclaration':
            break;
        case 'ExportDefaultDeclaration':
            break;
        case 'ExportNamedDeclaration':
            break;
        case 'ExportSpecifier':
            break;
        case 'ExpressionStatement':
            if ('ExpressionStatement' in hooks) {
                hooks['ExpressionStatement'](ast);
            }
            traversal(ast['expression'], hooks);
            break;
        case 'ForStatement':
            if ('ForStatement' in hooks) {
                hooks['ForStatement'](ast);
            }
            traversal(ast['init'], hooks);
            traversal(ast['test'], hooks);
            traversal(ast['update'], hooks);
            traversal(ast['body'], hooks);
            break;
        case 'ForOfStatement':
            break;
        case 'ForInStatement':
            if ('ForInStatement' in hooks) {
                hooks['ForInStatement'](ast);
            }
            traversal(ast['left'], hooks);
            traversal(ast['right'], hooks);
            traversal(ast['body'], hooks);
            break;
        case 'FunctionDeclaration':
            if ('FunctionDeclaration' in hooks) {
                hooks['FunctionDeclaration'](ast);
            }
            traversal(ast['id'], hooks);
            traversal(ast['params'], hooks);
            traversal(ast['defaults'], hooks);
            traversal(ast['body'], hooks);
            break;
        case 'FunctionExpression':
            if ('FunctionExpression' in hooks) {
                hooks['FunctionExpression'](ast);
            }
            traversal(ast['params'], hooks);
            traversal(ast['defaults'], hooks);
            traversal(ast['body'], hooks);
            break;
        case 'Identifier':
            break;
        case 'IfStatement':
            if ('IfStatement' in hooks) {
                hooks['IfStatement'](ast);
            }
            traversal(ast['test'], hooks);
            traversal(ast['consequent'], hooks);
            break;
        case 'ImportDeclaration':
            break;
        case 'ImportDefaultSpecifier':
            break;
        case 'ImportNamespaceSpecifier':
            break;
        case 'ImportSpecifier':
            break;
        case 'Literal':
            break;
        case 'LabeledStatement':
            break;
        case 'LogicalExpression':
            if ('LogicalExpression' in hooks) {
                hooks['LogicalExpression'](ast);
            }
            traversal(ast['left'], hooks);
            traversal(ast['right'], hooks);
            break;
        case 'MemberExpression':
            if ('MemberExpression' in hooks) {
                hooks['MemberExpression'](ast);
            }
            traversal(ast['object'], hooks);
            traversal(ast['property'], hooks);
            break;
        case 'MetaProperty':
            break;
        case 'MethodDefinition':
            break;
        case 'NewExpression':
            break;
        case 'ObjectExpression':
            if ('ObjectExpression' in hooks) {
                hooks['ObjectExpression'](ast);
            }
            traversal(ast['properties'], hooks);
            break;
        case 'ObjectPattern':
            break;
        case 'Program':
            if ('Program' in hooks) {
                hooks['Program'](ast);
            }
            traversal(ast['body'], hooks);
            break;
        case 'Property':
            if ('Property' in hooks) {
                hooks['Property'](ast);
            }
            traversal(ast['key'], hooks);
            traversal(ast['value'], hooks);
            break;
        case 'RestElement':
            break;
        case 'ReturnStatement':
            if ('ReturnStatement' in hooks) {
                hooks['ReturnStatement'](ast);
            }
            traversal(ast['argument'], hooks);
            break;
        case 'SequenceExpression':
            break;
        case 'SpreadElement':
            break;
        case 'Super':
            break;
        case 'SwitchCase':
            break;
        case 'SwitchStatement':
            break;
        case 'TaggedTemplateExpression':
            break;
        case 'TemplateElement':
            break;
        case 'TemplateLiteral':
            break;
        case 'ThisExpression':
            break;
        case 'ThrowStatement':
            break;
        case 'TryStatement':
            break;
        case 'UnaryExpression':
            break;
        case 'UpdateExpression':
            break;
        case 'VariableDeclaration':
            if ('VariableDeclaration' in hooks) {
                hooks['VariableDeclaration'](ast);
            }
            traversal(ast['id'], hooks);
            traversal(ast['init'], hooks);
            break;
        case 'VariableDeclarator':
            break;
        case 'WhileStatement':
            if ('WhileStatement' in hooks) {
                hooks['WhileStatement'](ast);
            }
            traversal(ast['test'], hooks);
            traversal(ast['consequent'], hooks);
            break;
        case 'WithStatement':
            break;
        case 'YieldExpression':
            break;
        default:
            console.log('error: ' + ast);
            break;
        }
    } else {
        console.log('error: ' + ast);
    }
}

function find_call(ast, func) {
    traversal(ast, hooks={
        'CallExpression': function (ast) {
            if (ast['callee']['type'] == 'Identifier' && ast['callee']['name'] == func) {
                console.log('"' + func + '" called in line: ' + ast['loc']['start']['line'] + ', column: ' + ast['loc']['start']['column']);
            }
        },
    });
}

if (process.argv.length == 3) {
    var buffer = fs.readFileSync(process.argv[2]).toString();
    var ast = esprima.parse(buffer, {'loc':true});
    find_call(ast, 'eval');
}
