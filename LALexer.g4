lexer grammar LALexer;

// Tokens
DECLARE : 'declare';
REAL : 'real';
INTEIRO : 'inteiro';
LITERAL : 'literal';
LEIA : 'leia';
ESCREVA : 'escreva';
SE : 'se';
ENTAO : 'entao';
SENAO : 'senao';
FIM_SE : 'fim_se';
FIM_ALGORITMO : 'fim_algoritmo';
FIM : 'fim';
CONSTANTE : 'constante';
TIPO : 'tipo';
LOGICO : 'logico';
REGISTRO : 'registro';
FIM_REGISTRO : 'fim_registro';
PROCEDIMENTO : 'procedimento';
VAR : 'var';
FALSO : 'falso';
ENQUANTO : 'enquanto';
VERDADEIRO : 'verdadeiro';
FACA : 'faca';
ATE : 'ate';
FIM_ENQUANTO : 'fim_enquanto';
FIM_PROCEDIMENTO : 'fim_procedimento';
CASO : 'caso';
FIM_CASO : 'fim_caso';
SEJA : 'seja';
PARA : 'para';
FIM_PARA : 'fim_para';
FUNCAO : 'funcao';
FIM_FUNCAO : 'fim_funcao';
RETORNE : 'retorne';
E : 'e';
OU : 'ou';
NAO : 'nao';

// Comentarios
COMMENT : '{' ~[\r\n]* '}' -> skip;

// Operadores aritméticos
OP_ARITMETICOS : ('+' | '-' | '*' | '/' | '%');

// Operadores relacionais
OP_RELACIONAIS : ('<' | '>' | '=' | '<-' | '<>' | '!=' | '<=' | '>=' | '==');

// Operadores de memória
OP_MEMORIA : ('&' | '^');

// Delimitadores
DELIMITADORES : (':' | ';' | ',' | '(' | ')' | '[' | ']' | '/' | '..' | '^' | '&');

// Regras para cadeias de caracteres entre aspas
CADEIA : '"' ~[\r\n"]* '"';

// Regras para números reais
NREAL : DIGITO+ '.' DIGITO+;

// Regras para números inteiros
NINTEIRO : DIGITO+;

// Regras para identificadores
IDENTIFICADOR : [a-zA-Z_] [a-zA-Z_0-9]*;

// Regra para espaços em branco
WS : [ \t\r\n]+ -> skip;

// Definição de fragmentos
fragment DIGITO : [0-9];

// Caracteres inválidos
INVALID_CHAR: . -> skip;



