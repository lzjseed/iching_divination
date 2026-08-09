# Fix Gradle Sync Error: Task 'prepareKotlinBuildScriptModel' not found

The project is failing to sync because the IDE is trying to execute a Kotlin DSL-related task (`prepareKotlinBuildScriptModel`) on a project that uses Groovy DSL. This is often caused by version mismatches between Gradle, Android Gradle Plugin (AGP), and the Kotlin plugin, especially with newer Gradle versions like 8.12.

## User Review Required

> [!IMPORTANT]
> I am proposing to upgrade the Android Gradle Plugin (AGP) and Kotlin versions to ensure compatibility with Gradle 8.12. This might require minor adjustments to other dependencies if they have strict version requirements.

## Proposed Changes

### Build Configuration

#### [MODIFY] [root build.gradle](file:///D:/Gits/lzjseed/iching_divination/build.gradle)
- Upgrade AGP from `8.2.0` to `8.5.2`.
- Upgrade Kotlin from `1.9.0` to `1.9.24`.

#### [MODIFY] [gradle-wrapper.properties](file:///D:/Gits/lzjseed/iching_divination/gradle/wrapper/gradle-wrapper.properties)
- Downgrade Gradle to `8.7` to be more in line with AGP 8.5.2 stability, OR keep `8.12` and see if the version upgrades fix it. I will try keeping `8.12` first but with newer plugins.
- Actually, AGP 8.2.0 is definitely too old for Gradle 8.12. I'll upgrade AGP to `8.5.2`.

### Cleanup

#### [DELETE] `app/.idea/` and `app/.gradle/`
- These directories should only exist at the root. Their presence in the `app/` submodule suggests it was opened as a separate project, which can confuse Gradle sync.

## Verification Plan

### Automated Tests
- Run `gradle_sync` to ensure the project synchronizes without errors.
- Run `gradle_build("help")` to verify basic Gradle functionality.

### Manual Verification
- Verify that the project structure is correctly recognized in Android Studio.
