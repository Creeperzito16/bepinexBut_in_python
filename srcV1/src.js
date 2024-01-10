Interceptor.attach(ptr(Module.findExportByName(null, 'dlopen')), {
    onEnter: function (args) {
        send("[*] Função dlopen foi chamada!");
    }
});

Interceptor.attach(ptr(Module.findExportByName(null, 'strcmp')), {
    onEnter: function (args) {
        send("[*] Função strcmp foi chamada!");
    }
});

// Adicione mais interceptações para outras funções, se necessário
// Exemplo: Interceptor.attach(ptr(Module.findExportByName(null, 'outra_funcao')), {
//              onEnter: function (args) {
//                  send("[*] Outra função foi chamada!");
//              }
//          });