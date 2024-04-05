const assert = require('assert')
const { remote } = require('webdriverio');

(async () => {
    const capabilities = {
        protocol: 'http',
        hostname: '127.0.0.1',
        path: '/',
        port: 4723,
        capabilities: {
            platformName: 'Android',
            'appium:options' : {
                deviceName: 'emulator-5554',
                avd: 'nexus_4_14.0',
                automationName: 'UiAutomator2',
                app: '/app/calculadora.apk'
            }
        }
    };

    const driver = await remote(capabilities);

    // Agora você pode interagir com os elementos na página
    await driver.$("id:com.google.android.calculator:id/digit_2").click();
    await driver.$("accessibility id:plus").click();
    await driver.$("id:com.google.android.calculator:id/digit_2").click();
    await driver.$("accessibility id:equals").click();
    const resultElement = await driver.$("id:com.google.android.calculator:id/result_final");
    const resultText = await resultElement.getText();

    assert.strictEqual(resultText, "4","O resultado deve ser igual a 4");

    // Não esqueça de finalizar a sessão depois que terminar
    await driver.deleteSession();
})();