# Changelog

## 0.1.2 (2025-05-16)

Full Changelog: [v0.1.1...v0.1.2](https://github.com/OpenExecProtocol/oxp-python/compare/v0.1.1...v0.1.2)

### Bug Fixes

* **package:** support direct resource imports ([72c4510](https://github.com/OpenExecProtocol/oxp-python/commit/72c4510d911d8d1a370d61544801656bc89ec380))
* **perf:** optimize some hot paths ([6b0e567](https://github.com/OpenExecProtocol/oxp-python/commit/6b0e5678583e03c373ee4f7e78bf6298659a92b1))
* **perf:** skip traversing types for NotGiven values ([286dd31](https://github.com/OpenExecProtocol/oxp-python/commit/286dd311a3d0689f8d19114a80b64a8a6f95e5be))
* pluralize `list` response variables ([#18](https://github.com/OpenExecProtocol/oxp-python/issues/18)) ([83e50f3](https://github.com/OpenExecProtocol/oxp-python/commit/83e50f3c775959dae738d5d927fcf3ccfc2652bc))
* **pydantic v1:** more robust ModelField.annotation check ([151c8d7](https://github.com/OpenExecProtocol/oxp-python/commit/151c8d76c13ead33aee207edfedf1a7e5154443c))


### Chores

* broadly detect json family of content-type headers ([6581584](https://github.com/OpenExecProtocol/oxp-python/commit/65815847ad2c3f4e3f6f538978b26fe6cbf51c98))
* **ci:** add timeout thresholds for CI jobs ([5f8b24d](https://github.com/OpenExecProtocol/oxp-python/commit/5f8b24de0fedd15f744f0e27579693b06c2bcf8d))
* **ci:** fix installation instructions ([5dbb8ab](https://github.com/OpenExecProtocol/oxp-python/commit/5dbb8abd11a7e814f2f2e29d9ce57757f322a0a6))
* **ci:** only use depot for staging repos ([55e4d39](https://github.com/OpenExecProtocol/oxp-python/commit/55e4d39a1e10e4e0009a5b31a36f635e448f18e2))
* **ci:** upload sdks to package manager ([17a00b4](https://github.com/OpenExecProtocol/oxp-python/commit/17a00b41e83ffa3ab321ae0d098dad657796d2f2))
* **client:** minor internal fixes ([53c5d34](https://github.com/OpenExecProtocol/oxp-python/commit/53c5d34be4f5b5601321d886f4e86e054a394795))
* fix typos ([#16](https://github.com/OpenExecProtocol/oxp-python/issues/16)) ([4f69dfa](https://github.com/OpenExecProtocol/oxp-python/commit/4f69dfa1eb5016931e4febad4eebfaa2538c681d))
* **internal:** avoid errors for isinstance checks on proxies ([2667249](https://github.com/OpenExecProtocol/oxp-python/commit/266724983d1edbdca30f58b6175146ebf50a0510))
* **internal:** base client updates ([b1ec190](https://github.com/OpenExecProtocol/oxp-python/commit/b1ec19072e83637a07bfd8a305a9723698b98f8c))
* **internal:** bump pyright version ([24419c5](https://github.com/OpenExecProtocol/oxp-python/commit/24419c513a2e19ed18e3e734f68149aea4b989d9))
* **internal:** codegen related update ([4f449d6](https://github.com/OpenExecProtocol/oxp-python/commit/4f449d6a67753b051f0e1e72e63f7cdb0edc6bdf))
* **internal:** expand CI branch coverage ([e8a9f71](https://github.com/OpenExecProtocol/oxp-python/commit/e8a9f71f2f556bc7ab2d8c2193c1fd9fa44cec4e))
* **internal:** fix list file params ([f0cd66c](https://github.com/OpenExecProtocol/oxp-python/commit/f0cd66c23b9805f44268af34be9a4d613fa3c12e))
* **internal:** import reformatting ([102ccf2](https://github.com/OpenExecProtocol/oxp-python/commit/102ccf2387b007066f1c880c96e1d743c0578759))
* **internal:** reduce CI branch coverage ([908e6bc](https://github.com/OpenExecProtocol/oxp-python/commit/908e6bc4009e946b0eb65d59db4d82284f26b070))
* **internal:** refactor retries to not use recursion ([76e2a76](https://github.com/OpenExecProtocol/oxp-python/commit/76e2a76f2c3cb04af873be16b8d9af04f273949d))
* **internal:** remove trailing character ([#19](https://github.com/OpenExecProtocol/oxp-python/issues/19)) ([b870e56](https://github.com/OpenExecProtocol/oxp-python/commit/b870e569254debfbeffed25051a080c1650987eb))
* **internal:** slight transform perf improvement ([#20](https://github.com/OpenExecProtocol/oxp-python/issues/20)) ([1e27481](https://github.com/OpenExecProtocol/oxp-python/commit/1e27481a8e4eef43b8df3cb6b6bb9010ba12e783))
* **internal:** update models test ([6a227e2](https://github.com/OpenExecProtocol/oxp-python/commit/6a227e207e281f30d8fb1e588551bade9da4caf4))
* **internal:** update pyright settings ([dac518e](https://github.com/OpenExecProtocol/oxp-python/commit/dac518ec8de90d4854ca6b828661083e84b183ee))

## 0.1.1 (2025-03-17)

Full Changelog: [v0.1.0...v0.1.1](https://github.com/OpenExecProtocol/oxp-python/compare/v0.1.0...v0.1.1)

### Bug Fixes

* **ci:** remove publishing patch ([#12](https://github.com/OpenExecProtocol/oxp-python/issues/12)) ([2910bc2](https://github.com/OpenExecProtocol/oxp-python/commit/2910bc21d18ae16a8cc999f8553d35eb7d4773d1))

## 0.1.0 (2025-03-17)

Full Changelog: [v0.0.2...v0.1.0](https://github.com/OpenExecProtocol/oxp-python/compare/v0.0.2...v0.1.0)

### Features

* CI fix ([43570f3](https://github.com/OpenExecProtocol/oxp-python/commit/43570f3352ea7cd28250e63f6efd87287bd7923e))


### Bug Fixes

* **ci:** ensure pip is always available ([#10](https://github.com/OpenExecProtocol/oxp-python/issues/10)) ([4594515](https://github.com/OpenExecProtocol/oxp-python/commit/4594515bd8c5500adfa6f6c511e86490b314426d))

## 0.0.2 (2025-03-15)

Full Changelog: [v0.0.1-alpha.1...v0.0.2](https://github.com/OpenExecProtocol/oxp-python/compare/v0.0.1-alpha.1...v0.0.2)

### Features

* **api:** update via SDK Studio ([#5](https://github.com/OpenExecProtocol/oxp-python/issues/5)) ([10b7707](https://github.com/OpenExecProtocol/oxp-python/commit/10b770743b760ccc9b7a806fbebcd6d6c5eab9e9))

## 0.0.1-alpha.1 (2025-03-15)

Full Changelog: [v0.0.1-alpha.0...v0.0.1-alpha.1](https://github.com/OpenExecProtocol/oxp-python/compare/v0.0.1-alpha.0...v0.0.1-alpha.1)

### Chores

* go live ([#1](https://github.com/OpenExecProtocol/oxp-python/issues/1)) ([f34fa80](https://github.com/OpenExecProtocol/oxp-python/commit/f34fa8031bcf789d102f6292c480eb42a3c145ce))
* update SDK settings ([#3](https://github.com/OpenExecProtocol/oxp-python/issues/3)) ([3b8297b](https://github.com/OpenExecProtocol/oxp-python/commit/3b8297ba07fcdd5231f1f96ac25e8acc2d328d99))
