---

## Montando o ambiente

### Java

Baixe o **Java JDK** : https://www.oracle.com/br/java/technologies/downloads/

Coloque nas variáveis de ambiente o JAVA_HOME, que é o diretório que acabou de ser instalado o java 

**Exemplo**: `C:\Program Files\Java\jdk-22`

E depois adicione no path o caminho da pasta “`bin`” do java, neste formato: `%JAVA_HOME%\bin`

### Android Studio

Baixe e instale o **Android Studio**: https://developer.android.com/studio?hl=pt-br seguindo os passos básicos

Quando abrir o android studio, escolha a opção “**Custom**” em vez de “**Standard**”, selecione o ADD (Android Virtual Device) para instalar o emulador, além de escolheras opções de Performance do hypervisor driver, a API e o android SDK. **Prossiga com a instalação**

- Inicie um novo projeto com as opções mais básicas
- No lado direito superior vá na engrenagem e selecione SDK Manager
- Em **SDK Platforms**: selecione uma versão mais antiga da API do SDK que é o recomendado pelo Appium  (**Exemplo: 10.0 - API 29**)
- Em **SDK Tools:** opções que devem marcar são: Android Emulator, Android Emulator hypervisor, Android SDK Platform-Tools, Layout Inspector (a versão da API escolhida)
- No lado direito procure a opção “**Device Manager**” e clique para adicionar um novo dispositivo e escolha a opção do dispositivo (Exemplo: Pixel 2), após isso selecione a API Level (igual a instalada acima no SDK Platforms)
- Para iniciar o emulador é só clicar no botão de Play

Após ter criado o emulador e conseguido executá-lo a primeira vez, coloque a pasta do Sdk numa variáve de ambiente “`ANDROID_HOME`”, geralmente fica em um caminho parecido com “`C:\usr\alexa\AppData\Local\Android\Sdk`”

E logo depois crie duas variáveis de ambiente com os caminhos sendo “`%ANDROID_HOME%\platform-tools`” e “`%ANDROID_HOME%\emulator`” para ser possível executar o “adb” e o “emulator” por linha de comando..

### Comandos de terminal

- emulator -list-avds →  Mostra todas os dispositivos virtuais
- emulator -avd `appium` → Inicia o emulador sem precisar abrir o android studio

## Iniciando com Appium (emulador local)

- Antes de instalar o Appium, instale o NVM que é o gerenciador de versões node, e instale a última versão a partir da que tem no site do node.
- Abra o terminal em modo administrador e use os comandos NVM após colocá-lo nas variáveis de ambiente, caso ele não faça sozinho, é algo assim
- Após isso, use o comando “`nvm install xx.xx.xx`” para instalar a versão e depois use o “`nvm use xx.xx.xx`” para começar a usar esta versão.
- Instale o appium globalmente, use o comando “`npm install -g appium`”

---

Para instalar o **appium** : https://appium.io/docs/en/2.5/quickstart/install/

Instale também o **appium-inspector** (ou use web): https://appium.github.io/appium-inspector/2024.2/quickstart/installation/

Quando confirmar que o appium está funcionando pela linha de comando, instale o “uiautomator2” usando o seguinte comando: 

`appium driver install uiautomator2` uiautomator precisa ser instalado para permitir que o appium automatize uma plataforma específica. (Os drivers  disponíveis estão neste link para referência https://appium.io/docs/en/latest/ecosystem/drivers/)

Capabilities básicas e iniciais para iniciar sem aplicativo

```python
{
  "platformName": "Android",
  "appium:deviceName": "emulator-5554",
  "appium:avd": "appium",
  "appium:automationName": "UiAutomator2",
}
```

Capabilities mais refinadas para abrir com um aplicativo ([Necessário ter o aplicativo instalado](https://www.notion.so/Appium-ed57c34b4a174238aef2212a2f094f04?pvs=21))

```powershell
{
"platformName": "Android",
"appium:deviceName": "emulator-5554",
"appium:avd": "AppiumP",
"appium:automationName": "UiAutomator2",
"appPackage": "com.android.calculator2",
"appActivity": "com.android.calculator2.Calculator",
}
```

---

### Iniciando a automação

Passo a passo

**Pré condições:**

<aside>
💡 1. Dispositivo virtual já configurado e funcionando (pelo android studio)
2. Appium instalado com uiautomator2
3. Appium inspector instalado e inserido as capabitilies acima

</aside>

1. Inicie o servidor appium usando o comando `appium server` (ou só appium)
2. Coloque as capabilities no appium inspector e será executado
3. Navegue usando o emulador que foi aberto

O inspector tira uma screen shot do emulador e mostra os elementos, portanto, para inspecionar os elementos e interagir com a tela, deve-se ficar atualizando usando o botão central superior “Refresh Source & Screenshot”

---

### Instalar aplicativos dentro do emulador

**APK Downloader**

https://apps.evozi.com/apk-downloader/

Buscar os Apps pela playstore

https://play.google.com/store/apps?hl=pt_BR

---

Feito isso, baixe o APK, para instalar ele no emulador, existem duas formas:

**Segurando e arrastando:**

Arraste o APK para dentro do emulador com ele em execução e irá instalar normalmente.

**Através de comandos ADB:**

Abra o terminal e vá até a pasta que está sua aplicação pelo terminal e utilize o seguinte comando:

```
adb install nome-do-apk
```

Com isso, o aplicativo deve ser instalado corretamente e já aparecer disponível na lista de aplicações do seu dispositivo.

Agora com o aplicativo instalado, para conseguirmos preencher os valores destes parâmetros

```python
  "appium:appPackage": "",
  "appium:appActivity": "",
```

Vamos seguir os passos indicados [aqui](https://www.notion.so/Appium-ed57c34b4a174238aef2212a2f094f04?pvs=21)

---

### AVD

Pode-se usar o telnet (https://www.locaweb.com.br/ajuda/wiki/como-utilizar-o-telnet/) para se conectar ao device em tempo de execução para ter informações sobre ele, tendo alguns comandos úteis para se utilizar usando o “`avd`”: 

**telnet [localhost](http://localhost/) 5554**

use o comando `avd help` após se conectar ao device para ter mais informações sobre o que é possível fazer.

---

### ADB

Abrir outro terminal e usar o comando “`adb shell`” faz com que tenha acesso ao emulador em tempo real.

Para capturar os valores para appPackage e appActivity, abra pelo emulador o aplicativo que quer saber essas informações e use um dos comandos abaixo:

```powershell
**// Em Windows
adb shell dumpsys window | findstr "mCurrentFocus”** 
adb shell dumpsys window windows | findstr 'mCurrentFocus’
// Linux
adb shell dumpsys window windows | grep mCurrentFocus
```

O retorno será algo como isso

```powershell
mCurrentFocus=Window{bbc16fb u0 com.google.android.calculator/com.android.calculator2.Calculator}
```

Sendo estes valores respectivamente

**appPackage**: `com.google.android.calculator`

**appActivity**: `com.android.calculator2.Calculator`

Os aplicativos instalados não são acessíveis fora do emulador, portanto, assim que for instalado, o emulador pode ser fechado sem problema que quando for iniciado novamente, o aplicativo estará lá.

### Comandos ADB úteis

https://github.com/clarabez/comandosadb

**adb devices**

**adb install <arquivo apk instalado>**

**adb shell dumpsys window windows | findstr 'mCurrentFocus’**

**adb shell dumpsys window | findstr "mCurrentFocus”** **(Capturar tela atual do emulador)**

**Em caso de erro “WebDriverException An Unknown server-side error” ↓**

**adb uninstall io.appium.uiautomator2.server** 

**adb uninstall io.appium.uiautomator2.server.test**

**Usar os comandos acima ↑**

---