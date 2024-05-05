# Generated from LAParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .LAParserParser import LAParserParser
else:
    from LAParserParser import LAParserParser

# This class defines a complete listener for a parse tree produced by LAParserParser.
class LAParserListener(ParseTreeListener):

    # Enter a parse tree produced by LAParserParser#program.
    def enterProgram(self, ctx:LAParserParser.ProgramContext):
        pass

    # Exit a parse tree produced by LAParserParser#program.
    def exitProgram(self, ctx:LAParserParser.ProgramContext):
        pass


    # Enter a parse tree produced by LAParserParser#declaracoes.
    def enterDeclaracoes(self, ctx:LAParserParser.DeclaracoesContext):
        pass

    # Exit a parse tree produced by LAParserParser#declaracoes.
    def exitDeclaracoes(self, ctx:LAParserParser.DeclaracoesContext):
        pass


    # Enter a parse tree produced by LAParserParser#decl_local_global.
    def enterDecl_local_global(self, ctx:LAParserParser.Decl_local_globalContext):
        pass

    # Exit a parse tree produced by LAParserParser#decl_local_global.
    def exitDecl_local_global(self, ctx:LAParserParser.Decl_local_globalContext):
        pass


    # Enter a parse tree produced by LAParserParser#declaracao_local.
    def enterDeclaracao_local(self, ctx:LAParserParser.Declaracao_localContext):
        pass

    # Exit a parse tree produced by LAParserParser#declaracao_local.
    def exitDeclaracao_local(self, ctx:LAParserParser.Declaracao_localContext):
        pass


    # Enter a parse tree produced by LAParserParser#declaracao_global.
    def enterDeclaracao_global(self, ctx:LAParserParser.Declaracao_globalContext):
        pass

    # Exit a parse tree produced by LAParserParser#declaracao_global.
    def exitDeclaracao_global(self, ctx:LAParserParser.Declaracao_globalContext):
        pass


    # Enter a parse tree produced by LAParserParser#variavel.
    def enterVariavel(self, ctx:LAParserParser.VariavelContext):
        pass

    # Exit a parse tree produced by LAParserParser#variavel.
    def exitVariavel(self, ctx:LAParserParser.VariavelContext):
        pass


    # Enter a parse tree produced by LAParserParser#identificador.
    def enterIdentificador(self, ctx:LAParserParser.IdentificadorContext):
        pass

    # Exit a parse tree produced by LAParserParser#identificador.
    def exitIdentificador(self, ctx:LAParserParser.IdentificadorContext):
        pass


    # Enter a parse tree produced by LAParserParser#dimensao.
    def enterDimensao(self, ctx:LAParserParser.DimensaoContext):
        pass

    # Exit a parse tree produced by LAParserParser#dimensao.
    def exitDimensao(self, ctx:LAParserParser.DimensaoContext):
        pass


    # Enter a parse tree produced by LAParserParser#tipo.
    def enterTipo(self, ctx:LAParserParser.TipoContext):
        pass

    # Exit a parse tree produced by LAParserParser#tipo.
    def exitTipo(self, ctx:LAParserParser.TipoContext):
        pass


    # Enter a parse tree produced by LAParserParser#tipo_basico.
    def enterTipo_basico(self, ctx:LAParserParser.Tipo_basicoContext):
        pass

    # Exit a parse tree produced by LAParserParser#tipo_basico.
    def exitTipo_basico(self, ctx:LAParserParser.Tipo_basicoContext):
        pass


    # Enter a parse tree produced by LAParserParser#tipo_basico_ident.
    def enterTipo_basico_ident(self, ctx:LAParserParser.Tipo_basico_identContext):
        pass

    # Exit a parse tree produced by LAParserParser#tipo_basico_ident.
    def exitTipo_basico_ident(self, ctx:LAParserParser.Tipo_basico_identContext):
        pass


    # Enter a parse tree produced by LAParserParser#tipo_estendido.
    def enterTipo_estendido(self, ctx:LAParserParser.Tipo_estendidoContext):
        pass

    # Exit a parse tree produced by LAParserParser#tipo_estendido.
    def exitTipo_estendido(self, ctx:LAParserParser.Tipo_estendidoContext):
        pass


    # Enter a parse tree produced by LAParserParser#valor_constante.
    def enterValor_constante(self, ctx:LAParserParser.Valor_constanteContext):
        pass

    # Exit a parse tree produced by LAParserParser#valor_constante.
    def exitValor_constante(self, ctx:LAParserParser.Valor_constanteContext):
        pass


    # Enter a parse tree produced by LAParserParser#registro.
    def enterRegistro(self, ctx:LAParserParser.RegistroContext):
        pass

    # Exit a parse tree produced by LAParserParser#registro.
    def exitRegistro(self, ctx:LAParserParser.RegistroContext):
        pass


    # Enter a parse tree produced by LAParserParser#parametros.
    def enterParametros(self, ctx:LAParserParser.ParametrosContext):
        pass

    # Exit a parse tree produced by LAParserParser#parametros.
    def exitParametros(self, ctx:LAParserParser.ParametrosContext):
        pass


    # Enter a parse tree produced by LAParserParser#parametro.
    def enterParametro(self, ctx:LAParserParser.ParametroContext):
        pass

    # Exit a parse tree produced by LAParserParser#parametro.
    def exitParametro(self, ctx:LAParserParser.ParametroContext):
        pass


    # Enter a parse tree produced by LAParserParser#corpo.
    def enterCorpo(self, ctx:LAParserParser.CorpoContext):
        pass

    # Exit a parse tree produced by LAParserParser#corpo.
    def exitCorpo(self, ctx:LAParserParser.CorpoContext):
        pass


    # Enter a parse tree produced by LAParserParser#cmd.
    def enterCmd(self, ctx:LAParserParser.CmdContext):
        pass

    # Exit a parse tree produced by LAParserParser#cmd.
    def exitCmd(self, ctx:LAParserParser.CmdContext):
        pass


    # Enter a parse tree produced by LAParserParser#cmdLeia.
    def enterCmdLeia(self, ctx:LAParserParser.CmdLeiaContext):
        pass

    # Exit a parse tree produced by LAParserParser#cmdLeia.
    def exitCmdLeia(self, ctx:LAParserParser.CmdLeiaContext):
        pass


    # Enter a parse tree produced by LAParserParser#cmdEscreva.
    def enterCmdEscreva(self, ctx:LAParserParser.CmdEscrevaContext):
        pass

    # Exit a parse tree produced by LAParserParser#cmdEscreva.
    def exitCmdEscreva(self, ctx:LAParserParser.CmdEscrevaContext):
        pass


    # Enter a parse tree produced by LAParserParser#cmdSe.
    def enterCmdSe(self, ctx:LAParserParser.CmdSeContext):
        pass

    # Exit a parse tree produced by LAParserParser#cmdSe.
    def exitCmdSe(self, ctx:LAParserParser.CmdSeContext):
        pass


    # Enter a parse tree produced by LAParserParser#cmdCaso.
    def enterCmdCaso(self, ctx:LAParserParser.CmdCasoContext):
        pass

    # Exit a parse tree produced by LAParserParser#cmdCaso.
    def exitCmdCaso(self, ctx:LAParserParser.CmdCasoContext):
        pass


    # Enter a parse tree produced by LAParserParser#cmdPara.
    def enterCmdPara(self, ctx:LAParserParser.CmdParaContext):
        pass

    # Exit a parse tree produced by LAParserParser#cmdPara.
    def exitCmdPara(self, ctx:LAParserParser.CmdParaContext):
        pass


    # Enter a parse tree produced by LAParserParser#cmdEnquanto.
    def enterCmdEnquanto(self, ctx:LAParserParser.CmdEnquantoContext):
        pass

    # Exit a parse tree produced by LAParserParser#cmdEnquanto.
    def exitCmdEnquanto(self, ctx:LAParserParser.CmdEnquantoContext):
        pass


    # Enter a parse tree produced by LAParserParser#cmdFaca.
    def enterCmdFaca(self, ctx:LAParserParser.CmdFacaContext):
        pass

    # Exit a parse tree produced by LAParserParser#cmdFaca.
    def exitCmdFaca(self, ctx:LAParserParser.CmdFacaContext):
        pass


    # Enter a parse tree produced by LAParserParser#cmdAtribuicao.
    def enterCmdAtribuicao(self, ctx:LAParserParser.CmdAtribuicaoContext):
        pass

    # Exit a parse tree produced by LAParserParser#cmdAtribuicao.
    def exitCmdAtribuicao(self, ctx:LAParserParser.CmdAtribuicaoContext):
        pass


    # Enter a parse tree produced by LAParserParser#cmdChamada.
    def enterCmdChamada(self, ctx:LAParserParser.CmdChamadaContext):
        pass

    # Exit a parse tree produced by LAParserParser#cmdChamada.
    def exitCmdChamada(self, ctx:LAParserParser.CmdChamadaContext):
        pass


    # Enter a parse tree produced by LAParserParser#cmdRetorne.
    def enterCmdRetorne(self, ctx:LAParserParser.CmdRetorneContext):
        pass

    # Exit a parse tree produced by LAParserParser#cmdRetorne.
    def exitCmdRetorne(self, ctx:LAParserParser.CmdRetorneContext):
        pass


    # Enter a parse tree produced by LAParserParser#selecao.
    def enterSelecao(self, ctx:LAParserParser.SelecaoContext):
        pass

    # Exit a parse tree produced by LAParserParser#selecao.
    def exitSelecao(self, ctx:LAParserParser.SelecaoContext):
        pass


    # Enter a parse tree produced by LAParserParser#item_selecao.
    def enterItem_selecao(self, ctx:LAParserParser.Item_selecaoContext):
        pass

    # Exit a parse tree produced by LAParserParser#item_selecao.
    def exitItem_selecao(self, ctx:LAParserParser.Item_selecaoContext):
        pass


    # Enter a parse tree produced by LAParserParser#constantes.
    def enterConstantes(self, ctx:LAParserParser.ConstantesContext):
        pass

    # Exit a parse tree produced by LAParserParser#constantes.
    def exitConstantes(self, ctx:LAParserParser.ConstantesContext):
        pass


    # Enter a parse tree produced by LAParserParser#numero_intervalo.
    def enterNumero_intervalo(self, ctx:LAParserParser.Numero_intervaloContext):
        pass

    # Exit a parse tree produced by LAParserParser#numero_intervalo.
    def exitNumero_intervalo(self, ctx:LAParserParser.Numero_intervaloContext):
        pass


    # Enter a parse tree produced by LAParserParser#op_unario.
    def enterOp_unario(self, ctx:LAParserParser.Op_unarioContext):
        pass

    # Exit a parse tree produced by LAParserParser#op_unario.
    def exitOp_unario(self, ctx:LAParserParser.Op_unarioContext):
        pass


    # Enter a parse tree produced by LAParserParser#exp_aritmetica.
    def enterExp_aritmetica(self, ctx:LAParserParser.Exp_aritmeticaContext):
        pass

    # Exit a parse tree produced by LAParserParser#exp_aritmetica.
    def exitExp_aritmetica(self, ctx:LAParserParser.Exp_aritmeticaContext):
        pass


    # Enter a parse tree produced by LAParserParser#termo.
    def enterTermo(self, ctx:LAParserParser.TermoContext):
        pass

    # Exit a parse tree produced by LAParserParser#termo.
    def exitTermo(self, ctx:LAParserParser.TermoContext):
        pass


    # Enter a parse tree produced by LAParserParser#fator.
    def enterFator(self, ctx:LAParserParser.FatorContext):
        pass

    # Exit a parse tree produced by LAParserParser#fator.
    def exitFator(self, ctx:LAParserParser.FatorContext):
        pass


    # Enter a parse tree produced by LAParserParser#op1.
    def enterOp1(self, ctx:LAParserParser.Op1Context):
        pass

    # Exit a parse tree produced by LAParserParser#op1.
    def exitOp1(self, ctx:LAParserParser.Op1Context):
        pass


    # Enter a parse tree produced by LAParserParser#op2.
    def enterOp2(self, ctx:LAParserParser.Op2Context):
        pass

    # Exit a parse tree produced by LAParserParser#op2.
    def exitOp2(self, ctx:LAParserParser.Op2Context):
        pass


    # Enter a parse tree produced by LAParserParser#op3.
    def enterOp3(self, ctx:LAParserParser.Op3Context):
        pass

    # Exit a parse tree produced by LAParserParser#op3.
    def exitOp3(self, ctx:LAParserParser.Op3Context):
        pass


    # Enter a parse tree produced by LAParserParser#parcela.
    def enterParcela(self, ctx:LAParserParser.ParcelaContext):
        pass

    # Exit a parse tree produced by LAParserParser#parcela.
    def exitParcela(self, ctx:LAParserParser.ParcelaContext):
        pass


    # Enter a parse tree produced by LAParserParser#parcela_unario.
    def enterParcela_unario(self, ctx:LAParserParser.Parcela_unarioContext):
        pass

    # Exit a parse tree produced by LAParserParser#parcela_unario.
    def exitParcela_unario(self, ctx:LAParserParser.Parcela_unarioContext):
        pass


    # Enter a parse tree produced by LAParserParser#parcela_nao_unario.
    def enterParcela_nao_unario(self, ctx:LAParserParser.Parcela_nao_unarioContext):
        pass

    # Exit a parse tree produced by LAParserParser#parcela_nao_unario.
    def exitParcela_nao_unario(self, ctx:LAParserParser.Parcela_nao_unarioContext):
        pass


    # Enter a parse tree produced by LAParserParser#exp_relacional.
    def enterExp_relacional(self, ctx:LAParserParser.Exp_relacionalContext):
        pass

    # Exit a parse tree produced by LAParserParser#exp_relacional.
    def exitExp_relacional(self, ctx:LAParserParser.Exp_relacionalContext):
        pass


    # Enter a parse tree produced by LAParserParser#op_relacional.
    def enterOp_relacional(self, ctx:LAParserParser.Op_relacionalContext):
        pass

    # Exit a parse tree produced by LAParserParser#op_relacional.
    def exitOp_relacional(self, ctx:LAParserParser.Op_relacionalContext):
        pass


    # Enter a parse tree produced by LAParserParser#expressao.
    def enterExpressao(self, ctx:LAParserParser.ExpressaoContext):
        pass

    # Exit a parse tree produced by LAParserParser#expressao.
    def exitExpressao(self, ctx:LAParserParser.ExpressaoContext):
        pass


    # Enter a parse tree produced by LAParserParser#termo_logico.
    def enterTermo_logico(self, ctx:LAParserParser.Termo_logicoContext):
        pass

    # Exit a parse tree produced by LAParserParser#termo_logico.
    def exitTermo_logico(self, ctx:LAParserParser.Termo_logicoContext):
        pass


    # Enter a parse tree produced by LAParserParser#fator_logico.
    def enterFator_logico(self, ctx:LAParserParser.Fator_logicoContext):
        pass

    # Exit a parse tree produced by LAParserParser#fator_logico.
    def exitFator_logico(self, ctx:LAParserParser.Fator_logicoContext):
        pass


    # Enter a parse tree produced by LAParserParser#parcela_logica.
    def enterParcela_logica(self, ctx:LAParserParser.Parcela_logicaContext):
        pass

    # Exit a parse tree produced by LAParserParser#parcela_logica.
    def exitParcela_logica(self, ctx:LAParserParser.Parcela_logicaContext):
        pass


    # Enter a parse tree produced by LAParserParser#op_logico_1.
    def enterOp_logico_1(self, ctx:LAParserParser.Op_logico_1Context):
        pass

    # Exit a parse tree produced by LAParserParser#op_logico_1.
    def exitOp_logico_1(self, ctx:LAParserParser.Op_logico_1Context):
        pass


    # Enter a parse tree produced by LAParserParser#op_logico_2.
    def enterOp_logico_2(self, ctx:LAParserParser.Op_logico_2Context):
        pass

    # Exit a parse tree produced by LAParserParser#op_logico_2.
    def exitOp_logico_2(self, ctx:LAParserParser.Op_logico_2Context):
        pass



del LAParserParser