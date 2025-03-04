# udis86 - scripts/ud_itab.py
# 
# Copyright (c) 2009, 2013 Vivek Thampi
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without modification, 
# are permitted provided that the following conditions are met:
# 
#     * Redistributions of source code must retain the above copyright notice, 
#       this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright notice, 
#       this list of conditions and the following disclaimer in the documentation 
#       and/or other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND 
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED 
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR 
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES 
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; 
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON 
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT 
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS 
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import os
import sys
import ud_optable
import ud_opcode

class UdItabGenerator( ud_opcode.UdOpcodeTables ):

    OperandDict = {
        "Av"       : [    "OP_A"        , "SZ_V"     ],
        "E"        : [    "OP_E"        , "SZ_NA"    ],
        "Eb"       : [    "OP_E"        , "SZ_B"     ],
        "Ew"       : [    "OP_E"        , "SZ_W"     ],
        "Ev"       : [    "OP_E"        , "SZ_V"     ],
        "Ed"       : [    "OP_E"        , "SZ_D"     ],
        "Ey"       : [    "OP_E"        , "SZ_Y"     ],
        "Eq"       : [    "OP_E"        , "SZ_Q"     ],
        "Ez"       : [    "OP_E"        , "SZ_Z"     ],
        "Fv"       : [    "OP_F"        , "SZ_V"     ],
        "G"        : [    "OP_G"        , "SZ_NA"    ],
        "Gb"       : [    "OP_G"        , "SZ_B"     ],
        "Gw"       : [    "OP_G"        , "SZ_W"     ],
        "Gv"       : [    "OP_G"        , "SZ_V"     ],
        "Gy"       : [    "OP_G"        , "SZ_Y"     ],
        "Gd"       : [    "OP_G"        , "SZ_D"     ],
        "Gq"       : [    "OP_G"        , "SZ_Q"     ],
        "Gz"       : [    "OP_G"        , "SZ_Z"     ],
        "M"        : [    "OP_M"        , "SZ_NA"    ],
        "Mb"       : [    "OP_M"        , "SZ_B"     ],
        "Mw"       : [    "OP_M"        , "SZ_W"     ],
        "Ms"       : [    "OP_M"        , "SZ_W"     ],
        "Md"       : [    "OP_M"        , "SZ_D"     ],
        "Mq"       : [    "OP_M"        , "SZ_Q"     ],
        "Mv"       : [    "OP_M"        , "SZ_V"     ],
        "Mt"       : [    "OP_M"        , "SZ_T"     ],
        "Mo"       : [    "OP_M"        , "SZ_O"     ],
        "MbRd"     : [    "OP_MR"       , "SZ_BD"    ],
        "MbRv"     : [    "OP_MR"       , "SZ_BV"    ],
        "MwRv"     : [    "OP_MR"       , "SZ_WV"    ],
        "MwRy"     : [    "OP_MR"       , "SZ_WY"    ],
        "MdRy"     : [    "OP_MR"       , "SZ_DY"    ],
        "I1"       : [    "OP_I1"       , "SZ_NA"    ],
        "I3"       : [    "OP_I3"       , "SZ_NA"    ],
        "Ib"       : [    "OP_I"        , "SZ_B"     ],
        "Iw"       : [    "OP_I"        , "SZ_W"     ],
        "Iv"       : [    "OP_I"        , "SZ_V"     ],
        "Iz"       : [    "OP_I"        , "SZ_Z"     ],
        "sIb"      : [    "OP_sI"       , "SZ_B"     ],
        "sIz"      : [    "OP_sI"       , "SZ_Z"     ],
        "sIv"      : [    "OP_sI"       , "SZ_V"     ],
        "Jv"       : [    "OP_J"        , "SZ_V"     ],
        "Jz"       : [    "OP_J"        , "SZ_Z"     ],
        "Jb"       : [    "OP_J"        , "SZ_B"     ],
        "R"        : [    "OP_R"        , "SZ_RDQ"   ], 
        "C"        : [    "OP_C"        , "SZ_NA"    ],
        "D"        : [    "OP_D"        , "SZ_NA"    ],
        "S"        : [    "OP_S"        , "SZ_NA"    ],
        "Ob"       : [    "OP_O"        , "SZ_B"     ],
        "Ow"       : [    "OP_O"        , "SZ_W"     ],
        "Ov"       : [    "OP_O"        , "SZ_V"     ],
        "U"        : [    "OP_U"        , "SZ_O"     ],
        "V"        : [    "OP_V"        , "SZ_O"     ],
        "MwU"      : [    "OP_MU"       , "SZ_WO"    ],
        "MdU"      : [    "OP_MU"       , "SZ_DO"    ],
        "MqU"      : [    "OP_MU"       , "SZ_QO"    ],
        "W"        : [    "OP_W"        , "SZ_O"     ],
        "N"        : [    "OP_N"        , "SZ_Q"     ],
        "P"        : [    "OP_P"        , "SZ_Q"     ],
        "Q"        : [    "OP_Q"        , "SZ_Q"     ],
        "AL"       : [    "OP_AL"       , "SZ_B"     ],
        "AX"       : [    "OP_AX"       , "SZ_W"     ],
        "eAX"      : [    "OP_eAX"      , "SZ_Z"     ],
        "rAX"      : [    "OP_rAX"      , "SZ_V"     ],
        "CL"       : [    "OP_CL"       , "SZ_B"     ],
        "CX"       : [    "OP_CX"       , "SZ_W"     ],
        "eCX"      : [    "OP_eCX"      , "SZ_Z"     ],
        "rCX"      : [    "OP_rCX"      , "SZ_V"     ],
        "DL"       : [    "OP_DL"       , "SZ_B"     ],
        "DX"       : [    "OP_DX"       , "SZ_W"     ],
        "eDX"      : [    "OP_eDX"      , "SZ_Z"     ],
        "rDX"      : [    "OP_rDX"      , "SZ_V"     ],
        "R0b"      : [    "OP_R0"       , "SZ_B"     ],
        "R1b"      : [    "OP_R1"       , "SZ_B"     ],
        "R2b"      : [    "OP_R2"       , "SZ_B"     ],
        "R3b"      : [    "OP_R3"       , "SZ_B"     ],
        "R4b"      : [    "OP_R4"       , "SZ_B"     ],
        "R5b"      : [    "OP_R5"       , "SZ_B"     ],
        "R6b"      : [    "OP_R6"       , "SZ_B"     ],
        "R7b"      : [    "OP_R7"       , "SZ_B"     ],
        "R0w"      : [    "OP_R0"       , "SZ_W"     ],
        "R1w"      : [    "OP_R1"       , "SZ_W"     ],
        "R2w"      : [    "OP_R2"       , "SZ_W"     ],
        "R3w"      : [    "OP_R3"       , "SZ_W"     ],
        "R4w"      : [    "OP_R4"       , "SZ_W"     ],
        "R5w"      : [    "OP_R5"       , "SZ_W"     ],
        "R6w"      : [    "OP_R6"       , "SZ_W"     ],
        "R7w"      : [    "OP_R7"       , "SZ_W"     ],
        "R0v"      : [    "OP_R0"       , "SZ_V"     ],
        "R1v"      : [    "OP_R1"       , "SZ_V"     ],
        "R2v"      : [    "OP_R2"       , "SZ_V"     ],
        "R3v"      : [    "OP_R3"       , "SZ_V"     ],
        "R4v"      : [    "OP_R4"       , "SZ_V"     ],
        "R5v"      : [    "OP_R5"       , "SZ_V"     ],
        "R6v"      : [    "OP_R6"       , "SZ_V"     ],
        "R7v"      : [    "OP_R7"       , "SZ_V"     ],
        "R0z"      : [    "OP_R0"       , "SZ_Z"     ],
        "R1z"      : [    "OP_R1"       , "SZ_Z"     ],
        "R2z"      : [    "OP_R2"       , "SZ_Z"     ],
        "R3z"      : [    "OP_R3"       , "SZ_Z"     ],
        "R4z"      : [    "OP_R4"       , "SZ_Z"     ],
        "R5z"      : [    "OP_R5"       , "SZ_Z"     ],
        "R6z"      : [    "OP_R6"       , "SZ_Z"     ],
        "R7z"      : [    "OP_R7"       , "SZ_Z"     ],
        "R0y"      : [    "OP_R0"       , "SZ_Y"     ],
        "R1y"      : [    "OP_R1"       , "SZ_Y"     ],
        "R2y"      : [    "OP_R2"       , "SZ_Y"     ],
        "R3y"      : [    "OP_R3"       , "SZ_Y"     ],
        "R4y"      : [    "OP_R4"       , "SZ_Y"     ],
        "R5y"      : [    "OP_R5"       , "SZ_Y"     ],
        "R6y"      : [    "OP_R6"       , "SZ_Y"     ],
        "R7y"      : [    "OP_R7"       , "SZ_Y"     ],
        "ES"       : [    "OP_ES"       , "SZ_NA"    ],
        "CS"       : [    "OP_CS"       , "SZ_NA"    ],
        "DS"       : [    "OP_DS"       , "SZ_NA"    ],
        "SS"       : [    "OP_SS"       , "SZ_NA"    ],
        "GS"       : [    "OP_GS"       , "SZ_NA"    ],
        "FS"       : [    "OP_FS"       , "SZ_NA"    ],
        "ST0"      : [    "OP_ST0"      , "SZ_NA"    ],
        "ST1"      : [    "OP_ST1"      , "SZ_NA"    ],
        "ST2"      : [    "OP_ST2"      , "SZ_NA"    ],
        "ST3"      : [    "OP_ST3"      , "SZ_NA"    ],
        "ST4"      : [    "OP_ST4"      , "SZ_NA"    ],
        "ST5"      : [    "OP_ST5"      , "SZ_NA"    ],
        "ST6"      : [    "OP_ST6"      , "SZ_NA"    ],
        "ST7"      : [    "OP_ST7"      , "SZ_NA"    ],
        "NONE"     : [    "OP_NONE"     , "SZ_NA"    ],
    }

    #
    # opcode prefix dictionary
    # 
    PrefixDict = { 
        "rep"      : "P_str",   
        "repz"     : "P_strz",   
        "aso"      : "P_aso",   
        "oso"      : "P_oso",   
        "rexw"     : "P_rexw", 
        "rexb"     : "P_rexb",  
        "rexx"     : "P_rexx",  
        "rexr"     : "P_rexr",
        "seg"      : "P_seg",
        "inv64"    : "P_inv64", 
        "def64"    : "P_def64", 
        "cast"     : "P_cast",
    }

    InvalidEntryIdx = 0 
    InvalidEntry = { 'type'     : 'invalid', 
                     'mnemonic' : 'invalid', 
                     'operands' : '', 
                     'prefixes' : '',
                     'meta'     : '' }

    Itab     = []   # instruction table
    ItabIdx  = 1    # instruction table index
    GtabIdx  = 0    # group table index
    GtabMeta = []

    ItabLookup = {}

    MnemonicAliases = ( "invalid", "3dnow", "none", "db", "pause" )
    
    def __init__( self ):
        # first itab entry (0) is Invalid
        self.Itab.append( self.InvalidEntry )
        self.MnemonicsTable.extend( self.MnemonicAliases )

    def toGroupId( self, id ):
        return 0x8000 | id

    def genLookupTable( self, table, scope = '' ):
        idxArray = [ ]
        ( tabIdx, self.GtabIdx ) = ( self.GtabIdx, self.GtabIdx + 1 )
        self.GtabMeta.append( { 'type' : table[ 'type' ], 'meta' : table[ 'meta' ] } )

        for _idx in range( self.sizeOfTable( table[ 'type' ] ) ):
            idx = "%02x" % _idx 

            e   = self.InvalidEntry
            i   = self.InvalidEntryIdx

            if idx in table[ 'entries' ].keys():
                e = table[ 'entries' ][ idx ]

            # leaf node (insn)
            if e[ 'type' ] == 'insn':
                ( i, self.ItabIdx ) = ( self.ItabIdx, self.ItabIdx + 1 )
                self.Itab.append( e )
            elif e[ 'type' ] != 'invalid':
                i = self.genLookupTable( e, 'static' )

            idxArray.append( i )

        name = "ud_itab__%s" % tabIdx
        self.ItabLookup[ tabIdx ] = name

        self.ItabC.write( "\n" );
        if len( scope ):
            self.ItabC.write( scope + ' ' )
        self.ItabC.write( "const uint16_t %s[] = {\n" % name )
        for i in range( len( idxArray ) ):
            if i > 0 and i % 4 == 0: 
                self.ItabC.write( "\n" )
            if ( i%4 == 0 ):
                self.ItabC.write( "  /* %2x */" % i)
            if idxArray[ i ] >= 0x8000:
                self.ItabC.write( "%12s," % ("GROUP(%d)" % ( ~0x8000 & idxArray[ i ] )))
            else:
                self.ItabC.write( "%12d," % ( idxArray[ i ] ))
        self.ItabC.write( "\n" )
        self.ItabC.write( "};\n" )

        return self.toGroupId( tabIdx )

    def genLookupTableList( self ):
        self.ItabC.write( "\n\n"  );
        self.ItabC.write( "struct ud_lookup_table_list_entry ud_lookup_table_list[] = {\n" )
        for i in range( len( self.GtabMeta ) ):
            f0 = self.ItabLookup[ i ] + ","
            f1 = ( self.nameOfTable( self.GtabMeta[ i ][ 'type' ] ) ) + ","
            f2 = "\"%s\"" % self.GtabMeta[ i ][ 'meta' ]
            self.ItabC.write( "    /* %03d */ { %s %s %s },\n" % ( i, f0, f1, f2 ) )
        self.ItabC.write( "};" )

    def genInsnTable( self ):
        self.ItabC.write( "struct ud_itab_entry ud_itab[] = {\n" );
        idx = 0
        for e in self.Itab:
            opr_c = [ "O_NONE", "O_NONE", "O_NONE" ]
            pfx_c = []
            opr   = e[ 'operands' ]
            for i in range(len(opr)): 
                if not (opr[i] in self.OperandDict.keys()):
                    print("error: invalid operand declaration: %s\n" % opr[i])
                opr_c[i] = "O_" + opr[i]
            opr = "%s %s %s" % (opr_c[0] + ",", opr_c[1] + ",", opr_c[2])

            for p in e['prefixes']:
                if not ( p in self.PrefixDict.keys() ):
                    print("error: invalid prefix specification: %s \n" % pfx)
                pfx_c.append( self.PrefixDict[p] )
            if len(e['prefixes']) == 0:
                pfx_c.append( "P_none" )
            pfx = "|".join( pfx_c )

            self.ItabC.write( "  /* %04d */ { UD_I%s %s, %s },\n" \
                        % ( idx, e[ 'mnemonic' ] + ',', opr, pfx ) )
            idx += 1
        self.ItabC.write( "};\n" )

        self.ItabC.write( "\n\n"  );
        self.ItabC.write( "const char * ud_mnemonics_str[] = {\n" )
        self.ItabC.write( ",\n    ".join( [ "\"%s\"" % m for m in self.MnemonicsTable ] ) )
        self.ItabC.write( "\n};\n" )
 

    def genItabH( self, filePath ):
        self.ItabH = open( filePath, "w" )

        # Generate Table Type Enumeration
        self.ItabH.write( "#ifndef UD_ITAB_H\n" )
        self.ItabH.write( "#define UD_ITAB_H\n\n" )

        self.ItabH.write("/* itab.h -- generated by udis86:scripts/ud_itab.py, do no edit */\n\n")

        # table type enumeration
        self.ItabH.write( "/* ud_table_type -- lookup table types (see decode.c) */\n" )
        self.ItabH.write( "enum ud_table_type {\n    " )
        enum = [ self.TableInfo[ k ][ 'name' ] for k in self.TableInfo.keys() ]
        self.ItabH.write( ",\n    ".join( enum ) )
        self.ItabH.write( "\n};\n\n" );

        # mnemonic enumeration
        self.ItabH.write( "/* ud_mnemonic -- mnemonic constants */\n" )
        enum  = "enum ud_mnemonic_code {\n    "
        enum += ",\n    ".join( [ "UD_I%s" % m for m in self.MnemonicsTable ] )
        enum += ",\n    UD_MAX_MNEMONIC_CODE"
        enum += "\n} UD_ATTR_PACKED;\n"
        self.ItabH.write( enum )
        self.ItabH.write( "\n" )

        self.ItabH.write( "extern const char * ud_mnemonics_str[];\n" )

        self.ItabH.write( "\n#endif /* UD_ITAB_H */\n" )
    
        self.ItabH.close()


    def genItabC( self, filePath ):
        self.ItabC = open( filePath, "w" )
        self.ItabC.write( "/* itab.c -- generated by udis86:scripts/ud_itab.py, do no edit" )
        self.ItabC.write( " */\n" );
        self.ItabC.write( "#include \"decode.h\"\n\n" );

        self.ItabC.write( "#define GROUP(n) (0x8000 | (n))\n\n" )

        self.genLookupTable( self.OpcodeTable0 ) 
        self.genLookupTableList()

        #
        # Macros defining short-names for operands
        #
        self.ItabC.write("\n\n/* itab entry operand definitions (for readability) */\n");
        operands = self.OperandDict.keys()
        operands = sorted(operands)
        for o in operands:
            self.ItabC.write("#define O_%-7s { %-12s %-8s }\n" %
                    (o, self.OperandDict[o][0] + ",", self.OperandDict[o][1]));
        self.ItabC.write("\n");

        self.genInsnTable()

        self.ItabC.close()

    def genItab( self, location ):
        self.genItabC(os.path.join(location, "itab.c"))
        self.genItabH(os.path.join(location, "itab.h"))

def usage():
    print("usage: ud_itab.py <optable.xml> <output-path>")

def main():

    if len(sys.argv) != 3:
        usage()
        sys.exit(1)
        
    generator = UdItabGenerator()
    optableXmlParser = ud_optable.UdOptableXmlParser()
    optableXmlParser.parse( sys.argv[ 1 ], generator.addInsnDef )
    generator.genItab(sys.argv[2])

if __name__ == '__main__':
    main()
