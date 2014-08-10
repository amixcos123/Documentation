Dota 2 Lua API
==============
{{Note | This page is automatically generated.  Any changes may be overwritten}}
  
==='''Accessing the DOTA 2 Scripting API from Lua===

While Lua is [http://en.wikipedia.org/wiki/Dynamically_typed dynamically typed], the DOTA 2 engine is written primarily in C++, which is [http://en.wikipedia.org/wiki/Type_system#Static_type-checking statically typed]. Thus, you'll need to be conscious of your data types when calling the API. (If you try to pass the wrong type to an API function, you'll get an error message in Vconsole telling you what you passed and what it was expecting.)


Global
############
Global functions.  These can be called without any class

  * :ref:`AngleDiff(float ang1, float ang2) <Global.AngleDiff>`
  * :ref:`AppendToLogFile(string a, string b) <Global.AppendToLogFile>`
  * :ref:`ApplyDamage(handle DamageTable) <Global.ApplyDamage>`
  * :ref:`AxisAngleToQuaternion(Vector a, float b) <Global.AxisAngleToQuaternion>`
  * :ref:`CancelEntityIOEvents(ehandle a) <Global.CancelEntityIOEvents>`
  * :ref:`CreateEffect(handle a) <Global.CreateEffect>`
  * :ref:`CreateHeroForPlayer(string a, handle b) <Global.CreateHeroForPlayer>`
  * :ref:`CreateItem(string item_name, handle owner, handle owner) <Global.CreateItem>`
  * :ref:`CreateItemOnPositionSync(Vector a, handle b) <Global.CreateItemOnPositionSync>`
  * :ref:`CreateTrigger(Vector a, Vector b, Vector c) <Global.CreateTrigger>`
  * :ref:`CreateTriggerRadiusApproximate(Vector a, float b) <Global.CreateTriggerRadiusApproximate>`
  * :ref:`CreateUnitByName(string a, Vector b, bool c, handle d, handle e, int f) <Global.CreateUnitByName>`
  * :ref:`CreateUnitByNameAsync(string a, Vector b, bool c, handle d, handle e, int f, handle g) <Global.CreateUnitByNameAsync>`
  * :ref:`cvar_getf(string a) <Global.cvar_getf>`
  * :ref:`cvar_setf(string a, float b) <Global.cvar_setf>`
  * :ref:`DebugBreak() <Global.DebugBreak>`
  * :ref:`DebugDrawBox(Vector a, Vector b, Vector c, int d, int e, int f, int g, float h) <Global.DebugDrawBox>`
  * :ref:`DebugDrawBoxDirection(Vector a, Vector b, Vector c, Vector d, Vector e, float f, float g) <Global.DebugDrawBoxDirection>`
  * :ref:`DebugDrawCircle(Vector a, Vector b, float c, float d, bool e, float f) <Global.DebugDrawCircle>`
  * :ref:`DebugDrawClear() <Global.DebugDrawClear>`
  * :ref:`DebugDrawLine(Vector a, Vector b, int c, int d, int e, bool f, float g) <Global.DebugDrawLine>`
  * :ref:`DebugDrawLine_vCol(Vector a, Vector b, Vector c, bool d, float e) <Global.DebugDrawLine_vCol>`
  * :ref:`DebugDrawScreenTextLine(float a, float b, int c, string d, int e, int f, int g, int h, float i) <Global.DebugDrawScreenTextLine>`
  * :ref:`DebugDrawSphere(Vector a, Vector b, float c, float d, bool e, float f) <Global.DebugDrawSphere>`
  * :ref:`DebugDrawText(Vector a, string b, bool c, float d) <Global.DebugDrawText>`
  * :ref:`DebugScreenTextPretty(float a, float b, int c, string d, int e, int f, int g, int h, float i, string j, int k, bool l) <Global.DebugScreenTextPretty>`
  * :ref:`DoEntFire(string a, string b, string c, float d, handle e, handle f) <Global.DoEntFire>`
  * :ref:`DoEntFireByInstanceHandle(handle a, string b, string c, float d, handle e, handle f) <Global.DoEntFireByInstanceHandle>`
  * :ref:`DoIncludeScript(string a, handle b) <Global.DoIncludeScript>`
  * :ref:`DoScriptAssert(bool a, string b) <Global.DoScriptAssert>`
  * :ref:`DoUniqueString(string a) <Global.DoUniqueString>`
  * :ref:`EmitGlobalSound(string a) <Global.EmitGlobalSound>`
  * :ref:`EmitSoundOn(string a, handle b) <Global.EmitSoundOn>`
  * :ref:`EmitSoundOnClient(string a, handle b) <Global.EmitSoundOnClient>`
  * :ref:`EntIndexToHScript(int a) <Global.EntIndexToHScript>`
  * :ref:`ExecuteOrderFromTable(handle a) <Global.ExecuteOrderFromTable>`
  * :ref:`ExponentialDecay(float a, float b, float c) <Global.ExponentialDecay>`
  * :ref:`FileToString(string a) <Global.FileToString>`
  * :ref:`FindClearSpaceForUnit(handle a, Vector b, bool c) <Global.FindClearSpaceForUnit>`
  * :ref:`FindUnitsInRadius(int a, Vector b, handle c, float d, int e, int f, int g, int h, bool i) <Global.FindUnitsInRadius>`
  * :ref:`FireEntityIOInputNameOnly(ehandle a, string b) <Global.FireEntityIOInputNameOnly>`
  * :ref:`FireEntityIOInputString(ehandle a, string b, string c) <Global.FireEntityIOInputString>`
  * :ref:`FireEntityIOInputVec(ehandle a, string b, Vector c) <Global.FireEntityIOInputVec>`
  * :ref:`FireGameEvent(string eventName, handle parameterTable) <Global.FireGameEvent>`
  * :ref:`FireGameEventLocal(string a, handle b) <Global.FireGameEventLocal>`
  * :ref:`FrameTime() <Global.FrameTime>`
  * :ref:`GetFrameCount() <Global.GetFrameCount>`
  * :ref:`GetFrostyBoostAmount(int a, int b) <Global.GetFrostyBoostAmount>`
  * :ref:`GetFrostyPointsForRound(int a, int b, int c) <Global.GetFrostyPointsForRound>`
  * :ref:`GetGoldFrostyBoostAmount(int a, int b) <Global.GetGoldFrostyBoostAmount>`
  * :ref:`GetGoldFrostyPointsForRound(int a, int b, int c) <Global.GetGoldFrostyPointsForRound>`
  * :ref:`GetGroundPosition(Vector a, handle b) <Global.GetGroundPosition>`
  * :ref:`GetListenServerHost() <Global.GetListenServerHost>`
  * :ref:`GetMapName() <Global.GetMapName>`
  * :ref:`GetMaxOutputDelay(ehandle a, string b) <Global.GetMaxOutputDelay>`
  * :ref:`GetPhysAngularVelocity(handle a) <Global.GetPhysAngularVelocity>`
  * :ref:`GetPhysVelocity(handle a) <Global.GetPhysVelocity>`
  * :ref:`GetSystemDate() <Global.GetSystemDate>`
  * :ref:`GetSystemTime() <Global.GetSystemTime>`
  * :ref:`GetWorldMaxX() <Global.GetWorldMaxX>`
  * :ref:`GetWorldMaxY() <Global.GetWorldMaxY>`
  * :ref:`GetWorldMinX() <Global.GetWorldMinX>`
  * :ref:`GetWorldMinY() <Global.GetWorldMinY>`
  * :ref:`InitLogFile(string a, string b) <Global.InitLogFile>`
  * :ref:`IsDedicatedServer() <Global.IsDedicatedServer>`
  * :ref:`IsMarkedForDeletion(handle a) <Global.IsMarkedForDeletion>`
  * :ref:`IsValidEntity(handle a) <Global.IsValidEntity>`
  * :ref:`ListenToGameEvent(string EventName, handle functionNameToCall, handle context) <Global.ListenToGameEvent>`
  * :ref:`LoadKeyValues(string a) <Global.LoadKeyValues>`
  * :ref:`LoadKeyValuesFromString(string a) <Global.LoadKeyValuesFromString>`
  * :ref:`MakeStringToken(string a) <Global.MakeStringToken>`
  * :ref:`Msg(string a) <Global.Msg>`
  * :ref:`PauseGame(bool a) <Global.PauseGame>`
  * :ref:`PlayerInstanceFromIndex(int a) <Global.PlayerInstanceFromIndex>`
  * :ref:`PrecacheEntityFromTable(string a, handle b, handle c) <Global.PrecacheEntityFromTable>`
  * :ref:`PrecacheEntityListFromTable(handle a, handle b) <Global.PrecacheEntityListFromTable>`
  * :ref:`PrecacheItemByNameAsync(string a, handle b) <Global.PrecacheItemByNameAsync>`
  * :ref:`PrecacheItemByNameSync(string a, handle b) <Global.PrecacheItemByNameSync>`
  * :ref:`PrecacheModel(string a, handle b) <Global.PrecacheModel>`
  * :ref:`PrecacheResource(string a, string b, handle c) <Global.PrecacheResource>`
  * :ref:`PrecacheUnitByNameAsync(string a, handle b) <Global.PrecacheUnitByNameAsync>`
  * :ref:`PrecacheUnitByNameSync(string a, handle b) <Global.PrecacheUnitByNameSync>`
  * :ref:`PrintLinkedConsoleMessage(string a, string b) <Global.PrintLinkedConsoleMessage>`
  * :ref:`RandomFloat(float a, float b) <Global.RandomFloat>`
  * :ref:`RandomInt(int a, int b) <Global.RandomInt>`
  * :ref:`RandomVector(float a) <Global.RandomVector>`
  * :ref:`RegisterSpawnGroupFilterProxy(string a) <Global.RegisterSpawnGroupFilterProxy>`
  * :ref:`ReloadMOTD() <Global.ReloadMOTD>`
  * :ref:`RemoveSpawnGroupFilterProxy(string a) <Global.RemoveSpawnGroupFilterProxy>`
  * :ref:`RollPercentage(int a) <Global.RollPercentage>`
  * :ref:`RotateOrientation(QAngle a, QAngle b) <Global.RotateOrientation>`
  * :ref:`RotatePosition(Vector a, QAngle b, Vector c) <Global.RotatePosition>`
  * :ref:`RotateQuaternionByAxisAngle(Quaternion a, Vector b, float c) <Global.RotateQuaternionByAxisAngle>`
  * :ref:`RotationDelta(QAngle a, QAngle b) <Global.RotationDelta>`
  * :ref:`rr_AddDecisionRule(handle a) <Global.rr_AddDecisionRule>`
  * :ref:`rr_CommitAIResponse(handle a, handle b) <Global.rr_CommitAIResponse>`
  * :ref:`rr_GetResponseTargets() <Global.rr_GetResponseTargets>`
  * :ref:`rr_QueryBestResponse(handle a, handle b, handle c) <Global.rr_QueryBestResponse>`
  * :ref:`Say(handle entity, string message, bool teamOnly) <Global.Say>`
  * :ref:`ScreenShake(Vector a, float b, float c, float d, float e, int f, bool g) <Global.ScreenShake>`
  * :ref:`SendFrostivusTimeElapsedToGC() <Global.SendFrostivusTimeElapsedToGC>`
  * :ref:`SendFrostyPointsMessageToGC(handle a) <Global.SendFrostyPointsMessageToGC>`
  * :ref:`SendToConsole(string a) <Global.SendToConsole>`
  * :ref:`SendToServerConsole(string a) <Global.SendToServerConsole>`
  * :ref:`SetOpvarFloatAll(string a, string b, string c, float d) <Global.SetOpvarFloatAll>`
  * :ref:`SetOpvarFloatPlayer(string a, string b, string c, float d, handle e) <Global.SetOpvarFloatPlayer>`
  * :ref:`SetQuestName(string a) <Global.SetQuestName>`
  * :ref:`SetQuestPhase(int a) <Global.SetQuestPhase>`
  * :ref:`SetRenderingEnabled(ehandle a, bool b) <Global.SetRenderingEnabled>`
  * :ref:`ShowGenericPopup(string title, string content, string unknown, string unknown, int containerType) <Global.ShowGenericPopup>`
  * :ref:`ShowGenericPopupToPlayer(handle a, string b, string c, string d, string e, int f) <Global.ShowGenericPopupToPlayer>`
  * :ref:`ShowMessage(string a) <Global.ShowMessage>`
  * :ref:`SpawnEntityFromTableSynchronous(string a, handle b) <Global.SpawnEntityFromTableSynchronous>`
  * :ref:`SpawnEntityGroupFromTable(handle groupSpawnTables, bool bAsync, handle hCallback) <Global.SpawnEntityGroupFromTable>`
  * :ref:`SpawnEntityListFromTableAsynchronous(handle a, handle b) <Global.SpawnEntityListFromTableAsynchronous>`
  * :ref:`SpawnEntityListFromTableSynchronous(handle a) <Global.SpawnEntityListFromTableSynchronous>`
  * :ref:`SplineQuaternions(Quaternion a, Quaternion b, float c) <Global.SplineQuaternions>`
  * :ref:`SplineVectors(Vector a, Vector b, float c) <Global.SplineVectors>`
  * :ref:`StartSoundEvent(string a, handle b) <Global.StartSoundEvent>`
  * :ref:`StopEffect(handle a, string b) <Global.StopEffect>`
  * :ref:`StopListeningToAllGameEvents(handle a) <Global.StopListeningToAllGameEvents>`
  * :ref:`StopListeningToGameEvent(int a) <Global.StopListeningToGameEvent>`
  * :ref:`StopSoundEvent(string a, handle b) <Global.StopSoundEvent>`
  * :ref:`StopSoundOn(string soundName, handle playingEntity) <Global.StopSoundOn>`
  * :ref:`StringToFile(string a, string b) <Global.StringToFile>`
  * :ref:`Time() <Global.Time>`
  * :ref:`TraceCollideable(handle a) <Global.TraceCollideable>`
  * :ref:`TraceHull(handle a) <Global.TraceHull>`
  * :ref:`TraceLine(handle a) <Global.TraceLine>`
  * :ref:`UnloadSpawnGroup(string a) <Global.UnloadSpawnGroup>`
  * :ref:`UnloadSpawnGroupByHandle(int a) <Global.UnloadSpawnGroupByHandle>`
  * :ref:`UpdateEventPoints(handle a) <Global.UpdateEventPoints>`
  * :ref:`UTIL_Remove(handle a) <Global.UTIL_Remove>`
  * :ref:`UTIL_RemoveImmediate(handle a) <Global.UTIL_RemoveImmediate>`
  * :ref:`VectorToAngles(Vector a) <Global.VectorToAngles>`
  * :ref:`Warning(string a) <Global.Warning>`

CBaseEntity
############
The base class for stuff

  * :ref:`ApplyAbsVelocityImpulse(Vector a) <CBaseEntity.ApplyAbsVelocityImpulse>`
  * :ref:`ApplyLocalAngularVelocityImpulse(Vector a) <CBaseEntity.ApplyLocalAngularVelocityImpulse>`
  * :ref:`EmitSound(string soundName) <CBaseEntity.EmitSound>`
  * :ref:`EmitSoundParams(string soundName, int pitch, float volume, float soundTime) <CBaseEntity.EmitSoundParams>`
  * :ref:`EyeAngles() <CBaseEntity.EyeAngles>`
  * :ref:`EyePosition() <CBaseEntity.EyePosition>`
  * :ref:`FirstMoveChild() <CBaseEntity.FirstMoveChild>`
  * :ref:`GatherCriteria(handle a) <CBaseEntity.GatherCriteria>`
  * :ref:`GetAbsOrigin() <CBaseEntity.GetAbsOrigin>`
  * :ref:`GetAngles() <CBaseEntity.GetAngles>`
  * :ref:`GetAnglesAsVector() <CBaseEntity.GetAnglesAsVector>`
  * :ref:`GetAngularVelocity() <CBaseEntity.GetAngularVelocity>`
  * :ref:`GetBaseVelocity() <CBaseEntity.GetBaseVelocity>`
  * :ref:`GetBoundingMaxs() <CBaseEntity.GetBoundingMaxs>`
  * :ref:`GetBoundingMins() <CBaseEntity.GetBoundingMins>`
  * :ref:`GetBounds() <CBaseEntity.GetBounds>`
  * :ref:`GetCenter() <CBaseEntity.GetCenter>`
  * :ref:`GetChildren() <CBaseEntity.GetChildren>`
  * :ref:`GetContext(string a) <CBaseEntity.GetContext>`
  * :ref:`GetForwardVector() <CBaseEntity.GetForwardVector>`
  * :ref:`GetHealth() <CBaseEntity.GetHealth>`
  * :ref:`GetLocalAngularVelocity() <CBaseEntity.GetLocalAngularVelocity>`
  * :ref:`GetLocalVelocity() <CBaseEntity.GetLocalVelocity>`
  * :ref:`GetMaxHealth() <CBaseEntity.GetMaxHealth>`
  * :ref:`GetModelName() <CBaseEntity.GetModelName>`
  * :ref:`GetMoveParent() <CBaseEntity.GetMoveParent>`
  * :ref:`GetOrigin() <CBaseEntity.GetOrigin>`
  * :ref:`GetOwner() <CBaseEntity.GetOwner>`
  * :ref:`GetOwnerEntity() <CBaseEntity.GetOwnerEntity>`
  * :ref:`GetRightVector() <CBaseEntity.GetRightVector>`
  * :ref:`GetRootMoveParent() <CBaseEntity.GetRootMoveParent>`
  * :ref:`GetSoundDuration(string soundName, string actormodelname) <CBaseEntity.GetSoundDuration>`
  * :ref:`GetTeam() <CBaseEntity.GetTeam>`
  * :ref:`GetUpVector() <CBaseEntity.GetUpVector>`
  * :ref:`GetVelocity() <CBaseEntity.GetVelocity>`
  * :ref:`IsAlive() <CBaseEntity.IsAlive>`
  * :ref:`IsPlayer() <CBaseEntity.IsPlayer>`
  * :ref:`Kill() <CBaseEntity.Kill>`
  * :ref:`NextMovePeer() <CBaseEntity.NextMovePeer>`
  * :ref:`OverrideFriction(float a, float b) <CBaseEntity.OverrideFriction>`
  * :ref:`PrecacheScriptSound(string a) <CBaseEntity.PrecacheScriptSound>`
  * :ref:`SetAbsOrigin(Vector origin) <CBaseEntity.SetAbsOrigin>`
  * :ref:`SetAngles(float pitch, float yaw, float roll) <CBaseEntity.SetAngles>`
  * :ref:`SetAngularVelocity(float pitch, float yaw, float roll) <CBaseEntity.SetAngularVelocity>`
  * :ref:`SetContext(string a, string b, float c) <CBaseEntity.SetContext>`
  * :ref:`SetContextNum(string a, float b, float c) <CBaseEntity.SetContextNum>`
  * :ref:`SetContextThink(string a, handle b, float c) <CBaseEntity.SetContextThink>`
  * :ref:`SetForwardVector(Vector forwardVec) <CBaseEntity.SetForwardVector>`
  * :ref:`SetFriction(float a) <CBaseEntity.SetFriction>`
  * :ref:`SetGravity(float a) <CBaseEntity.SetGravity>`
  * :ref:`SetHealth(int hp) <CBaseEntity.SetHealth>`
  * :ref:`SetMaxHealth(int maxHP) <CBaseEntity.SetMaxHealth>`
  * :ref:`SetModel(string modelName) <CBaseEntity.SetModel>`
  * :ref:`SetOrigin(Vector origin) <CBaseEntity.SetOrigin>`
  * :ref:`SetOwner(handle owningEntity) <CBaseEntity.SetOwner>`
  * :ref:`SetParent(handle a, string b) <CBaseEntity.SetParent>`
  * :ref:`SetRenderColor(int a, int b, int c) <CBaseEntity.SetRenderColor>`
  * :ref:`SetSize(Vector a, Vector b) <CBaseEntity.SetSize>`
  * :ref:`SetTeam(int team) <CBaseEntity.SetTeam>`
  * :ref:`SetVelocity(Vector a) <CBaseEntity.SetVelocity>`
  * :ref:`StopSound(string soundName) <CBaseEntity.StopSound>`
  * :ref:`Trigger() <CBaseEntity.Trigger>`

CEntities
############
No Description Set

  * :ref:`CreateByClassname(string className) <CEntities.CreateByClassname>`
  * :ref:`FindAllByClassname(string a) <CEntities.FindAllByClassname>`
  * :ref:`FindAllByClassnameWithin(string a, Vector b, float c) <CEntities.FindAllByClassnameWithin>`
  * :ref:`FindAllByModel(string modelName) <CEntities.FindAllByModel>`
  * :ref:`FindAllByName(string name) <CEntities.FindAllByName>`
  * :ref:`FindAllByNameWithin(string name, Vector origin, float maxRadius) <CEntities.FindAllByNameWithin>`
  * :ref:`FindAllByTarget(string targetName) <CEntities.FindAllByTarget>`
  * :ref:`FindAllInSphere(Vector origin, float maxRadius) <CEntities.FindAllInSphere>`
  * :ref:`FindByClassname(handle startFrom, string className) <CEntities.FindByClassname>`
  * :ref:`FindByClassnameNearest(string className, Vector origin, float maxRadius) <CEntities.FindByClassnameNearest>`
  * :ref:`FindByClassnameWithin(handle startFrom, string className, Vector origin, float maxRadius) <CEntities.FindByClassnameWithin>`
  * :ref:`FindByModel(handle startFrom, string modelName) <CEntities.FindByModel>`
  * :ref:`FindByModelWithin(handle startFrom, string modelName, Vector origin, float maxRadius) <CEntities.FindByModelWithin>`
  * :ref:`FindByName(handle lastEnt, string searchString) <CEntities.FindByName>`
  * :ref:`FindByNameNearest(string name, Vector origin, float maxRadius) <CEntities.FindByNameNearest>`
  * :ref:`FindByNameWithin(handle startFrom, string name, Vector origin, float maxRadius) <CEntities.FindByNameWithin>`
  * :ref:`FindByTarget(handle startFrom, string targetName) <CEntities.FindByTarget>`
  * :ref:`FindInSphere(handle startFrom, Vector origin, float maxRadius) <CEntities.FindInSphere>`
  * :ref:`First() <CEntities.First>`
  * :ref:`Next(handle startFrom) <CEntities.Next>`

CEntityInstance
############
extends CBaseEntity
No Description Set

  * :ref:`ConnectOutput(string a, string b) <CEntityInstance.ConnectOutput>`
  * :ref:`Destroy() <CEntityInstance.Destroy>`
  * :ref:`DisconnectOutput(string a, string b) <CEntityInstance.DisconnectOutput>`
  * :ref:`DisconnectRedirectedOutput(string a, string b, handle c) <CEntityInstance.DisconnectRedirectedOutput>`
  * :ref:`entindex() <CEntityInstance.entindex>`
  * :ref:`FireOutput(string a, handle b, handle c, table d, float e) <CEntityInstance.FireOutput>`
  * :ref:`GetClassname() <CEntityInstance.GetClassname>`
  * :ref:`GetDebugName() <CEntityInstance.GetDebugName>`
  * :ref:`GetEntityHandle() <CEntityInstance.GetEntityHandle>`
  * :ref:`GetEntityIndex() <CEntityInstance.GetEntityIndex>`
  * :ref:`GetIntAttr(string a) <CEntityInstance.GetIntAttr>`
  * :ref:`GetName() <CEntityInstance.GetName>`
  * :ref:`GetOrCreatePrivateScriptScope() <CEntityInstance.GetOrCreatePrivateScriptScope>`
  * :ref:`GetOrCreatePublicScriptScope() <CEntityInstance.GetOrCreatePublicScriptScope>`
  * :ref:`GetPrivateScriptScope() <CEntityInstance.GetPrivateScriptScope>`
  * :ref:`GetPublicScriptScope() <CEntityInstance.GetPublicScriptScope>`
  * :ref:`RedirectOutput(string a, string b, handle c) <CEntityInstance.RedirectOutput>`
  * :ref:`RemoveSelf() <CEntityInstance.RemoveSelf>`
  * :ref:`SetIntAttr(string a, int b) <CEntityInstance.SetIntAttr>`

CDOTABaseAbility
############
extends CBaseEntity
No Description Set

  * :ref:`CastAbility() <CDOTABaseAbility.CastAbility>`
  * :ref:`ContinueCasting() <CDOTABaseAbility.ContinueCasting>`
  * :ref:`CreateVisibilityNode(Vector a, float b, float c) <CDOTABaseAbility.CreateVisibilityNode>`
  * :ref:`DecrementModifierRefCount() <CDOTABaseAbility.DecrementModifierRefCount>`
  * :ref:`EndChannel(bool a) <CDOTABaseAbility.EndChannel>`
  * :ref:`EndCooldown() <CDOTABaseAbility.EndCooldown>`
  * :ref:`GetAbilityDamage() <CDOTABaseAbility.GetAbilityDamage>`
  * :ref:`GetAbilityDamageType() <CDOTABaseAbility.GetAbilityDamageType>`
  * :ref:`GetAbilityIndex() <CDOTABaseAbility.GetAbilityIndex>`
  * :ref:`GetAbilityName() <CDOTABaseAbility.GetAbilityName>`
  * :ref:`GetAbilityTargetFlags() <CDOTABaseAbility.GetAbilityTargetFlags>`
  * :ref:`GetAbilityTargetTeam() <CDOTABaseAbility.GetAbilityTargetTeam>`
  * :ref:`GetAbilityTargetType() <CDOTABaseAbility.GetAbilityTargetType>`
  * :ref:`GetAbilityType() <CDOTABaseAbility.GetAbilityType>`
  * :ref:`GetAnimationIgnoresModelScale() <CDOTABaseAbility.GetAnimationIgnoresModelScale>`
  * :ref:`GetAssociatedPrimaryAbilities() <CDOTABaseAbility.GetAssociatedPrimaryAbilities>`
  * :ref:`GetAssociatedSecondaryAbilities() <CDOTABaseAbility.GetAssociatedSecondaryAbilities>`
  * :ref:`GetAutoCastState() <CDOTABaseAbility.GetAutoCastState>`
  * :ref:`GetBackswingTime() <CDOTABaseAbility.GetBackswingTime>`
  * :ref:`GetBehavior() <CDOTABaseAbility.GetBehavior>`
  * :ref:`GetCaster() <CDOTABaseAbility.GetCaster>`
  * :ref:`GetCastPoint() <CDOTABaseAbility.GetCastPoint>`
  * :ref:`GetCastRange() <CDOTABaseAbility.GetCastRange>`
  * :ref:`GetChannelledManaCostPerSecond(int a) <CDOTABaseAbility.GetChannelledManaCostPerSecond>`
  * :ref:`GetChannelStartTime() <CDOTABaseAbility.GetChannelStartTime>`
  * :ref:`GetChannelTime() <CDOTABaseAbility.GetChannelTime>`
  * :ref:`GetCloneSource() <CDOTABaseAbility.GetCloneSource>`
  * :ref:`GetConceptRecipientType() <CDOTABaseAbility.GetConceptRecipientType>`
  * :ref:`GetCooldown(int a) <CDOTABaseAbility.GetCooldown>`
  * :ref:`GetCooldownTime() <CDOTABaseAbility.GetCooldownTime>`
  * :ref:`GetCooldownTimeRemaining() <CDOTABaseAbility.GetCooldownTimeRemaining>`
  * :ref:`GetCursorPosition() <CDOTABaseAbility.GetCursorPosition>`
  * :ref:`GetCursorTarget() <CDOTABaseAbility.GetCursorTarget>`
  * :ref:`GetCursorTargetingNothing() <CDOTABaseAbility.GetCursorTargetingNothing>`
  * :ref:`GetDuration() <CDOTABaseAbility.GetDuration>`
  * :ref:`GetGoldCost(int a) <CDOTABaseAbility.GetGoldCost>`
  * :ref:`GetGoldCostForUpgrade(int a) <CDOTABaseAbility.GetGoldCostForUpgrade>`
  * :ref:`GetHeroLevelRequiredToUpgrade() <CDOTABaseAbility.GetHeroLevelRequiredToUpgrade>`
  * :ref:`GetIntrinsicModifierName() <CDOTABaseAbility.GetIntrinsicModifierName>`
  * :ref:`GetLevel() <CDOTABaseAbility.GetLevel>`
  * :ref:`GetLevelSpecialValueFor(string a, int b) <CDOTABaseAbility.GetLevelSpecialValueFor>`
  * :ref:`GetManaCost(int a) <CDOTABaseAbility.GetManaCost>`
  * :ref:`GetMaxLevel() <CDOTABaseAbility.GetMaxLevel>`
  * :ref:`GetModifierValue() <CDOTABaseAbility.GetModifierValue>`
  * :ref:`GetModifierValueBonus() <CDOTABaseAbility.GetModifierValueBonus>`
  * :ref:`GetPlaybackRateOverride() <CDOTABaseAbility.GetPlaybackRateOverride>`
  * :ref:`GetSharedCooldownName() <CDOTABaseAbility.GetSharedCooldownName>`
  * :ref:`GetSpecialValueFor(string a) <CDOTABaseAbility.GetSpecialValueFor>`
  * :ref:`GetStolenActivityModifier() <CDOTABaseAbility.GetStolenActivityModifier>`
  * :ref:`GetToggleState() <CDOTABaseAbility.GetToggleState>`
  * :ref:`HeroXPChange(float a) <CDOTABaseAbility.HeroXPChange>`
  * :ref:`IncrementModifierRefCount() <CDOTABaseAbility.IncrementModifierRefCount>`
  * :ref:`IsActivated() <CDOTABaseAbility.IsActivated>`
  * :ref:`IsAttributeBonus() <CDOTABaseAbility.IsAttributeBonus>`
  * :ref:`IsChanneling() <CDOTABaseAbility.IsChanneling>`
  * :ref:`IsCooldownReady() <CDOTABaseAbility.IsCooldownReady>`
  * :ref:`IsCosmetic() <CDOTABaseAbility.IsCosmetic>`
  * :ref:`IsFullyCastable() <CDOTABaseAbility.IsFullyCastable>`
  * :ref:`IsHidden() <CDOTABaseAbility.IsHidden>`
  * :ref:`IsHiddenWhenStolen() <CDOTABaseAbility.IsHiddenWhenStolen>`
  * :ref:`IsInAbilityPhase() <CDOTABaseAbility.IsInAbilityPhase>`
  * :ref:`IsItem() <CDOTABaseAbility.IsItem>`
  * :ref:`IsOwnersGoldEnough(int a) <CDOTABaseAbility.IsOwnersGoldEnough>`
  * :ref:`IsOwnersGoldEnoughForUpgrade() <CDOTABaseAbility.IsOwnersGoldEnoughForUpgrade>`
  * :ref:`IsOwnersManaEnough() <CDOTABaseAbility.IsOwnersManaEnough>`
  * :ref:`IsPassive() <CDOTABaseAbility.IsPassive>`
  * :ref:`IsSharedWithTeammates() <CDOTABaseAbility.IsSharedWithTeammates>`
  * :ref:`IsStealable() <CDOTABaseAbility.IsStealable>`
  * :ref:`IsStolen() <CDOTABaseAbility.IsStolen>`
  * :ref:`IsToggle() <CDOTABaseAbility.IsToggle>`
  * :ref:`IsTrained() <CDOTABaseAbility.IsTrained>`
  * :ref:`MarkAbilityButtonDirty() <CDOTABaseAbility.MarkAbilityButtonDirty>`
  * :ref:`NumModifiersUsingAbility() <CDOTABaseAbility.NumModifiersUsingAbility>`
  * :ref:`OnAbilityPhaseInterrupted() <CDOTABaseAbility.OnAbilityPhaseInterrupted>`
  * :ref:`OnAbilityPhaseStart() <CDOTABaseAbility.OnAbilityPhaseStart>`
  * :ref:`OnAbilityPinged() <CDOTABaseAbility.OnAbilityPinged>`
  * :ref:`OnChannelFinish(bool a) <CDOTABaseAbility.OnChannelFinish>`
  * :ref:`OnChannelThink(float a) <CDOTABaseAbility.OnChannelThink>`
  * :ref:`OnHeroCalculateStatBonus() <CDOTABaseAbility.OnHeroCalculateStatBonus>`
  * :ref:`OnHeroLevelUp() <CDOTABaseAbility.OnHeroLevelUp>`
  * :ref:`OnInventoryContentsChanged() <CDOTABaseAbility.OnInventoryContentsChanged>`
  * :ref:`OnOwnerDied() <CDOTABaseAbility.OnOwnerDied>`
  * :ref:`OnOwnerSpawned() <CDOTABaseAbility.OnOwnerSpawned>`
  * :ref:`OnSpellStart() <CDOTABaseAbility.OnSpellStart>`
  * :ref:`OnToggle() <CDOTABaseAbility.OnToggle>`
  * :ref:`OnUpgrade() <CDOTABaseAbility.OnUpgrade>`
  * :ref:`PayGoldCost() <CDOTABaseAbility.PayGoldCost>`
  * :ref:`PayGoldCostForUpgrade() <CDOTABaseAbility.PayGoldCostForUpgrade>`
  * :ref:`PayManaCost() <CDOTABaseAbility.PayManaCost>`
  * :ref:`PlaysDefaultAnimWhenStolen() <CDOTABaseAbility.PlaysDefaultAnimWhenStolen>`
  * :ref:`ProcsMagicStick() <CDOTABaseAbility.ProcsMagicStick>`
  * :ref:`RefCountsModifiers() <CDOTABaseAbility.RefCountsModifiers>`
  * :ref:`RefundManaCost() <CDOTABaseAbility.RefundManaCost>`
  * :ref:`ResetToggleOnRespawn() <CDOTABaseAbility.ResetToggleOnRespawn>`
  * :ref:`SetAbilityIndex(int a) <CDOTABaseAbility.SetAbilityIndex>`
  * :ref:`SetActivated(bool a) <CDOTABaseAbility.SetActivated>`
  * :ref:`SetChanneling(bool a) <CDOTABaseAbility.SetChanneling>`
  * :ref:`SetHidden(bool a) <CDOTABaseAbility.SetHidden>`
  * :ref:`SetInAbilityPhase(bool a) <CDOTABaseAbility.SetInAbilityPhase>`
  * :ref:`SetLevel(int a) <CDOTABaseAbility.SetLevel>`
  * :ref:`SetOverrideCastPoint(float a) <CDOTABaseAbility.SetOverrideCastPoint>`
  * :ref:`SetRefCountsModifiers(bool a) <CDOTABaseAbility.SetRefCountsModifiers>`
  * :ref:`SetStolen(bool a) <CDOTABaseAbility.SetStolen>`
  * :ref:`ShouldUseResources() <CDOTABaseAbility.ShouldUseResources>`
  * :ref:`SpeakAbilityConcept(int a) <CDOTABaseAbility.SpeakAbilityConcept>`
  * :ref:`SpeakTrigger() <CDOTABaseAbility.SpeakTrigger>`
  * :ref:`StartCooldown(float a) <CDOTABaseAbility.StartCooldown>`
  * :ref:`ToggleAbility() <CDOTABaseAbility.ToggleAbility>`
  * :ref:`ToggleAutoCast() <CDOTABaseAbility.ToggleAutoCast>`
  * :ref:`UpgradeAbility() <CDOTABaseAbility.UpgradeAbility>`
  * :ref:`UseResources(bool a, bool b, bool c) <CDOTABaseAbility.UseResources>`

CDOTA_Ability_Animation_Attack
############
extends CDOTABaseAbility
No Description Set

  * :ref:`SetPlaybackRate(float a) <CDOTA_Ability_Animation_Attack.SetPlaybackRate>`

CDOTA_Ability_Animation_TailSpin
############
extends CDOTABaseAbility
No Description Set

  * :ref:`SetPlaybackRate(float a) <CDOTA_Ability_Animation_TailSpin.SetPlaybackRate>`

CDOTA_Ability_Nian_Leap
############
extends CDOTABaseAbility
No Description Set

  * :ref:`SetPlaybackRate(float a) <CDOTA_Ability_Nian_Leap.SetPlaybackRate>`

CDOTA_Ability_Nian_Dive
############
extends CDOTABaseAbility
No Description Set

  * :ref:`SetPlaybackRate(float a) <CDOTA_Ability_Nian_Dive.SetPlaybackRate>`

CDOTA_Ability_Nian_Roar
############
extends CDOTABaseAbility
No Description Set

  * :ref:`GetCastCount() <CDOTA_Ability_Nian_Roar.GetCastCount>`

CDOTA_Item
############
extends CDOTABaseAbility
No Description Set

  * :ref:`GetContainer() <CDOTA_Item.GetContainer>`
  * :ref:`GetCost() <CDOTA_Item.GetCost>`
  * :ref:`GetCurrentCharges() <CDOTA_Item.GetCurrentCharges>`
  * :ref:`GetInitialCharges() <CDOTA_Item.GetInitialCharges>`
  * :ref:`GetPurchaser() <CDOTA_Item.GetPurchaser>`
  * :ref:`GetPurchaseTime() <CDOTA_Item.GetPurchaseTime>`
  * :ref:`GetShareability() <CDOTA_Item.GetShareability>`
  * :ref:`IsPermanent() <CDOTA_Item.IsPermanent>`
  * :ref:`LaunchLoot(bool a, float b, float c, Vector d) <CDOTA_Item.LaunchLoot>`
  * :ref:`SetCurrentCharges(int a) <CDOTA_Item.SetCurrentCharges>`
  * :ref:`SetPurchaser(handle a) <CDOTA_Item.SetPurchaser>`
  * :ref:`SetPurchaseTime(float a) <CDOTA_Item.SetPurchaseTime>`
  * :ref:`SetStacksWithOtherOwners(bool a) <CDOTA_Item.SetStacksWithOtherOwners>`
  * :ref:`StacksWithOtherOwners() <CDOTA_Item.StacksWithOtherOwners>`
  * :ref:`Think() <CDOTA_Item.Think>`

CDOTA_Item_Physical
############
extends CBaseAnimating
No Description Set

  * :ref:`GetContainedItem() <CDOTA_Item_Physical.GetContainedItem>`
  * :ref:`GetCreationTime() <CDOTA_Item_Physical.GetCreationTime>`
  * :ref:`SetContainedItem(handle a) <CDOTA_Item_Physical.SetContainedItem>`

CDOTA_Item_DataDriven
############
extends CDOTA_Item


  * :ref:`ApplyDataDrivenModifier(handle source, handle target, string modifier_name, handle modifierArgs) <CDOTA_Item_DataDriven.ApplyDataDrivenModifier>`

CDOTA_Unit_Nian
############
extends CDOTA_BaseNPC_Creature
No Description Set

  * :ref:`GetHorn() <CDOTA_Unit_Nian.GetHorn>`
  * :ref:`GetTail() <CDOTA_Unit_Nian.GetTail>`
  * :ref:`IsHornAlive() <CDOTA_Unit_Nian.IsHornAlive>`
  * :ref:`IsTailAlive() <CDOTA_Unit_Nian.IsTailAlive>`

CBasePlayer
############
No Description Set

  * :ref:`IsNoclipping() <CBasePlayer.IsNoclipping>`

CDOTAPlayer
############
extends CBaseAnimating
No Description Set

  * :ref:`GetAssignedHero() <CDOTAPlayer.GetAssignedHero>`
  * :ref:`GetControlledRPGUnit() <CDOTAPlayer.GetControlledRPGUnit>`
  * :ref:`GetPlayerID() <CDOTAPlayer.GetPlayerID>`
  * :ref:`MakeRandomHeroSelection() <CDOTAPlayer.MakeRandomHeroSelection>`
  * :ref:`SetKillCamUnit(handle a) <CDOTAPlayer.SetKillCamUnit>`
  * :ref:`SetMusicStatus(int nMusicStatus, float flIntensity) <CDOTAPlayer.SetMusicStatus>`

CDOTA_PlayerResource
############
extends CBaseEntity
No Description Set

  * :ref:`AddAegisPickup(int a) <CDOTA_PlayerResource.AddAegisPickup>`
  * :ref:`AddClaimedFarm(int a, float b) <CDOTA_PlayerResource.AddClaimedFarm>`
  * :ref:`AddGoldSpentOnSupport(int a, int b) <CDOTA_PlayerResource.AddGoldSpentOnSupport>`
  * :ref:`AddRunePickup(int a) <CDOTA_PlayerResource.AddRunePickup>`
  * :ref:`AreUnitsSharedWithPlayerID(int a, int b) <CDOTA_PlayerResource.AreUnitsSharedWithPlayerID>`
  * :ref:`ClearKillsMatrix(int a) <CDOTA_PlayerResource.ClearKillsMatrix>`
  * :ref:`ClearLastHitMultikill(int a) <CDOTA_PlayerResource.ClearLastHitMultikill>`
  * :ref:`ClearLastHitStreak(int a) <CDOTA_PlayerResource.ClearLastHitStreak>`
  * :ref:`ClearRawPlayerDamageMatrix(int a) <CDOTA_PlayerResource.ClearRawPlayerDamageMatrix>`
  * :ref:`ClearStreak(int a) <CDOTA_PlayerResource.ClearStreak>`
  * :ref:`GetAegisPickups(int a) <CDOTA_PlayerResource.GetAegisPickups>`
  * :ref:`GetAssists(int a) <CDOTA_PlayerResource.GetAssists>`
  * :ref:`GetBroadcasterChannel(int a) <CDOTA_PlayerResource.GetBroadcasterChannel>`
  * :ref:`GetBroadcasterChannelSlot(int a) <CDOTA_PlayerResource.GetBroadcasterChannelSlot>`
  * :ref:`GetClaimedDenies(int a) <CDOTA_PlayerResource.GetClaimedDenies>`
  * :ref:`GetClaimedFarm(int a) <CDOTA_PlayerResource.GetClaimedFarm>`
  * :ref:`GetClaimedMisses(int a) <CDOTA_PlayerResource.GetClaimedMisses>`
  * :ref:`GetConnectionState(int a) <CDOTA_PlayerResource.GetConnectionState>`
  * :ref:`GetCreepDamageTaken(int a) <CDOTA_PlayerResource.GetCreepDamageTaken>`
  * :ref:`GetCustomBuybackCooldown(int a) <CDOTA_PlayerResource.GetCustomBuybackCooldown>`
  * :ref:`GetCustomBuybackCost(int a) <CDOTA_PlayerResource.GetCustomBuybackCost>`
  * :ref:`GetDamageDoneToHero(int a, int b) <CDOTA_PlayerResource.GetDamageDoneToHero>`
  * :ref:`GetDeaths(int a) <CDOTA_PlayerResource.GetDeaths>`
  * :ref:`GetDenies(int a) <CDOTA_PlayerResource.GetDenies>`
  * :ref:`GetEventPointsForPlayerID(int a) <CDOTA_PlayerResource.GetEventPointsForPlayerID>`
  * :ref:`GetEventPremiumPointsGranted(int a) <CDOTA_PlayerResource.GetEventPremiumPointsGranted>`
  * :ref:`GetEventRankGranted(int a) <CDOTA_PlayerResource.GetEventRankGranted>`
  * :ref:`GetGold(int a) <CDOTA_PlayerResource.GetGold>`
  * :ref:`GetGoldBagsCollected(int a) <CDOTA_PlayerResource.GetGoldBagsCollected>`
  * :ref:`GetGoldLostToDeath(int a) <CDOTA_PlayerResource.GetGoldLostToDeath>`
  * :ref:`GetGoldPerMin(int a) <CDOTA_PlayerResource.GetGoldPerMin>`
  * :ref:`GetGoldSpentOnBuybacks(int a) <CDOTA_PlayerResource.GetGoldSpentOnBuybacks>`
  * :ref:`GetGoldSpentOnConsumables(int a) <CDOTA_PlayerResource.GetGoldSpentOnConsumables>`
  * :ref:`GetGoldSpentOnItems(int a) <CDOTA_PlayerResource.GetGoldSpentOnItems>`
  * :ref:`GetGoldSpentOnSupport(int a) <CDOTA_PlayerResource.GetGoldSpentOnSupport>`
  * :ref:`GetHealing(int a) <CDOTA_PlayerResource.GetHealing>`
  * :ref:`GetHeroDamageTaken(int a) <CDOTA_PlayerResource.GetHeroDamageTaken>`
  * :ref:`GetKills(int a) <CDOTA_PlayerResource.GetKills>`
  * :ref:`GetKillsDoneToHero(int a, int b) <CDOTA_PlayerResource.GetKillsDoneToHero>`
  * :ref:`GetLastHitMultikill(int a) <CDOTA_PlayerResource.GetLastHitMultikill>`
  * :ref:`GetLastHits(int a) <CDOTA_PlayerResource.GetLastHits>`
  * :ref:`GetLastHitStreak(int a) <CDOTA_PlayerResource.GetLastHitStreak>`
  * :ref:`GetLevel(int playerID) <CDOTA_PlayerResource.GetLevel>`
  * :ref:`GetMisses(int a) <CDOTA_PlayerResource.GetMisses>`
  * :ref:`GetNearbyCreepDeaths(int a) <CDOTA_PlayerResource.GetNearbyCreepDeaths>`
  * :ref:`GetNthCourierForTeam(int a, int b) <CDOTA_PlayerResource.GetNthCourierForTeam>`
  * :ref:`GetNthPlayerIDOnTeam(int a, int b) <CDOTA_PlayerResource.GetNthPlayerIDOnTeam>`
  * :ref:`GetNumConsumablesPurchased(int a) <CDOTA_PlayerResource.GetNumConsumablesPurchased>`
  * :ref:`GetNumCouriersForTeam(int a) <CDOTA_PlayerResource.GetNumCouriersForTeam>`
  * :ref:`GetNumItemsPurchased(int a) <CDOTA_PlayerResource.GetNumItemsPurchased>`
  * :ref:`GetPlayer(int a) <CDOTA_PlayerResource.GetPlayer>`
  * :ref:`GetPlayerLoadedCompletely(int a) <CDOTA_PlayerResource.GetPlayerLoadedCompletely>`
  * :ref:`GetPlayerName(int a) <CDOTA_PlayerResource.GetPlayerName>`
  * :ref:`GetPlayerReservedState(int a) <CDOTA_PlayerResource.GetPlayerReservedState>`
  * :ref:`GetRawPlayerDamage(int a) <CDOTA_PlayerResource.GetRawPlayerDamage>`
  * :ref:`GetReliableGold(int a) <CDOTA_PlayerResource.GetReliableGold>`
  * :ref:`GetRespawnSeconds(int a) <CDOTA_PlayerResource.GetRespawnSeconds>`
  * :ref:`GetRoshanKills(int a) <CDOTA_PlayerResource.GetRoshanKills>`
  * :ref:`GetRunePickups(int a) <CDOTA_PlayerResource.GetRunePickups>`
  * :ref:`GetSelectedHeroEntity(int a) <CDOTA_PlayerResource.GetSelectedHeroEntity>`
  * :ref:`GetSelectedHeroID(int a) <CDOTA_PlayerResource.GetSelectedHeroID>`
  * :ref:`GetSelectedHeroName(int a) <CDOTA_PlayerResource.GetSelectedHeroName>`
  * :ref:`GetSteamAccountID(int a) <CDOTA_PlayerResource.GetSteamAccountID>`
  * :ref:`GetStreak(int a) <CDOTA_PlayerResource.GetStreak>`
  * :ref:`GetStuns(int a) <CDOTA_PlayerResource.GetStuns>`
  * :ref:`GetTeam(int a) <CDOTA_PlayerResource.GetTeam>`
  * :ref:`GetTeamKills(int a) <CDOTA_PlayerResource.GetTeamKills>`
  * :ref:`GetTimeOfLastConsumablePurchase(int a) <CDOTA_PlayerResource.GetTimeOfLastConsumablePurchase>`
  * :ref:`GetTimeOfLastDeath(int a) <CDOTA_PlayerResource.GetTimeOfLastDeath>`
  * :ref:`GetTimeOfLastItemPurchase(int a) <CDOTA_PlayerResource.GetTimeOfLastItemPurchase>`
  * :ref:`GetTotalEarnedGold(int a) <CDOTA_PlayerResource.GetTotalEarnedGold>`
  * :ref:`GetTotalEarnedXP(int a) <CDOTA_PlayerResource.GetTotalEarnedXP>`
  * :ref:`GetTotalGoldSpent(int a) <CDOTA_PlayerResource.GetTotalGoldSpent>`
  * :ref:`GetTowerDamageTaken(int a) <CDOTA_PlayerResource.GetTowerDamageTaken>`
  * :ref:`GetTowerKills(int a) <CDOTA_PlayerResource.GetTowerKills>`
  * :ref:`GetUnitShareMaskForPlayer(int a, int b) <CDOTA_PlayerResource.GetUnitShareMaskForPlayer>`
  * :ref:`GetUnreliableGold(int a) <CDOTA_PlayerResource.GetUnreliableGold>`
  * :ref:`GetXPPerMin(int a) <CDOTA_PlayerResource.GetXPPerMin>`
  * :ref:`HasRandomed(int a) <CDOTA_PlayerResource.HasRandomed>`
  * :ref:`HasRepicked(int playerID) <CDOTA_PlayerResource.HasRepicked>`
  * :ref:`HasSelectedHero(int a) <CDOTA_PlayerResource.HasSelectedHero>`
  * :ref:`HaveAllPlayersJoined() <CDOTA_PlayerResource.HaveAllPlayersJoined>`
  * :ref:`HeroLevelUp(int a) <CDOTA_PlayerResource.HeroLevelUp>`
  * :ref:`IncrementAssists(int playerID) <CDOTA_PlayerResource.IncrementAssists>`
  * :ref:`IncrementClaimedDenies(int a) <CDOTA_PlayerResource.IncrementClaimedDenies>`
  * :ref:`IncrementClaimedMisses(int a) <CDOTA_PlayerResource.IncrementClaimedMisses>`
  * :ref:`IncrementDeaths(int playerID) <CDOTA_PlayerResource.IncrementDeaths>`
  * :ref:`IncrementDenies(int a) <CDOTA_PlayerResource.IncrementDenies>`
  * :ref:`IncrementGoldBagsCollected(int a) <CDOTA_PlayerResource.IncrementGoldBagsCollected>`
  * :ref:`IncrementKills(int playerID, int kills) <CDOTA_PlayerResource.IncrementKills>`
  * :ref:`IncrementLastHitMultikill(int a) <CDOTA_PlayerResource.IncrementLastHitMultikill>`
  * :ref:`IncrementLastHits(int a) <CDOTA_PlayerResource.IncrementLastHits>`
  * :ref:`IncrementLastHitStreak(int a) <CDOTA_PlayerResource.IncrementLastHitStreak>`
  * :ref:`IncrementMisses(int a) <CDOTA_PlayerResource.IncrementMisses>`
  * :ref:`IncrementNearbyCreepDeaths(int a) <CDOTA_PlayerResource.IncrementNearbyCreepDeaths>`
  * :ref:`IncrementStreak(int a) <CDOTA_PlayerResource.IncrementStreak>`
  * :ref:`IncrementTotalEarnedXP(int a, int b) <CDOTA_PlayerResource.IncrementTotalEarnedXP>`
  * :ref:`IsBroadcaster(int a) <CDOTA_PlayerResource.IsBroadcaster>`
  * :ref:`IsDisableHelpSetForPlayerID(int a, int b) <CDOTA_PlayerResource.IsDisableHelpSetForPlayerID>`
  * :ref:`IsFakeClient(int a) <CDOTA_PlayerResource.IsFakeClient>`
  * :ref:`IsHeroSelected(string a) <CDOTA_PlayerResource.IsHeroSelected>`
  * :ref:`IsHeroSharedWithPlayerID(int a, int b) <CDOTA_PlayerResource.IsHeroSharedWithPlayerID>`
  * :ref:`IsValidPlayer(int playerID) <CDOTA_PlayerResource.IsValidPlayer>`
  * :ref:`IsValidPlayerID(int playerID) <CDOTA_PlayerResource.IsValidPlayerID>`
  * :ref:`IsValidTeamPlayer(int playerID) <CDOTA_PlayerResource.IsValidTeamPlayer>`
  * :ref:`IsValidTeamPlayerID(int playerID) <CDOTA_PlayerResource.IsValidTeamPlayerID>`
  * :ref:`ModifyGold(int playerID, int goldAmmt, bool reliable, int d) <CDOTA_PlayerResource.ModifyGold>`
  * :ref:`ReplaceHeroWith(int a, string b, int c, int d) <CDOTA_PlayerResource.ReplaceHeroWith>`
  * :ref:`ResetBuybackCostTime(int a) <CDOTA_PlayerResource.ResetBuybackCostTime>`
  * :ref:`ResetTotalEarnedGold(int a) <CDOTA_PlayerResource.ResetTotalEarnedGold>`
  * :ref:`SetBuybackCooldownTime(int a, float b) <CDOTA_PlayerResource.SetBuybackCooldownTime>`
  * :ref:`SetBuybackGoldLimitTime(int a, float b) <CDOTA_PlayerResource.SetBuybackGoldLimitTime>`
  * :ref:`SetCameraTarget(int a, handle b) <CDOTA_PlayerResource.SetCameraTarget>`
  * :ref:`SetCustomBuybackCooldown(int a, float b) <CDOTA_PlayerResource.SetCustomBuybackCooldown>`
  * :ref:`SetCustomBuybackCost(int a, int b) <CDOTA_PlayerResource.SetCustomBuybackCost>`
  * :ref:`SetGold(int a, int b, bool c) <CDOTA_PlayerResource.SetGold>`
  * :ref:`SetHasRandomed(int playerID) <CDOTA_PlayerResource.SetHasRandomed>`
  * :ref:`SetHasRepicked(int playerID) <CDOTA_PlayerResource.SetHasRepicked>`
  * :ref:`SetLastBuybackTime(int a, int b) <CDOTA_PlayerResource.SetLastBuybackTime>`
  * :ref:`SetPlayerReservedState(int a, bool b) <CDOTA_PlayerResource.SetPlayerReservedState>`
  * :ref:`SetUnitShareMaskForPlayer(int a, int b, int c, bool d) <CDOTA_PlayerResource.SetUnitShareMaskForPlayer>`
  * :ref:`SpendGold(int a, int b, int c) <CDOTA_PlayerResource.SpendGold>`
  * :ref:`UpdateTeamSlot(int a, int b) <CDOTA_PlayerResource.UpdateTeamSlot>`
  * :ref:`WhoSelectedHero(string a) <CDOTA_PlayerResource.WhoSelectedHero>`

CDOTA_BaseNPC
############
extends CBaseFlex


  * :ref:`AddAbility(string a) <CDOTA_BaseNPC.AddAbility>`
  * :ref:`AddItem(handle a) <CDOTA_BaseNPC.AddItem>`
  * :ref:`AddNewModifier(handle caster, handle optionalSourceAbility, string modifierName, handle modifierData) <CDOTA_BaseNPC.AddNewModifier>`
  * :ref:`AddNoDraw() <CDOTA_BaseNPC.AddNoDraw>`
  * :ref:`AlertNearbyUnits(handle a, handle b) <CDOTA_BaseNPC.AlertNearbyUnits>`
  * :ref:`AngerNearbyUnits() <CDOTA_BaseNPC.AngerNearbyUnits>`
  * :ref:`AttackNoEarlierThan(float a) <CDOTA_BaseNPC.AttackNoEarlierThan>`
  * :ref:`AttackReady() <CDOTA_BaseNPC.AttackReady>`
  * :ref:`BoundingRadius2D() <CDOTA_BaseNPC.BoundingRadius2D>`
  * :ref:`CastAbilityImmediately(handle a, int b) <CDOTA_BaseNPC.CastAbilityImmediately>`
  * :ref:`CastAbilityNoTarget(handle ability, int playerIndex) <CDOTA_BaseNPC.CastAbilityNoTarget>`
  * :ref:`CastAbilityOnPosition(Vector a, handle b, int c) <CDOTA_BaseNPC.CastAbilityOnPosition>`
  * :ref:`CastAbilityOnTarget(handle target, handle ability, int playerIndex) <CDOTA_BaseNPC.CastAbilityOnTarget>`
  * :ref:`CastAbilityToggle(handle a, int b) <CDOTA_BaseNPC.CastAbilityToggle>`
  * :ref:`DisassembleItem(handle a) <CDOTA_BaseNPC.DisassembleItem>`
  * :ref:`DropItemAtPosition(Vector a, handle b) <CDOTA_BaseNPC.DropItemAtPosition>`
  * :ref:`DropItemAtPositionImmediate(handle a, Vector b) <CDOTA_BaseNPC.DropItemAtPositionImmediate>`
  * :ref:`EjectItemFromStash(handle a) <CDOTA_BaseNPC.EjectItemFromStash>`
  * :ref:`FindAbilityByName(string a) <CDOTA_BaseNPC.FindAbilityByName>`
  * :ref:`ForceKill(bool a) <CDOTA_BaseNPC.ForceKill>`
  * :ref:`GetAbilityByIndex(int a) <CDOTA_BaseNPC.GetAbilityByIndex>`
  * :ref:`GetAbilityCount() <CDOTA_BaseNPC.GetAbilityCount>`
  * :ref:`GetAcquisitionRange() <CDOTA_BaseNPC.GetAcquisitionRange>`
  * :ref:`GetAdditionalBattleMusicWeight() <CDOTA_BaseNPC.GetAdditionalBattleMusicWeight>`
  * :ref:`GetAttackAnimationPoint() <CDOTA_BaseNPC.GetAttackAnimationPoint>`
  * :ref:`GetAttackDamage() <CDOTA_BaseNPC.GetAttackDamage>`
  * :ref:`GetAttackRange() <CDOTA_BaseNPC.GetAttackRange>`
  * :ref:`GetAttackRangeBuffer() <CDOTA_BaseNPC.GetAttackRangeBuffer>`
  * :ref:`GetAttackSpeed() <CDOTA_BaseNPC.GetAttackSpeed>`
  * :ref:`GetAttacksPerSecond() <CDOTA_BaseNPC.GetAttacksPerSecond>`
  * :ref:`GetAttackTarget() <CDOTA_BaseNPC.GetAttackTarget>`
  * :ref:`GetAverageTrueAttackDamage() <CDOTA_BaseNPC.GetAverageTrueAttackDamage>`
  * :ref:`GetBaseAttackRange() <CDOTA_BaseNPC.GetBaseAttackRange>`
  * :ref:`GetBaseAttackTime() <CDOTA_BaseNPC.GetBaseAttackTime>`
  * :ref:`GetBaseDamageMax() <CDOTA_BaseNPC.GetBaseDamageMax>`
  * :ref:`GetBaseDamageMin() <CDOTA_BaseNPC.GetBaseDamageMin>`
  * :ref:`GetBaseDayTimeVisionRange() <CDOTA_BaseNPC.GetBaseDayTimeVisionRange>`
  * :ref:`GetBaseHealthRegen() <CDOTA_BaseNPC.GetBaseHealthRegen>`
  * :ref:`GetBaseMagicalResistanceValue() <CDOTA_BaseNPC.GetBaseMagicalResistanceValue>`
  * :ref:`GetBaseMaxHealth() <CDOTA_BaseNPC.GetBaseMaxHealth>`
  * :ref:`GetBaseMoveSpeed() <CDOTA_BaseNPC.GetBaseMoveSpeed>`
  * :ref:`GetBaseNightTimeVisionRange() <CDOTA_BaseNPC.GetBaseNightTimeVisionRange>`
  * :ref:`GetCastPoint(bool a) <CDOTA_BaseNPC.GetCastPoint>`
  * :ref:`GetCollisionPadding() <CDOTA_BaseNPC.GetCollisionPadding>`
  * :ref:`GetConstantBasedManaRegen() <CDOTA_BaseNPC.GetConstantBasedManaRegen>`
  * :ref:`GetCreationTime() <CDOTA_BaseNPC.GetCreationTime>`
  * :ref:`GetCurrentActiveAbility() <CDOTA_BaseNPC.GetCurrentActiveAbility>`
  * :ref:`GetCurrentVisionRange() <CDOTA_BaseNPC.GetCurrentVisionRange>`
  * :ref:`GetCursorCastTarget() <CDOTA_BaseNPC.GetCursorCastTarget>`
  * :ref:`GetCursorPosition() <CDOTA_BaseNPC.GetCursorPosition>`
  * :ref:`GetCursorTargetingNothing() <CDOTA_BaseNPC.GetCursorTargetingNothing>`
  * :ref:`GetDayTimeVisionRange() <CDOTA_BaseNPC.GetDayTimeVisionRange>`
  * :ref:`GetDeathXP() <CDOTA_BaseNPC.GetDeathXP>`
  * :ref:`GetForceAttackTarget() <CDOTA_BaseNPC.GetForceAttackTarget>`
  * :ref:`GetGoldBounty() <CDOTA_BaseNPC.GetGoldBounty>`
  * :ref:`GetHasteFactor() <CDOTA_BaseNPC.GetHasteFactor>`
  * :ref:`GetHealth() <CDOTA_BaseNPC.GetHealth>`
  * :ref:`GetHealthDeficit() <CDOTA_BaseNPC.GetHealthDeficit>`
  * :ref:`GetHealthPercent() <CDOTA_BaseNPC.GetHealthPercent>`
  * :ref:`GetHealthRegen() <CDOTA_BaseNPC.GetHealthRegen>`
  * :ref:`GetHullRadius() <CDOTA_BaseNPC.GetHullRadius>`
  * :ref:`GetIdealSpeed() <CDOTA_BaseNPC.GetIdealSpeed>`
  * :ref:`GetIncreasedAttackSpeed() <CDOTA_BaseNPC.GetIncreasedAttackSpeed>`
  * :ref:`GetInitialGoalEntity() <CDOTA_BaseNPC.GetInitialGoalEntity>`
  * :ref:`GetItemInSlot(int a) <CDOTA_BaseNPC.GetItemInSlot>`
  * :ref:`GetLastIdleChangeTime() <CDOTA_BaseNPC.GetLastIdleChangeTime>`
  * :ref:`GetLevel() <CDOTA_BaseNPC.GetLevel>`
  * :ref:`GetMagicalArmorValue() <CDOTA_BaseNPC.GetMagicalArmorValue>`
  * :ref:`GetMainControllingPlayer() <CDOTA_BaseNPC.GetMainControllingPlayer>`
  * :ref:`GetMana() <CDOTA_BaseNPC.GetMana>`
  * :ref:`GetManaPercent() <CDOTA_BaseNPC.GetManaPercent>`
  * :ref:`GetManaRegen() <CDOTA_BaseNPC.GetManaRegen>`
  * :ref:`GetMaxHealth() <CDOTA_BaseNPC.GetMaxHealth>`
  * :ref:`GetMaxMana() <CDOTA_BaseNPC.GetMaxMana>`
  * :ref:`GetModelRadius() <CDOTA_BaseNPC.GetModelRadius>`
  * :ref:`GetModifierCount() <CDOTA_BaseNPC.GetModifierCount>`
  * :ref:`GetModifierNameByIndex(int a) <CDOTA_BaseNPC.GetModifierNameByIndex>`
  * :ref:`GetMoveSpeedModifier(float a) <CDOTA_BaseNPC.GetMoveSpeedModifier>`
  * :ref:`GetMustReachEachGoalEntity() <CDOTA_BaseNPC.GetMustReachEachGoalEntity>`
  * :ref:`GetNightTimeVisionRange() <CDOTA_BaseNPC.GetNightTimeVisionRange>`
  * :ref:`GetOpposingTeamNumber() <CDOTA_BaseNPC.GetOpposingTeamNumber>`
  * :ref:`GetPaddedCollisionRadius() <CDOTA_BaseNPC.GetPaddedCollisionRadius>`
  * :ref:`GetPercentageBasedManaRegen() <CDOTA_BaseNPC.GetPercentageBasedManaRegen>`
  * :ref:`GetPhysicalArmorBaseValue() <CDOTA_BaseNPC.GetPhysicalArmorBaseValue>`
  * :ref:`GetPhysicalArmorValue() <CDOTA_BaseNPC.GetPhysicalArmorValue>`
  * :ref:`GetPlayerOwner() <CDOTA_BaseNPC.GetPlayerOwner>`
  * :ref:`GetPlayerOwnerID() <CDOTA_BaseNPC.GetPlayerOwnerID>`
  * :ref:`GetProjectileSpeed() <CDOTA_BaseNPC.GetProjectileSpeed>`
  * :ref:`GetRangeToUnit(handle a) <CDOTA_BaseNPC.GetRangeToUnit>`
  * :ref:`GetSecondsPerAttack() <CDOTA_BaseNPC.GetSecondsPerAttack>`
  * :ref:`GetStatsBasedManaRegen() <CDOTA_BaseNPC.GetStatsBasedManaRegen>`
  * :ref:`GetTeamNumber() <CDOTA_BaseNPC.GetTeamNumber>`
  * :ref:`GetTotalPurchasedUpgradeGoldCost() <CDOTA_BaseNPC.GetTotalPurchasedUpgradeGoldCost>`
  * :ref:`GetUnitLabel() <CDOTA_BaseNPC.GetUnitLabel>`
  * :ref:`GetUnitName() <CDOTA_BaseNPC.GetUnitName>`
  * :ref:`GiveMana(float a) <CDOTA_BaseNPC.GiveMana>`
  * :ref:`HasAbility(string a) <CDOTA_BaseNPC.HasAbility>`
  * :ref:`HasAttackCapability() <CDOTA_BaseNPC.HasAttackCapability>`
  * :ref:`HasFlyingVision() <CDOTA_BaseNPC.HasFlyingVision>`
  * :ref:`HasFlyMovementCapability() <CDOTA_BaseNPC.HasFlyMovementCapability>`
  * :ref:`HasGroundMovementCapability() <CDOTA_BaseNPC.HasGroundMovementCapability>`
  * :ref:`HasInventory() <CDOTA_BaseNPC.HasInventory>`
  * :ref:`HasItemInInventory(string a) <CDOTA_BaseNPC.HasItemInInventory>`
  * :ref:`HasModifier(string a) <CDOTA_BaseNPC.HasModifier>`
  * :ref:`HasMovementCapability() <CDOTA_BaseNPC.HasMovementCapability>`
  * :ref:`HasScepter() <CDOTA_BaseNPC.HasScepter>`
  * :ref:`Heal(float a, handle b) <CDOTA_BaseNPC.Heal>`
  * :ref:`Hold() <CDOTA_BaseNPC.Hold>`
  * :ref:`Interrupt() <CDOTA_BaseNPC.Interrupt>`
  * :ref:`InterruptChannel() <CDOTA_BaseNPC.InterruptChannel>`
  * :ref:`InterruptMotionControllers(bool a) <CDOTA_BaseNPC.InterruptMotionControllers>`
  * :ref:`IsAlive() <CDOTA_BaseNPC.IsAlive>`
  * :ref:`IsAncient() <CDOTA_BaseNPC.IsAncient>`
  * :ref:`IsAttackImmune() <CDOTA_BaseNPC.IsAttackImmune>`
  * :ref:`IsAttacking() <CDOTA_BaseNPC.IsAttacking>`
  * :ref:`IsAttackingEntity(handle a) <CDOTA_BaseNPC.IsAttackingEntity>`
  * :ref:`IsBlind() <CDOTA_BaseNPC.IsBlind>`
  * :ref:`IsBlockDisabled() <CDOTA_BaseNPC.IsBlockDisabled>`
  * :ref:`IsCommandRestricted() <CDOTA_BaseNPC.IsCommandRestricted>`
  * :ref:`IsControllableByAnyPlayer() <CDOTA_BaseNPC.IsControllableByAnyPlayer>`
  * :ref:`IsCreature() <CDOTA_BaseNPC.IsCreature>`
  * :ref:`IsDeniable() <CDOTA_BaseNPC.IsDeniable>`
  * :ref:`IsDisarmed() <CDOTA_BaseNPC.IsDisarmed>`
  * :ref:`IsDominated() <CDOTA_BaseNPC.IsDominated>`
  * :ref:`IsEvadeDisabled() <CDOTA_BaseNPC.IsEvadeDisabled>`
  * :ref:`IsFrozen() <CDOTA_BaseNPC.IsFrozen>`
  * :ref:`IsHardDisarmed() <CDOTA_BaseNPC.IsHardDisarmed>`
  * :ref:`IsHero() <CDOTA_BaseNPC.IsHero>`
  * :ref:`IsHexed() <CDOTA_BaseNPC.IsHexed>`
  * :ref:`IsIdle() <CDOTA_BaseNPC.IsIdle>`
  * :ref:`IsIllusion() <CDOTA_BaseNPC.IsIllusion>`
  * :ref:`IsInvisible() <CDOTA_BaseNPC.IsInvisible>`
  * :ref:`IsInvulnerable() <CDOTA_BaseNPC.IsInvulnerable>`
  * :ref:`IsLowAttackPriority() <CDOTA_BaseNPC.IsLowAttackPriority>`
  * :ref:`IsMagicImmune() <CDOTA_BaseNPC.IsMagicImmune>`
  * :ref:`IsMechanical() <CDOTA_BaseNPC.IsMechanical>`
  * :ref:`IsMovementImpaired() <CDOTA_BaseNPC.IsMovementImpaired>`
  * :ref:`IsMuted() <CDOTA_BaseNPC.IsMuted>`
  * :ref:`IsNeutralUnitType() <CDOTA_BaseNPC.IsNeutralUnitType>`
  * :ref:`IsNightmared() <CDOTA_BaseNPC.IsNightmared>`
  * :ref:`IsOpposingTeam(int a) <CDOTA_BaseNPC.IsOpposingTeam>`
  * :ref:`IsOutOfGame() <CDOTA_BaseNPC.IsOutOfGame>`
  * :ref:`IsOwnedByAnyPlayer() <CDOTA_BaseNPC.IsOwnedByAnyPlayer>`
  * :ref:`IsPhantom() <CDOTA_BaseNPC.IsPhantom>`
  * :ref:`IsPhantomBlocker() <CDOTA_BaseNPC.IsPhantomBlocker>`
  * :ref:`IsPhased() <CDOTA_BaseNPC.IsPhased>`
  * :ref:`IsPositionInRange(Vector a, float b) <CDOTA_BaseNPC.IsPositionInRange>`
  * :ref:`IsRangedAttacker() <CDOTA_BaseNPC.IsRangedAttacker>`
  * :ref:`IsRealHero() <CDOTA_BaseNPC.IsRealHero>`
  * :ref:`IsRooted() <CDOTA_BaseNPC.IsRooted>`
  * :ref:`IsSilenced() <CDOTA_BaseNPC.IsSilenced>`
  * :ref:`IsSoftDisarmed() <CDOTA_BaseNPC.IsSoftDisarmed>`
  * :ref:`IsSpeciallyDeniable() <CDOTA_BaseNPC.IsSpeciallyDeniable>`
  * :ref:`IsStunned() <CDOTA_BaseNPC.IsStunned>`
  * :ref:`IsSummoned() <CDOTA_BaseNPC.IsSummoned>`
  * :ref:`IsTower() <CDOTA_BaseNPC.IsTower>`
  * :ref:`IsUnableToMiss() <CDOTA_BaseNPC.IsUnableToMiss>`
  * :ref:`IsUnselectable() <CDOTA_BaseNPC.IsUnselectable>`
  * :ref:`Kill(handle a, handle b) <CDOTA_BaseNPC.Kill>`
  * :ref:`MakeIllusion() <CDOTA_BaseNPC.MakeIllusion>`
  * :ref:`MakePhantomBlocker() <CDOTA_BaseNPC.MakePhantomBlocker>`
  * :ref:`MakeVisibleDueToAttack(int a) <CDOTA_BaseNPC.MakeVisibleDueToAttack>`
  * :ref:`MakeVisibleToTeam(int a, float b) <CDOTA_BaseNPC.MakeVisibleToTeam>`
  * :ref:`ModifyHealth(int a, handle b, bool c, int d) <CDOTA_BaseNPC.ModifyHealth>`
  * :ref:`MoveToNPC(handle a) <CDOTA_BaseNPC.MoveToNPC>`
  * :ref:`MoveToNPCToGiveItem(handle a, handle b) <CDOTA_BaseNPC.MoveToNPCToGiveItem>`
  * :ref:`MoveToPosition(Vector a) <CDOTA_BaseNPC.MoveToPosition>`
  * :ref:`MoveToPositionAggressive(Vector a) <CDOTA_BaseNPC.MoveToPositionAggressive>`
  * :ref:`MoveToTargetToAttack(handle a) <CDOTA_BaseNPC.MoveToTargetToAttack>`
  * :ref:`NoHealthBar() <CDOTA_BaseNPC.NoHealthBar>`
  * :ref:`NoTeamMoveTo() <CDOTA_BaseNPC.NoTeamMoveTo>`
  * :ref:`NoTeamSelect() <CDOTA_BaseNPC.NoTeamSelect>`
  * :ref:`NotOnMinimap() <CDOTA_BaseNPC.NotOnMinimap>`
  * :ref:`NotOnMinimapForEnemies() <CDOTA_BaseNPC.NotOnMinimapForEnemies>`
  * :ref:`NoUnitCollision() <CDOTA_BaseNPC.NoUnitCollision>`
  * :ref:`PassivesDisabled() <CDOTA_BaseNPC.PassivesDisabled>`
  * :ref:`PerformAttack(handle a, bool b, bool c, bool d, bool e) <CDOTA_BaseNPC.PerformAttack>`
  * :ref:`PickupDroppedItem(handle a) <CDOTA_BaseNPC.PickupDroppedItem>`
  * :ref:`PickupRune(handle a) <CDOTA_BaseNPC.PickupRune>`
  * :ref:`ProvidesVision() <CDOTA_BaseNPC.ProvidesVision>`
  * :ref:`ReduceMana(float a) <CDOTA_BaseNPC.ReduceMana>`
  * :ref:`RemoveAbility(string a) <CDOTA_BaseNPC.RemoveAbility>`
  * :ref:`RemoveItem(handle a) <CDOTA_BaseNPC.RemoveItem>`
  * :ref:`RemoveModifierByName(string a) <CDOTA_BaseNPC.RemoveModifierByName>`
  * :ref:`RemoveModifierByNameAndCaster(string a, handle b) <CDOTA_BaseNPC.RemoveModifierByNameAndCaster>`
  * :ref:`RemoveNoDraw() <CDOTA_BaseNPC.RemoveNoDraw>`
  * :ref:`RespawnUnit() <CDOTA_BaseNPC.RespawnUnit>`
  * :ref:`SellItem(handle a) <CDOTA_BaseNPC.SellItem>`
  * :ref:`SetAdditionalBattleMusicWeight(float a) <CDOTA_BaseNPC.SetAdditionalBattleMusicWeight>`
  * :ref:`SetAttackCapability(int a) <CDOTA_BaseNPC.SetAttackCapability>`
  * :ref:`SetAttacking(handle a) <CDOTA_BaseNPC.SetAttacking>`
  * :ref:`SetBaseAttackTime(float a) <CDOTA_BaseNPC.SetBaseAttackTime>`
  * :ref:`SetBaseDamageMax(int a) <CDOTA_BaseNPC.SetBaseDamageMax>`
  * :ref:`SetBaseDamageMin(int a) <CDOTA_BaseNPC.SetBaseDamageMin>`
  * :ref:`SetBaseHealthRegen(float a) <CDOTA_BaseNPC.SetBaseHealthRegen>`
  * :ref:`SetBaseMagicalResistanceValue(float a) <CDOTA_BaseNPC.SetBaseMagicalResistanceValue>`
  * :ref:`SetBaseManaRegen(float a) <CDOTA_BaseNPC.SetBaseManaRegen>`
  * :ref:`SetBaseMaxHealth(float a) <CDOTA_BaseNPC.SetBaseMaxHealth>`
  * :ref:`SetBaseMoveSpeed(int a) <CDOTA_BaseNPC.SetBaseMoveSpeed>`
  * :ref:`SetControllableByPlayer(int a, bool b) <CDOTA_BaseNPC.SetControllableByPlayer>`
  * :ref:`SetCursorCastTarget(handle a) <CDOTA_BaseNPC.SetCursorCastTarget>`
  * :ref:`SetCursorPosition(Vector a) <CDOTA_BaseNPC.SetCursorPosition>`
  * :ref:`SetCursorTargetingNothing(bool a) <CDOTA_BaseNPC.SetCursorTargetingNothing>`
  * :ref:`SetDayTimeVisionRange(int a) <CDOTA_BaseNPC.SetDayTimeVisionRange>`
  * :ref:`SetDeathXP(int a) <CDOTA_BaseNPC.SetDeathXP>`
  * :ref:`SetForceAttackTarget(handle a) <CDOTA_BaseNPC.SetForceAttackTarget>`
  * :ref:`SetHasInventory(bool a) <CDOTA_BaseNPC.SetHasInventory>`
  * :ref:`SetHullRadius(float a) <CDOTA_BaseNPC.SetHullRadius>`
  * :ref:`SetIdleAcquire(bool a) <CDOTA_BaseNPC.SetIdleAcquire>`
  * :ref:`SetInitialGoalEntity(handle a) <CDOTA_BaseNPC.SetInitialGoalEntity>`
  * :ref:`SetMana(float a) <CDOTA_BaseNPC.SetMana>`
  * :ref:`SetMaximumGoldBounty(int a) <CDOTA_BaseNPC.SetMaximumGoldBounty>`
  * :ref:`SetMinimumGoldBounty(int a) <CDOTA_BaseNPC.SetMinimumGoldBounty>`
  * :ref:`SetMoveCapability(int a) <CDOTA_BaseNPC.SetMoveCapability>`
  * :ref:`SetMustReachEachGoalEntity(bool a) <CDOTA_BaseNPC.SetMustReachEachGoalEntity>`
  * :ref:`SetNeverMoveToClearSpace(bool a) <CDOTA_BaseNPC.SetNeverMoveToClearSpace>`
  * :ref:`SetNightTimeVisionRange(int a) <CDOTA_BaseNPC.SetNightTimeVisionRange>`
  * :ref:`SetOriginalModel(string originalModel) <CDOTA_BaseNPC.SetOriginalModel>`
  * :ref:`SetPhysicalArmorBaseValue(float a) <CDOTA_BaseNPC.SetPhysicalArmorBaseValue>`
  * :ref:`SetRangedProjectileName(string a) <CDOTA_BaseNPC.SetRangedProjectileName>`
  * :ref:`SetStolenScepter(bool a) <CDOTA_BaseNPC.SetStolenScepter>`
  * :ref:`SetUnitName(string a) <CDOTA_BaseNPC.SetUnitName>`
  * :ref:`ShouldIdleAcquire() <CDOTA_BaseNPC.ShouldIdleAcquire>`
  * :ref:`SpendMana(float a, handle b) <CDOTA_BaseNPC.SpendMana>`
  * :ref:`Stop() <CDOTA_BaseNPC.Stop>`
  * :ref:`SwapAbilities(string a, string b, bool c, bool d) <CDOTA_BaseNPC.SwapAbilities>`
  * :ref:`TimeUntilNextAttack() <CDOTA_BaseNPC.TimeUntilNextAttack>`
  * :ref:`TriggerModifierDodge() <CDOTA_BaseNPC.TriggerModifierDodge>`
  * :ref:`TriggerSpellAbsorb(handle a) <CDOTA_BaseNPC.TriggerSpellAbsorb>`
  * :ref:`UnitCanRespawn() <CDOTA_BaseNPC.UnitCanRespawn>`

CDOTA_BaseNPC_Hero
############
extends CDOTA_BaseNPC


  * :ref:`AddExperience(float amount, bool applyBotDifficultyScaling) <CDOTA_BaseNPC_Hero.AddExperience>`
  * :ref:`Buyback() <CDOTA_BaseNPC_Hero.Buyback>`
  * :ref:`CalculateStatBonus() <CDOTA_BaseNPC_Hero.CalculateStatBonus>`
  * :ref:`CanEarnGold() <CDOTA_BaseNPC_Hero.CanEarnGold>`
  * :ref:`ClearLastHitMultikill() <CDOTA_BaseNPC_Hero.ClearLastHitMultikill>`
  * :ref:`ClearLastHitStreak() <CDOTA_BaseNPC_Hero.ClearLastHitStreak>`
  * :ref:`ClearStreak() <CDOTA_BaseNPC_Hero.ClearStreak>`
  * :ref:`GetAbilityPoints() <CDOTA_BaseNPC_Hero.GetAbilityPoints>`
  * :ref:`GetAgility() <CDOTA_BaseNPC_Hero.GetAgility>`
  * :ref:`GetAgilityGain() <CDOTA_BaseNPC_Hero.GetAgilityGain>`
  * :ref:`GetAssists() <CDOTA_BaseNPC_Hero.GetAssists>`
  * :ref:`GetAttacker(int a) <CDOTA_BaseNPC_Hero.GetAttacker>`
  * :ref:`GetBaseAgility() <CDOTA_BaseNPC_Hero.GetBaseAgility>`
  * :ref:`GetBaseDamageMax() <CDOTA_BaseNPC_Hero.GetBaseDamageMax>`
  * :ref:`GetBaseDamageMin() <CDOTA_BaseNPC_Hero.GetBaseDamageMin>`
  * :ref:`GetBaseIntellect() <CDOTA_BaseNPC_Hero.GetBaseIntellect>`
  * :ref:`GetBaseStrength() <CDOTA_BaseNPC_Hero.GetBaseStrength>`
  * :ref:`GetBonusDamageFromPrimaryStat() <CDOTA_BaseNPC_Hero.GetBonusDamageFromPrimaryStat>`
  * :ref:`GetBuybackCooldownTime() <CDOTA_BaseNPC_Hero.GetBuybackCooldownTime>`
  * :ref:`GetBuybackCost() <CDOTA_BaseNPC_Hero.GetBuybackCost>`
  * :ref:`GetBuybackGoldLimitTime() <CDOTA_BaseNPC_Hero.GetBuybackGoldLimitTime>`
  * :ref:`GetCurrentXP() <CDOTA_BaseNPC_Hero.GetCurrentXP>`
  * :ref:`GetDeathGoldCost() <CDOTA_BaseNPC_Hero.GetDeathGoldCost>`
  * :ref:`GetDeaths() <CDOTA_BaseNPC_Hero.GetDeaths>`
  * :ref:`GetDenies() <CDOTA_BaseNPC_Hero.GetDenies>`
  * :ref:`GetGold() <CDOTA_BaseNPC_Hero.GetGold>`
  * :ref:`GetGoldBounty() <CDOTA_BaseNPC_Hero.GetGoldBounty>`
  * :ref:`GetHealthRegen() <CDOTA_BaseNPC_Hero.GetHealthRegen>`
  * :ref:`GetIncreasedAttackSpeed() <CDOTA_BaseNPC_Hero.GetIncreasedAttackSpeed>`
  * :ref:`GetIntellect() <CDOTA_BaseNPC_Hero.GetIntellect>`
  * :ref:`GetIntellectGain() <CDOTA_BaseNPC_Hero.GetIntellectGain>`
  * :ref:`GetKills() <CDOTA_BaseNPC_Hero.GetKills>`
  * :ref:`GetLastHits() <CDOTA_BaseNPC_Hero.GetLastHits>`
  * :ref:`GetManaRegen() <CDOTA_BaseNPC_Hero.GetManaRegen>`
  * :ref:`GetMostRecentDamageTime() <CDOTA_BaseNPC_Hero.GetMostRecentDamageTime>`
  * :ref:`GetMultipleKillCount() <CDOTA_BaseNPC_Hero.GetMultipleKillCount>`
  * :ref:`GetNumAttackers() <CDOTA_BaseNPC_Hero.GetNumAttackers>`
  * :ref:`GetPhysicalArmorValue() <CDOTA_BaseNPC_Hero.GetPhysicalArmorValue>`
  * :ref:`GetPlayerID() <CDOTA_BaseNPC_Hero.GetPlayerID>`
  * :ref:`GetPrimaryAttribute() <CDOTA_BaseNPC_Hero.GetPrimaryAttribute>`
  * :ref:`GetPrimaryStatValue() <CDOTA_BaseNPC_Hero.GetPrimaryStatValue>`
  * :ref:`GetRespawnTime() <CDOTA_BaseNPC_Hero.GetRespawnTime>`
  * :ref:`GetStatsBasedManaRegen() <CDOTA_BaseNPC_Hero.GetStatsBasedManaRegen>`
  * :ref:`GetStreak() <CDOTA_BaseNPC_Hero.GetStreak>`
  * :ref:`GetStrength() <CDOTA_BaseNPC_Hero.GetStrength>`
  * :ref:`GetStrengthGain() <CDOTA_BaseNPC_Hero.GetStrengthGain>`
  * :ref:`GetTimeUntilRespawn() <CDOTA_BaseNPC_Hero.GetTimeUntilRespawn>`
  * :ref:`HasAnyAvailableInventorySpace() <CDOTA_BaseNPC_Hero.HasAnyAvailableInventorySpace>`
  * :ref:`HasFlyingVision() <CDOTA_BaseNPC_Hero.HasFlyingVision>`
  * :ref:`HasOwnerAbandoned() <CDOTA_BaseNPC_Hero.HasOwnerAbandoned>`
  * :ref:`HasRoomForItem(string a, bool b, bool c) <CDOTA_BaseNPC_Hero.HasRoomForItem>`
  * :ref:`HeroLevelUp(bool a) <CDOTA_BaseNPC_Hero.HeroLevelUp>`
  * :ref:`IncrementAssists() <CDOTA_BaseNPC_Hero.IncrementAssists>`
  * :ref:`IncrementDeaths() <CDOTA_BaseNPC_Hero.IncrementDeaths>`
  * :ref:`IncrementDenies() <CDOTA_BaseNPC_Hero.IncrementDenies>`
  * :ref:`IncrementKills(int kills) <CDOTA_BaseNPC_Hero.IncrementKills>`
  * :ref:`IncrementLastHitMultikill() <CDOTA_BaseNPC_Hero.IncrementLastHitMultikill>`
  * :ref:`IncrementLastHits() <CDOTA_BaseNPC_Hero.IncrementLastHits>`
  * :ref:`IncrementLastHitStreak() <CDOTA_BaseNPC_Hero.IncrementLastHitStreak>`
  * :ref:`IncrementNearbyCreepDeaths() <CDOTA_BaseNPC_Hero.IncrementNearbyCreepDeaths>`
  * :ref:`IncrementStreak() <CDOTA_BaseNPC_Hero.IncrementStreak>`
  * :ref:`IsBuybackDisabledByReapersScythe() <CDOTA_BaseNPC_Hero.IsBuybackDisabledByReapersScythe>`
  * :ref:`IsReincarnating() <CDOTA_BaseNPC_Hero.IsReincarnating>`
  * :ref:`KilledHero(handle a, handle b) <CDOTA_BaseNPC_Hero.KilledHero>`
  * :ref:`ModifyAgility(float a) <CDOTA_BaseNPC_Hero.ModifyAgility>`
  * :ref:`ModifyGold(int goldAmmt, bool reliable, int reason) <CDOTA_BaseNPC_Hero.ModifyGold>`
  * :ref:`ModifyIntellect(float a) <CDOTA_BaseNPC_Hero.ModifyIntellect>`
  * :ref:`ModifyStrength(float a) <CDOTA_BaseNPC_Hero.ModifyStrength>`
  * :ref:`PerformTaunt() <CDOTA_BaseNPC_Hero.PerformTaunt>`
  * :ref:`RecordLastHit() <CDOTA_BaseNPC_Hero.RecordLastHit>`
  * :ref:`RespawnHero(bool buyback, bool unknown1, bool unknown2) <CDOTA_BaseNPC_Hero.RespawnHero>`
  * :ref:`SetAbilityPoints(int a) <CDOTA_BaseNPC_Hero.SetAbilityPoints>`
  * :ref:`SetBaseAgility(float a) <CDOTA_BaseNPC_Hero.SetBaseAgility>`
  * :ref:`SetBaseIntellect(float a) <CDOTA_BaseNPC_Hero.SetBaseIntellect>`
  * :ref:`SetBaseStrength(float a) <CDOTA_BaseNPC_Hero.SetBaseStrength>`
  * :ref:`SetBuybackCooldownTime(float a) <CDOTA_BaseNPC_Hero.SetBuybackCooldownTime>`
  * :ref:`SetBuyBackDisabledByReapersScythe(bool a) <CDOTA_BaseNPC_Hero.SetBuyBackDisabledByReapersScythe>`
  * :ref:`SetBuybackGoldLimitTime(float a) <CDOTA_BaseNPC_Hero.SetBuybackGoldLimitTime>`
  * :ref:`SetCustomDeathXP(int a) <CDOTA_BaseNPC_Hero.SetCustomDeathXP>`
  * :ref:`SetGold(int a, bool b) <CDOTA_BaseNPC_Hero.SetGold>`
  * :ref:`SetPlayerID(int a) <CDOTA_BaseNPC_Hero.SetPlayerID>`
  * :ref:`SetRespawnPosition(Vector a) <CDOTA_BaseNPC_Hero.SetRespawnPosition>`
  * :ref:`SetTimeUntilRespawn(float a) <CDOTA_BaseNPC_Hero.SetTimeUntilRespawn>`
  * :ref:`ShouldDoFlyHeightVisual() <CDOTA_BaseNPC_Hero.ShouldDoFlyHeightVisual>`
  * :ref:`SpendGold(int a, int b) <CDOTA_BaseNPC_Hero.SpendGold>`
  * :ref:`UnitCanRespawn() <CDOTA_BaseNPC_Hero.UnitCanRespawn>`
  * :ref:`UpgradeAbility(handle a) <CDOTA_BaseNPC_Hero.UpgradeAbility>`
  * :ref:`WillReincarnate() <CDOTA_BaseNPC_Hero.WillReincarnate>`

CDOTA_BaseNPC_Creature
############
extends CDOTA_BaseNPC
No Description Set

  * :ref:`AddItemDrop(handle a) <CDOTA_BaseNPC_Creature.AddItemDrop>`
  * :ref:`CreatureLevelUp(int a) <CDOTA_BaseNPC_Creature.CreatureLevelUp>`
  * :ref:`IsChampion() <CDOTA_BaseNPC_Creature.IsChampion>`
  * :ref:`SetArmorGain(float a) <CDOTA_BaseNPC_Creature.SetArmorGain>`
  * :ref:`SetAttackTimeGain(float a) <CDOTA_BaseNPC_Creature.SetAttackTimeGain>`
  * :ref:`SetBountyGain(int a) <CDOTA_BaseNPC_Creature.SetBountyGain>`
  * :ref:`SetChampion(bool a) <CDOTA_BaseNPC_Creature.SetChampion>`
  * :ref:`SetDamageGain(int a) <CDOTA_BaseNPC_Creature.SetDamageGain>`
  * :ref:`SetDisableResistanceGain(float a) <CDOTA_BaseNPC_Creature.SetDisableResistanceGain>`
  * :ref:`SetHPGain(int a) <CDOTA_BaseNPC_Creature.SetHPGain>`
  * :ref:`SetHPRegenGain(float a) <CDOTA_BaseNPC_Creature.SetHPRegenGain>`
  * :ref:`SetMagicResistanceGain(float a) <CDOTA_BaseNPC_Creature.SetMagicResistanceGain>`
  * :ref:`SetManaGain(int a) <CDOTA_BaseNPC_Creature.SetManaGain>`
  * :ref:`SetManaRegenGain(float a) <CDOTA_BaseNPC_Creature.SetManaRegenGain>`
  * :ref:`SetMoveSpeedGain(int a) <CDOTA_BaseNPC_Creature.SetMoveSpeedGain>`
  * :ref:`SetXPGain(int a) <CDOTA_BaseNPC_Creature.SetXPGain>`

CDOTA_BaseNPC_Building
############
extends CDOTA_BaseNPC
No Description Set

  * :ref:`GetInvulnCount() <CDOTA_BaseNPC_Building.GetInvulnCount>`
  * :ref:`SetInvulnCount(int a) <CDOTA_BaseNPC_Building.SetInvulnCount>`

CRPG_Unit
############
No Description Set

  * :ref:`ActionState() <CRPG_Unit.ActionState>`
  * :ref:`ClearMovementTarget() <CRPG_Unit.ClearMovementTarget>`
  * :ref:`FindSensedEnemies() <CRPG_Unit.FindSensedEnemies>`
  * :ref:`GetMaxSpeed() <CRPG_Unit.GetMaxSpeed>`
  * :ref:`GetMaxStamina() <CRPG_Unit.GetMaxStamina>`
  * :ref:`GetMovementTargetEntity() <CRPG_Unit.GetMovementTargetEntity>`
  * :ref:`GetSensingSphereRange() <CRPG_Unit.GetSensingSphereRange>`
  * :ref:`GetSightConeAngle() <CRPG_Unit.GetSightConeAngle>`
  * :ref:`GetSightConeRange() <CRPG_Unit.GetSightConeRange>`
  * :ref:`GetStamina() <CRPG_Unit.GetStamina>`
  * :ref:`GetTurnRate() <CRPG_Unit.GetTurnRate>`
  * :ref:`GetUnitName() <CRPG_Unit.GetUnitName>`
  * :ref:`GrantItem(string a, bool b) <CRPG_Unit.GrantItem>`
  * :ref:`IsBlocking() <CRPG_Unit.IsBlocking>`
  * :ref:`IsFacing(Vector a, float b) <CRPG_Unit.IsFacing>`
  * :ref:`SetBlocking(bool a) <CRPG_Unit.SetBlocking>`
  * :ref:`SetMaxSpeed(float a) <CRPG_Unit.SetMaxSpeed>`
  * :ref:`SetMovementTargetEntity(handle a, float b) <CRPG_Unit.SetMovementTargetEntity>`
  * :ref:`SetMovementTargetPosition(Vector a, float b) <CRPG_Unit.SetMovementTargetPosition>`
  * :ref:`SetSensingSphereRange(float a) <CRPG_Unit.SetSensingSphereRange>`
  * :ref:`SetSightConeAngle(float a) <CRPG_Unit.SetSightConeAngle>`
  * :ref:`SetSightConeRange(float a) <CRPG_Unit.SetSightConeRange>`
  * :ref:`SetTurnRate(float a) <CRPG_Unit.SetTurnRate>`

CDOTABaseGameMode
############
extends CBaseEntity
No Description Set

  * :ref:`ClientLoadGridNav() <CDOTABaseGameMode.ClientLoadGridNav>`
  * :ref:`SetAlwaysShowPlayerInventory(bool a) <CDOTABaseGameMode.SetAlwaysShowPlayerInventory>`
  * :ref:`SetBotThinkingEnabled(bool a) <CDOTABaseGameMode.SetBotThinkingEnabled>`
  * :ref:`SetBuybackEnabled(bool a) <CDOTABaseGameMode.SetBuybackEnabled>`
  * :ref:`SetCameraDistanceOverride(float a) <CDOTABaseGameMode.SetCameraDistanceOverride>`
  * :ref:`SetCustomBuybackCooldownEnabled(bool a) <CDOTABaseGameMode.SetCustomBuybackCooldownEnabled>`
  * :ref:`SetCustomBuybackCostEnabled(bool a) <CDOTABaseGameMode.SetCustomBuybackCostEnabled>`
  * :ref:`SetCustomHeroMaxLevel(int maxLevel) <CDOTABaseGameMode.SetCustomHeroMaxLevel>`
  * :ref:`SetCustomXPRequiredToReachNextLevel(handle a) <CDOTABaseGameMode.SetCustomXPRequiredToReachNextLevel>`
  * :ref:`SetFogOfWarDisabled(bool a) <CDOTABaseGameMode.SetFogOfWarDisabled>`
  * :ref:`SetGoldSoundDisabled(bool a) <CDOTABaseGameMode.SetGoldSoundDisabled>`
  * :ref:`SetOverrideSelectionEntity(handle unit) <CDOTABaseGameMode.SetOverrideSelectionEntity>`
  * :ref:`SetRecommendedItemsDisabled(bool a) <CDOTABaseGameMode.SetRecommendedItemsDisabled>`
  * :ref:`SetRemoveIllusionsOnDeath(bool a) <CDOTABaseGameMode.SetRemoveIllusionsOnDeath>`
  * :ref:`SetTopBarTeamValue(int a, int b) <CDOTABaseGameMode.SetTopBarTeamValue>`
  * :ref:`SetTopBarTeamValuesOverride(bool a) <CDOTABaseGameMode.SetTopBarTeamValuesOverride>`
  * :ref:`SetTopBarTeamValuesVisible(bool a) <CDOTABaseGameMode.SetTopBarTeamValuesVisible>`
  * :ref:`SetTowerBackdoorProtectionEnabled(bool a) <CDOTABaseGameMode.SetTowerBackdoorProtectionEnabled>`
  * :ref:`SetUseCustomHeroLevels(bool a) <CDOTABaseGameMode.SetUseCustomHeroLevels>`

CDotaQuest
############
extends CBaseEntity
A quest, as seen in the Tutorial and Frostivus

  * :ref:`AddSubquest(handle a) <CDotaQuest.AddSubquest>`
  * :ref:`CompleteQuest() <CDotaQuest.CompleteQuest>`
  * :ref:`GetSubquest(int a) <CDotaQuest.GetSubquest>`
  * :ref:`GetSubquestByName(string a) <CDotaQuest.GetSubquestByName>`
  * :ref:`RemoveSubquest(handle a) <CDotaQuest.RemoveSubquest>`
  * :ref:`SetTextReplaceString(string a) <CDotaQuest.SetTextReplaceString>`
  * :ref:`SetTextReplaceValue(int a, int b) <CDotaQuest.SetTextReplaceValue>`

CDotaSubquestBase
############
extends CDotaQuest
No Description Set

  * :ref:`CompleteSubquest() <CDotaSubquestBase.CompleteSubquest>`
  * :ref:`SetTextReplaceString(string a) <CDotaSubquestBase.SetTextReplaceString>`
  * :ref:`SetTextReplaceValue(int a, int b) <CDotaSubquestBase.SetTextReplaceValue>`

CPhysicsComponent
############
No Description Set

  * :ref:`ExpensiveInstantRayCast(Vector a, Vector b, handle c) <CPhysicsComponent.ExpensiveInstantRayCast>`

CPointTemplate
############
No Description Set

  * :ref:`DeleteCreatedSpawnGroups() <CPointTemplate.DeleteCreatedSpawnGroups>`
  * :ref:`ForceSpawn() <CPointTemplate.ForceSpawn>`
  * :ref:`GetSpawnedEntities() <CPointTemplate.GetSpawnedEntities>`
  * :ref:`SetSpawnCallback(handle a, handle b) <CPointTemplate.SetSpawnCallback>`

CBodyComponent
############
No Description Set

  * :ref:`AddImpulseAtPosition(Vector a, Vector b) <CBodyComponent.AddImpulseAtPosition>`
  * :ref:`AddVelocity(Vector a, Vector b) <CBodyComponent.AddVelocity>`
  * :ref:`DetachFromParent() <CBodyComponent.DetachFromParent>`
  * :ref:`GetSequence() <CBodyComponent.GetSequence>`
  * :ref:`IsAttachedToParent() <CBodyComponent.IsAttachedToParent>`
  * :ref:`LookupSequence(string a) <CBodyComponent.LookupSequence>`
  * :ref:`SequenceDuration(string a) <CBodyComponent.SequenceDuration>`
  * :ref:`SetAngularVelocity(Vector a) <CBodyComponent.SetAngularVelocity>`
  * :ref:`SetAnimation(string a) <CBodyComponent.SetAnimation>`
  * :ref:`SetBodyGroup(string a) <CBodyComponent.SetBodyGroup>`
  * :ref:`SetMaterialGroup(utlstringtoken a) <CBodyComponent.SetMaterialGroup>`
  * :ref:`SetVelocity(Vector velocity) <CBodyComponent.SetVelocity>`

CBaseAnimating
############
extends CBaseEntity
A class containing functions involved in animations

  * :ref:`GetAttachmentAngles(int a) <CBaseAnimating.GetAttachmentAngles>`
  * :ref:`GetAttachmentOrigin(int a) <CBaseAnimating.GetAttachmentOrigin>`
  * :ref:`IsSequenceFinished() <CBaseAnimating.IsSequenceFinished>`
  * :ref:`ScriptLookupAttachment(string a) <CBaseAnimating.ScriptLookupAttachment>`
  * :ref:`SetBodygroup(int a, int b) <CBaseAnimating.SetBodygroup>`
  * :ref:`SetModelScale(float scale) <CBaseAnimating.SetModelScale>`
  * :ref:`SetPoseParameter(string a, float b) <CBaseAnimating.SetPoseParameter>`

CBaseCombatCharacter
############
No Description Set

  * :ref:`GetEquippedWeapons() <CBaseCombatCharacter.GetEquippedWeapons>`
  * :ref:`GetWeaponCount() <CBaseCombatCharacter.GetWeaponCount>`

ProjectileManager
############
The projectile manager, it manages projectiles.

  * :ref:`CreateLinearProjectile(handle a) <ProjectileManager.CreateLinearProjectile>`
  * :ref:`CreateTrackingProjectile(handle a) <ProjectileManager.CreateTrackingProjectile>`
  * :ref:`DestroyLinearProjectile(int a) <ProjectileManager.DestroyLinearProjectile>`
  * :ref:`ProjectileDodge(handle a) <ProjectileManager.ProjectileDodge>`

CBaseTrigger
############
No Description Set

  * :ref:`Disable() <CBaseTrigger.Disable>`
  * :ref:`Enable() <CBaseTrigger.Enable>`
  * :ref:`IsTouching(handle a) <CBaseTrigger.IsTouching>`

CEnvEntityMaker
############
extends CBaseEntity
No Description Set

  * :ref:`SpawnEntity() <CEnvEntityMaker.SpawnEntity>`
  * :ref:`SpawnEntityAtEntityOrigin(handle a) <CEnvEntityMaker.SpawnEntityAtEntityOrigin>`
  * :ref:`SpawnEntityAtLocation(Vector a, Vector b) <CEnvEntityMaker.SpawnEntityAtLocation>`
  * :ref:`SpawnEntityAtNamedEntityOrigin(string a) <CEnvEntityMaker.SpawnEntityAtNamedEntityOrigin>`

CDOTAVoteSystem
############
No Description Set

  * :ref:`StartVote(handle a) <CDOTAVoteSystem.StartVote>`

CMarkupVolumeTagged
############
No Description Set

  * :ref:`HasTag(string a) <CMarkupVolumeTagged.HasTag>`

CScriptPrecacheContext
############
No Description Set

  * :ref:`AddResource(string a) <CScriptPrecacheContext.AddResource>`
  * :ref:`GetValue(string a) <CScriptPrecacheContext.GetValue>`

CScriptKeyValues
############
No Description Set

  * :ref:`GetValue(string a) <CScriptKeyValues.GetValue>`

CScriptParticleManager
############
No Description Set

  * :ref:`CreateParticle(string particleName, int particleAttach, handle owningEntity) <CScriptParticleManager.CreateParticle>`
  * :ref:`CreateParticleForPlayer(string particleName, int particleAttach, handle owningEntity, handle owningPlayer) <CScriptParticleManager.CreateParticleForPlayer>`
  * :ref:`GetParticleReplacement(string a, handle b) <CScriptParticleManager.GetParticleReplacement>`
  * :ref:`ReleaseParticleIndex(int particleId) <CScriptParticleManager.ReleaseParticleIndex>`
  * :ref:`SetParticleAlwaysSimulate(int a) <CScriptParticleManager.SetParticleAlwaysSimulate>`
  * :ref:`SetParticleControl(int particleId, int controlIndex, Vector controlData) <CScriptParticleManager.SetParticleControl>`
  * :ref:`SetParticleControlEnt(int a, int b, handle c, int d, string e, Vector f, bool g) <CScriptParticleManager.SetParticleControlEnt>`

CScriptHeroList
############
No Description Set

  * :ref:`GetAllHeroes() <CScriptHeroList.GetAllHeroes>`
  * :ref:`GetHero(int heroId) <CScriptHeroList.GetHero>`
  * :ref:`GetHeroCount() <CScriptHeroList.GetHeroCount>`

CNativeOutputs
############
No Description Set

  * :ref:`AddOutput(string a, string b) <CNativeOutputs.AddOutput>`
  * :ref:`Init(int a) <CNativeOutputs.Init>`

CEnvProjectedTexture
############
extends CBaseEntity
No Description Set

  * :ref:`SetFarRange(float a) <CEnvProjectedTexture.SetFarRange>`
  * :ref:`SetLinearAttenuation(float a) <CEnvProjectedTexture.SetLinearAttenuation>`
  * :ref:`SetNearRange(float a) <CEnvProjectedTexture.SetNearRange>`
  * :ref:`SetQuadraticAttenuation(float a) <CEnvProjectedTexture.SetQuadraticAttenuation>`
  * :ref:`SetVolumetrics(bool a, float b, float c, int d, float e) <CEnvProjectedTexture.SetVolumetrics>`

CInfoData
############
No Description Set

  * :ref:`QueryColor(utlstringtoken a, Vector b) <CInfoData.QueryColor>`
  * :ref:`QueryFloat(utlstringtoken a, float b) <CInfoData.QueryFloat>`
  * :ref:`QueryInt(utlstringtoken a, int b) <CInfoData.QueryInt>`
  * :ref:`QueryNumber(utlstringtoken a, float b) <CInfoData.QueryNumber>`
  * :ref:`QueryString(utlstringtoken a, string b) <CInfoData.QueryString>`
  * :ref:`QueryVector(utlstringtoken a, Vector b) <CInfoData.QueryVector>`

CPhysicsProp
############
No Description Set

  * :ref:`DisableMotion() <CPhysicsProp.DisableMotion>`
  * :ref:`EnableMotion() <CPhysicsProp.EnableMotion>`

CDOTAGamerules
############


  * :ref:`Defeated() <CDOTAGamerules.Defeated>`
  * :ref:`DidMatchSignoutTimeOut() <CDOTAGamerules.DidMatchSignoutTimeOut>`
  * :ref:`GetCustomGameDifficulty() <CDOTAGamerules.GetCustomGameDifficulty>`
  * :ref:`GetDifficulty() <CDOTAGamerules.GetDifficulty>`
  * :ref:`GetDroppedItem(int dropIndex) <CDOTAGamerules.GetDroppedItem>`
  * :ref:`GetGameModeEntity() <CDOTAGamerules.GetGameModeEntity>`
  * :ref:`GetGameTime() <CDOTAGamerules.GetGameTime>`
  * :ref:`GetMatchSignoutComplete() <CDOTAGamerules.GetMatchSignoutComplete>`
  * :ref:`GetNianFightStartTime() <CDOTAGamerules.GetNianFightStartTime>`
  * :ref:`GetNianTotalDamageTaken() <CDOTAGamerules.GetNianTotalDamageTaken>`
  * :ref:`GetTimeOfDay() <CDOTAGamerules.GetTimeOfDay>`
  * :ref:`IsDaytime() <CDOTAGamerules.IsDaytime>`
  * :ref:`MakeTeamLose(int team) <CDOTAGamerules.MakeTeamLose>`
  * :ref:`NumDroppedItems() <CDOTAGamerules.NumDroppedItems>`
  * :ref:`Playtesting_UpdateAddOnKeyValues() <CDOTAGamerules.Playtesting_UpdateAddOnKeyValues>`
  * :ref:`ResetDefeated() <CDOTAGamerules.ResetDefeated>`
  * :ref:`ResetToHeroSelection() <CDOTAGamerules.ResetToHeroSelection>`
  * :ref:`SendCustomMessage(string message, int teamID, int unknown(1?)) <CDOTAGamerules.SendCustomMessage>`
  * :ref:`SetCreepMinimapIconScale(float scale) <CDOTAGamerules.SetCreepMinimapIconScale>`
  * :ref:`SetCustomGameDifficulty(int a) <CDOTAGamerules.SetCustomGameDifficulty>`
  * :ref:`SetFirstBloodActive(bool a) <CDOTAGamerules.SetFirstBloodActive>`
  * :ref:`SetGameWinner(int team) <CDOTAGamerules.SetGameWinner>`
  * :ref:`SetGoldPerTick(int a) <CDOTAGamerules.SetGoldPerTick>`
  * :ref:`SetGoldTickTime(float a) <CDOTAGamerules.SetGoldTickTime>`
  * :ref:`SetHeroMinimapIconSize(int iconSize) <CDOTAGamerules.SetHeroMinimapIconSize>`
  * :ref:`SetHeroRespawnEnabled(bool canRespawn) <CDOTAGamerules.SetHeroRespawnEnabled>`
  * :ref:`SetHeroSelectionTime(float time) <CDOTAGamerules.SetHeroSelectionTime>`
  * :ref:`SetNianFightStartTime(float a) <CDOTAGamerules.SetNianFightStartTime>`
  * :ref:`SetOverlayHealthBarUnit(handle unit, int style) <CDOTAGamerules.SetOverlayHealthBarUnit>`
  * :ref:`SetPostGameTime(float time) <CDOTAGamerules.SetPostGameTime>`
  * :ref:`SetPreGameTime(float time) <CDOTAGamerules.SetPreGameTime>`
  * :ref:`SetRuneMinimapIconScale(float scale) <CDOTAGamerules.SetRuneMinimapIconScale>`
  * :ref:`SetRuneSpawnTime(float time) <CDOTAGamerules.SetRuneSpawnTime>`
  * :ref:`SetSafeToLeave(bool safeToLeave) <CDOTAGamerules.SetSafeToLeave>`
  * :ref:`SetSameHeroSelectionEnabled(bool enabled) <CDOTAGamerules.SetSameHeroSelectionEnabled>`
  * :ref:`SetTimeOfDay(float time) <CDOTAGamerules.SetTimeOfDay>`
  * :ref:`SetTreeRegrowTime(float time) <CDOTAGamerules.SetTreeRegrowTime>`
  * :ref:`SetUseBaseGoldBountyOnHeroes(bool a) <CDOTAGamerules.SetUseBaseGoldBountyOnHeroes>`
  * :ref:`SetUseCustomHeroXPValues(bool a) <CDOTAGamerules.SetUseCustomHeroXPValues>`
  * :ref:`SetUseUniversalShopMode(bool enabled) <CDOTAGamerules.SetUseUniversalShopMode>`
  * :ref:`State_Get() <CDOTAGamerules.State_Get>`

CToneMapControllerComponent
############
No Description Set

  * :ref:`GetBloomScale() <CToneMapControllerComponent.GetBloomScale>`
  * :ref:`GetMaxExposure() <CToneMapControllerComponent.GetMaxExposure>`
  * :ref:`GetMinExposure() <CToneMapControllerComponent.GetMinExposure>`
  * :ref:`SetBloomScale(float a) <CToneMapControllerComponent.SetBloomScale>`
  * :ref:`SetMaxExposure(float a) <CToneMapControllerComponent.SetMaxExposure>`
  * :ref:`SetMinExposure(float a) <CToneMapControllerComponent.SetMinExposure>`

CDebugOverlayScriptHelper
############
No Description Set

  * :ref:`Axis(Vector a, Quaternion b, float c, bool d, float e) <CDebugOverlayScriptHelper.Axis>`
  * :ref:`Box(Vector a, Vector b, int c, int d, int e, int f, bool g, float h) <CDebugOverlayScriptHelper.Box>`
  * :ref:`BoxAngles(Vector a, Vector b, Vector c, Quaternion d, int e, int f, int g, int h, bool i, float j) <CDebugOverlayScriptHelper.BoxAngles>`
  * :ref:`Capsule(Vector a, Quaternion b, float c, float d, int e, int f, int g, int h, bool i, float j) <CDebugOverlayScriptHelper.Capsule>`
  * :ref:`Circle(Vector a, Quaternion b, float c, int d, int e, int f, int g, bool h, float i) <CDebugOverlayScriptHelper.Circle>`
  * :ref:`CircleScreenOriented(Vector a, float b, int c, int d, int e, int f, bool g, float h) <CDebugOverlayScriptHelper.CircleScreenOriented>`
  * :ref:`Cone(Vector a, Vector b, float c, float d, int e, int f, int g, int h, bool i, float j) <CDebugOverlayScriptHelper.Cone>`
  * :ref:`Cross(Vector a, float b, int c, int d, int e, int f, bool g, float h) <CDebugOverlayScriptHelper.Cross>`
  * :ref:`Cross3D(Vector a, float b, int c, int d, int e, int f, bool g, float h) <CDebugOverlayScriptHelper.Cross3D>`
  * :ref:`Cross3DOriented(Vector a, Quaternion b, float c, int d, int e, int f, int g, bool h, float i) <CDebugOverlayScriptHelper.Cross3DOriented>`
  * :ref:`DrawTickMarkedLine(Vector a, Vector b, float c, int d, int e, int f, int g, int h, bool i, float j) <CDebugOverlayScriptHelper.DrawTickMarkedLine>`
  * :ref:`EntityAttachments(ehandle a, float b) <CDebugOverlayScriptHelper.EntityAttachments>`
  * :ref:`EntityAxis(ehandle a, float b, bool c, float d) <CDebugOverlayScriptHelper.EntityAxis>`
  * :ref:`EntityBounds(ehandle a, int b, int c, int d, int e, bool f, float g) <CDebugOverlayScriptHelper.EntityBounds>`
  * :ref:`EntitySkeleton(ehandle a, float b) <CDebugOverlayScriptHelper.EntitySkeleton>`
  * :ref:`EntityText(ehandle a, int b, string c, int d, int e, int f, int g, float h) <CDebugOverlayScriptHelper.EntityText>`
  * :ref:`FilledRect2D(Vector2D a, Vector2D b, int c, int d, int e, int f, float g) <CDebugOverlayScriptHelper.FilledRect2D>`
  * :ref:`HorzArrow(Vector a, Vector b, float c, int d, int e, int f, int g, bool h, float i) <CDebugOverlayScriptHelper.HorzArrow>`
  * :ref:`Line(Vector a, Vector b, int c, int d, int e, int f, bool g, float h) <CDebugOverlayScriptHelper.Line>`
  * :ref:`Line2D(Vector2D a, Vector2D b, int c, int d, int e, int f, float g) <CDebugOverlayScriptHelper.Line2D>`
  * :ref:`PopDebugOverlayScope() <CDebugOverlayScriptHelper.PopDebugOverlayScope>`
  * :ref:`PushAndClearDebugOverlayScope(utlstringtoken a) <CDebugOverlayScriptHelper.PushAndClearDebugOverlayScope>`
  * :ref:`PushDebugOverlayScope(utlstringtoken a) <CDebugOverlayScriptHelper.PushDebugOverlayScope>`
  * :ref:`RemoveAllInScope(utlstringtoken a) <CDebugOverlayScriptHelper.RemoveAllInScope>`
  * :ref:`SolidCone(Vector a, Vector b, float c, float d, int e, int f, int g, int h, bool i, float j) <CDebugOverlayScriptHelper.SolidCone>`
  * :ref:`Sphere(Vector a, float b, int c, int d, int e, int f, bool g, float h) <CDebugOverlayScriptHelper.Sphere>`
  * :ref:`SweptBox(Vector a, Vector b, Vector c, Vector d, Quaternion e, int f, int g, int h, int i, float j) <CDebugOverlayScriptHelper.SweptBox>`
  * :ref:`Text(Vector a, int b, string c, float d, int e, int f, int g, int h, float i) <CDebugOverlayScriptHelper.Text>`
  * :ref:`Texture(string a, Vector2D b, Vector2D c, int d, int e, int f, int g, Vector2D h, Vector2D i, float j) <CDebugOverlayScriptHelper.Texture>`
  * :ref:`Triangle(Vector a, Vector b, Vector c, int d, int e, int f, int g, bool h, float i) <CDebugOverlayScriptHelper.Triangle>`
  * :ref:`UnitTestCycleOverlayRenderType() <CDebugOverlayScriptHelper.UnitTestCycleOverlayRenderType>`
  * :ref:`VectorText3D(Vector a, Quaternion b, string c, int d, int e, int f, int g, bool h, float i) <CDebugOverlayScriptHelper.VectorText3D>`
  * :ref:`VertArrow(Vector a, Vector b, float c, int d, int e, int f, int g, bool h, float i) <CDebugOverlayScriptHelper.VertArrow>`
  * :ref:`YawArrow(Vector a, float b, float c, float d, int e, int f, int g, int h, bool i, float j) <CDebugOverlayScriptHelper.YawArrow>`

CBaseFlex
############
extends CBaseAnimating
Animated characters who have vertex flex capability (Hi hex6)

  * :ref:`GetCurrentScene() <CBaseFlex.GetCurrentScene>`
  * :ref:`GetSceneByIndex(int a) <CBaseFlex.GetSceneByIndex>`

CSceneEntity
############
extends CBaseEntity
Choreographed scene which controls animation and/or dialog on one or more actors.

  * :ref:`AddBroadcastTeamTarget(int a) <CSceneEntity.AddBroadcastTeamTarget>`
  * :ref:`Cancel() <CSceneEntity.Cancel>`
  * :ref:`EstimateLength() <CSceneEntity.EstimateLength>`
  * :ref:`FindCamera() <CSceneEntity.FindCamera>`
  * :ref:`FindNamedEntity(string a) <CSceneEntity.FindNamedEntity>`
  * :ref:`IsPaused() <CSceneEntity.IsPaused>`
  * :ref:`IsPlayingBack() <CSceneEntity.IsPlayingBack>`
  * :ref:`LoadSceneFromString(string a, string b) <CSceneEntity.LoadSceneFromString>`
  * :ref:`RemoveBroadcastTeamTarget(int a) <CSceneEntity.RemoveBroadcastTeamTarget>`
  * :ref:`Start(handle a) <CSceneEntity.Start>`

GridNav
############
A class that can communicate with the gridnav, useful for seeing if stuff should be able to move

  * :ref:`GridPosToWorldCenterX(int a) <GridNav.GridPosToWorldCenterX>`
  * :ref:`GridPosToWorldCenterY(int a) <GridNav.GridPosToWorldCenterY>`
  * :ref:`IsBlocked(Vector a) <GridNav.IsBlocked>`
  * :ref:`IsNearbyTree(Vector position, float radius, bool c) <GridNav.IsNearbyTree>`
  * :ref:`IsTraversable(Vector a) <GridNav.IsTraversable>`
  * :ref:`RegrowAllTrees() <GridNav.RegrowAllTrees>`
  * :ref:`WorldToGridPosX(float a) <GridNav.WorldToGridPosX>`
  * :ref:`WorldToGridPosY(float a) <GridNav.WorldToGridPosY>`

Convars
############
No Description Set

  * :ref:`GetBool(string variableName) <Convars.GetBool>`
  * :ref:`GetCommandClient() <Convars.GetCommandClient>`
  * :ref:`GetDOTACommandClient() <Convars.GetDOTACommandClient>`
  * :ref:`GetFloat(string name) <Convars.GetFloat>`
  * :ref:`GetInt(string a) <Convars.GetInt>`
  * :ref:`GetStr(string variableName) <Convars.GetStr>`
  * :ref:`RegisterCommand(string variableName, handle function, string helpText, int flags) <Convars.RegisterCommand>`
  * :ref:`RegisterConvar(string name, string defaultValue, string helpText, int flags) <Convars.RegisterConvar>`
  * :ref:`SetBool(string variableName, bool value) <Convars.SetBool>`
  * :ref:`SetFloat(string variableName, float value) <Convars.SetFloat>`
  * :ref:`SetInt(string a, int b) <Convars.SetInt>`
  * :ref:`SetStr(string a, string b) <Convars.SetStr>`

 .. _Global.AngleDiff:
float Global.AngleDiff(float ang1, float ang2)---------------

Returns the number of degrees difference between two yaw angles


::
    local ang = AngleDiff(45, 80)
print(ang)
+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float | ang1 | No Description Set |
|  float | ang2 | No Description Set |
+-----------+--------------+--------------+
Returns:
float - No Description Set


 .. _Global.AppendToLogFile:
void Global.AppendToLogFile(string a, string b)---------------

Appends a ''string'' to a log file on the server


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.ApplyDamage:
float Global.ApplyDamage(handle DamageTable)---------------

Pass ''table'' - Inputs: victim, attacker, damage, damage_type, damage_flags, abilityReturn damage done.


::
    --Apply 500 pure damage from player 1's hero to itself


playerHero = PlayerResource:GetPlayer(1):GetAssignedHero()

local damageTable = {
	victim = playerHero,
	attacker = playerHero,
	damage = 500,
	damage_type = DAMAGE_TYPE_PURE,
}

playerHero:ApplyDamage(damageTable)
+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle | DamageTable | a table containing Unit Victim, Unit attacker, float damage, and DAMAGE_TYPE type |
+-----------+--------------+--------------+
Returns:
float - damage done after reductions


 .. _Global.AxisAngleToQuaternion:
Quaternion Global.AxisAngleToQuaternion(Vector a, float b)---------------

(''vector'',''float'') constructs a quaternion representing a rotation by angle around the specified ''vector'' axis


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+
Returns:
Quaternion - No Description Set


 .. _Global.CancelEntityIOEvents:
void Global.CancelEntityIOEvents(ehandle a)---------------

Create all I/O events for a particular entity


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  ehandle |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.CreateEffect:
bool Global.CreateEffect(handle a)---------------

Pass ''table'' - Inputs: entity, effect


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _Global.CreateHeroForPlayer:
handle Global.CreateHeroForPlayer(string a, handle b)---------------

Creates a DOTA hero by its dota_npc_units.txt name and sets it as the given player's controlled hero


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _Global.CreateItem:
handle Global.CreateItem(string item_name, handle owner, handle owner)---------------

Creates an item with classname <i>item_name</i> that <i>owner</i> can use.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string | item_name | No Description Set |
|  handle | owner | No Description Set |
|  handle | owner | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _Global.CreateItemOnPositionSync:
handle Global.CreateItemOnPositionSync(Vector a, handle b)---------------

Create a physical item at a given location


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _Global.CreateTrigger:
handle Global.CreateTrigger(Vector a, Vector b, Vector c)---------------

CreateTrigger( vecMin, vecMax ) : Creates and returns an AABB trigger


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector |  | No Description Set |
|  Vector |  | No Description Set |
|  Vector |  | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _Global.CreateTriggerRadiusApproximate:
handle Global.CreateTriggerRadiusApproximate(Vector a, float b)---------------

CreateTriggerRadiusApproximate( vecOrigin, flRadius ) : Creates and returns an AABB trigger thats bigger than the radius provided


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _Global.CreateUnitByName:
handle Global.CreateUnitByName(string a, Vector b, bool c, handle d, handle e, int f)---------------

Creates a DOTA unit by its dota_npc_units.txt name ( szUnitName, vLocation, bFindClearSpace, hNPCOwner, hUnitOwner, iTeamNumber )


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
|  Vector |  | No Description Set |
|  bool |  | No Description Set |
|  handle |  | No Description Set |
|  handle |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _Global.CreateUnitByNameAsync:
int Global.CreateUnitByNameAsync(string a, Vector b, bool c, handle d, handle e, int f, handle g)---------------

Creates a DOTA unit by its dota_npc_units.txt name ( szUnitName, vLocation, bFindClearSpace, hNPCOwner, hUnitOwner, iTeamNumber, hCallback )


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
|  Vector |  | No Description Set |
|  bool |  | No Description Set |
|  handle |  | No Description Set |
|  handle |  | No Description Set |
|  int |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _Global.cvar_getf:
float Global.cvar_getf(string a)---------------

Gets the value of the given cvar, as a ''float''.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
+-----------+--------------+--------------+
Returns:
float - No Description Set


 .. _Global.cvar_setf:
bool Global.cvar_setf(string a, float b)---------------

Sets the value of the given cvar, as a ''float''.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _Global.DebugBreak:
void Global.DebugBreak()---------------

Breaks in the debugger




 .. _Global.DebugDrawBox:
void Global.DebugDrawBox(Vector a, Vector b, Vector c, int d, int e, int f, int g, float h)---------------

Draw a debug overlay box (origin, mins, maxs, forward, r, g, b, a, duration )


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector |  | No Description Set |
|  Vector |  | No Description Set |
|  Vector |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.DebugDrawBoxDirection:
void Global.DebugDrawBoxDirection(Vector a, Vector b, Vector c, Vector d, Vector e, float f, float g)---------------

Draw a debug forward box (cent, min, max, forward, vRgb, a, duration)


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector |  | No Description Set |
|  Vector |  | No Description Set |
|  Vector |  | No Description Set |
|  Vector |  | No Description Set |
|  Vector |  | No Description Set |
|  float |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.DebugDrawCircle:
void Global.DebugDrawCircle(Vector a, Vector b, float c, float d, bool e, float f)---------------

Draw a debug circle (center, vRgb, a, rad, ztest, duration)


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector |  | No Description Set |
|  Vector |  | No Description Set |
|  float |  | No Description Set |
|  float |  | No Description Set |
|  bool |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.DebugDrawClear:
void Global.DebugDrawClear()---------------

Try to clear all the debug overlay info




 .. _Global.DebugDrawLine:
void Global.DebugDrawLine(Vector a, Vector b, int c, int d, int e, bool f, float g)---------------

Draw a debug overlay line (origin, target, r, g, b, ztest, duration)


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector |  | No Description Set |
|  Vector |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  bool |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.DebugDrawLine_vCol:
void Global.DebugDrawLine_vCol(Vector a, Vector b, Vector c, bool d, float e)---------------

Draw a debug line using color vec (start, end, vRgb, a, ztest, duration)


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector |  | No Description Set |
|  Vector |  | No Description Set |
|  Vector |  | No Description Set |
|  bool |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.DebugDrawScreenTextLine:
void Global.DebugDrawScreenTextLine(float a, float b, int c, string d, int e, int f, int g, int h, float i)---------------

Draw text with a line offset (x, y, lineOffset, text, r, g, b, a, duration)


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
|  float |  | No Description Set |
|  int |  | No Description Set |
|  string |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.DebugDrawSphere:
void Global.DebugDrawSphere(Vector a, Vector b, float c, float d, bool e, float f)---------------

Draw a debug sphere (center, vRgb, a, rad, ztest, duration)


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector |  | No Description Set |
|  Vector |  | No Description Set |
|  float |  | No Description Set |
|  float |  | No Description Set |
|  bool |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.DebugDrawText:
void Global.DebugDrawText(Vector a, string b, bool c, float d)---------------

Draw text in 3d (origin, text, bViewCheck, duration)


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector |  | No Description Set |
|  string |  | No Description Set |
|  bool |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.DebugScreenTextPretty:
void Global.DebugScreenTextPretty(float a, float b, int c, string d, int e, int f, int g, int h, float i, string j, int k, bool l)---------------

Draw pretty debug text (x, y, lineOffset, text, r, g, b, a, duration, font, size, bBold)


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
|  float |  | No Description Set |
|  int |  | No Description Set |
|  string |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  float |  | No Description Set |
|  string |  | No Description Set |
|  int |  | No Description Set |
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.DoEntFire:
void Global.DoEntFire(string a, string b, string c, float d, handle e, handle f)---------------

EntFire: Generate an entity i/o event ( szTarget, szAction, szValue, flDelay, hActivator, hCaller )


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
|  string |  | No Description Set |
|  string |  | No Description Set |
|  float |  | No Description Set |
|  handle |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.DoEntFireByInstanceHandle:
void Global.DoEntFireByInstanceHandle(handle a, string b, string c, float d, handle e, handle f)---------------

EntFireByHandle:Generate and entity i/o event


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
|  string |  | No Description Set |
|  string |  | No Description Set |
|  float |  | No Description Set |
|  handle |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.DoIncludeScript:
bool Global.DoIncludeScript(string a, handle b)---------------

Execute a script (internal)


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _Global.DoScriptAssert:
void Global.DoScriptAssert(bool a, string b)---------------

ScriptAssert:Asserts the passed in value. Prints out a message and brings up the assert dialog.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  bool |  | No Description Set |
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.DoUniqueString:
string Global.DoUniqueString(string a)---------------

UniqueString:Generate a string guaranteed to be unique across the life of the script VM, with an optional root string. Useful for adding data to table's when not sure what keys are already in use in that table.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
+-----------+--------------+--------------+
Returns:
string - No Description Set


 .. _Global.EmitGlobalSound:
void Global.EmitGlobalSound(string a)---------------

Play named sound for all players


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.EmitSoundOn:
void Global.EmitSoundOn(string a, handle b)---------------

Play named sound on Entity


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.EmitSoundOnClient:
void Global.EmitSoundOnClient(string a, handle b)---------------

Play named sound only on the client for the passed in player


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.EntIndexToHScript:
handle Global.EntIndexToHScript(int a)---------------

Turn an entity index integer to an HScript representing that entity's script instance.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _Global.ExecuteOrderFromTable:
void Global.ExecuteOrderFromTable(handle a)---------------

Issue an order from a script table


::
    local newOrder = {
 		UnitIndex = unitIndex, 
 		OrderType = order,
 		TargetIndex = targetIndex,
 		AbilityIndex = abilityIndex,
 		Position = position,
 		Queue = queue
 	}

ExecuteOrderFromTable(newOrder)
+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.ExponentialDecay:
float Global.ExponentialDecay(float a, float b, float c)---------------

Smooth curve decreasing slower as it approaches zero


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
|  float |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+
Returns:
float - No Description Set


 .. _Global.FileToString:
string Global.FileToString(string a)---------------

Reads a ''string'' from a file to send to script


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
+-----------+--------------+--------------+
Returns:
string - No Description Set


 .. _Global.FindClearSpaceForUnit:
void Global.FindClearSpaceForUnit(handle a, Vector b, bool c)---------------

Place a unit somewhere not already occupied.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
|  Vector |  | No Description Set |
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.FindUnitsInRadius:
table Global.FindUnitsInRadius(int a, Vector b, handle c, float d, int e, int f, int g, int h, bool i)---------------

Finds the units in a given radius with the given flags. ( iTeamNumber, vPosition, hCacheUnit, flRadius, iTeamFilter, iTypeFilter, iFlagFilter, iOrder, bCanGrowCache )


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
|  Vector |  | No Description Set |
|  handle |  | No Description Set |
|  float |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  bool |  | No Description Set |
+-----------+--------------+--------------+
Returns:
table - No Description Set


 .. _Global.FireEntityIOInputNameOnly:
void Global.FireEntityIOInputNameOnly(ehandle a, string b)---------------

Fire Entity's Action Input w/no data


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  ehandle |  | No Description Set |
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.FireEntityIOInputString:
void Global.FireEntityIOInputString(ehandle a, string b, string c)---------------

Fire Entity's Action Input with passed String - you own the memory


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  ehandle |  | No Description Set |
|  string |  | No Description Set |
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.FireEntityIOInputVec:
void Global.FireEntityIOInputVec(ehandle a, string b, Vector c)---------------

Fire Entity's Action Input with passed ''Vector'' ( hEntity, szActionName, vector )


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  ehandle |  | No Description Set |
|  string |  | No Description Set |
|  Vector |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.FireGameEvent:
void Global.FireGameEvent(string eventName, handle parameterTable)---------------

Fire a pre-defined event, which can be found either in custom_events.txt or in dota's resource/*.res


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string | eventName | No Description Set |
|  handle | parameterTable | No Description Set |
+-----------+--------------+--------------+


 .. _Global.FireGameEventLocal:
void Global.FireGameEventLocal(string a, handle b)---------------

Fire a game event without broadcasting to the client.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.FrameTime:
float Global.FrameTime()---------------

Get the time spent on the server in the last frame


Returns:
float - No Description Set


 .. _Global.GetFrameCount:
int Global.GetFrameCount()---------------

Returns the engines current frame count


Returns:
int - No Description Set


 .. _Global.GetFrostyBoostAmount:
float Global.GetFrostyBoostAmount(int a, int b)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
float - No Description Set


 .. _Global.GetFrostyPointsForRound:
int Global.GetFrostyPointsForRound(int a, int b, int c)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _Global.GetGoldFrostyBoostAmount:
float Global.GetGoldFrostyBoostAmount(int a, int b)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
float - No Description Set


 .. _Global.GetGoldFrostyPointsForRound:
int Global.GetGoldFrostyPointsForRound(int a, int b, int c)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _Global.GetGroundPosition:
Vector Global.GetGroundPosition(Vector a, handle b)---------------

Returns the supplied position moved to the ground. Second parameter is an NPC for measuring movement collision hull offset.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+
Returns:
Vector - No Description Set


 .. _Global.GetListenServerHost:
handle Global.GetListenServerHost()---------------

Get the local player on a listen server.


Returns:
handle - No Description Set


 .. _Global.GetMapName:
string Global.GetMapName()---------------

Get the name of the map.


Returns:
string - No Description Set


 .. _Global.GetMaxOutputDelay:
float Global.GetMaxOutputDelay(ehandle a, string b)---------------

Get the longest delay for all events attached to an output


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  ehandle |  | No Description Set |
|  string |  | No Description Set |
+-----------+--------------+--------------+
Returns:
float - No Description Set


 .. _Global.GetPhysAngularVelocity:
Vector Global.GetPhysAngularVelocity(handle a)---------------

Get Angular Velocity for VPHYS or normal object


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
+-----------+--------------+--------------+
Returns:
Vector - No Description Set


 .. _Global.GetPhysVelocity:
Vector Global.GetPhysVelocity(handle a)---------------

Get Velocity for VPHYS or normal object


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
+-----------+--------------+--------------+
Returns:
Vector - No Description Set


 .. _Global.GetSystemDate:
string Global.GetSystemDate()---------------

Get the current real world date


Returns:
string - No Description Set


 .. _Global.GetSystemTime:
string Global.GetSystemTime()---------------

Get the current real world time


Returns:
string - No Description Set


 .. _Global.GetWorldMaxX:
float Global.GetWorldMaxX()---------------

Gets the world's maximum X position.


Returns:
float - No Description Set


 .. _Global.GetWorldMaxY:
float Global.GetWorldMaxY()---------------

Gets the world's maximum Y position.


Returns:
float - No Description Set


 .. _Global.GetWorldMinX:
float Global.GetWorldMinX()---------------

Gets the world's minimum X position.


Returns:
float - No Description Set


 .. _Global.GetWorldMinY:
float Global.GetWorldMinY()---------------

Gets the world's minimum Y position.


Returns:
float - No Description Set


 .. _Global.InitLogFile:
void Global.InitLogFile(string a, string b)---------------

If the given file doesn't exist, creates it with the given contents; does nothing if it exists


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.IsDedicatedServer:
bool Global.IsDedicatedServer()---------------

Returns true if this server is a dedicated server.


Returns:
bool - No Description Set


 .. _Global.IsMarkedForDeletion:
bool Global.IsMarkedForDeletion(handle a)---------------

Returns true if the entity is valid and marked for deletion.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _Global.IsValidEntity:
bool Global.IsValidEntity(handle a)---------------

Checks to see if the given hScript is a valid entity


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _Global.ListenToGameEvent:
int Global.ListenToGameEvent(string EventName, handle functionNameToCall, handle context)---------------

Register as a listener for a game event from script.

{{tip|In addition to listening for [[Dota 2 Workshop Tools/Scripting/Built-In Engine Events|standard engine events]], you can also create your own events by placing them in /scripts/custom_events.txt.}}


::
    ListenToGameEvent('entity_killed', Dynamic_Wrap(MyCustomGameMode, 'OnEntityKilled'), self)


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string | EventName | No Description Set |
|  handle | functionNameToCall | No Description Set |
|  handle | context | No Description Set |
+-----------+--------------+--------------+
Returns:
int - a handle for the event/function pair


 .. _Global.LoadKeyValues:
table Global.LoadKeyValues(string a)---------------

Creates a ''table'' from the specified keyvalues text file


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
+-----------+--------------+--------------+
Returns:
table - No Description Set


 .. _Global.LoadKeyValuesFromString:
table Global.LoadKeyValuesFromString(string a)---------------

Creates a ''table'' from the specified keyvalues ''string''


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
+-----------+--------------+--------------+
Returns:
table - No Description Set


 .. _Global.MakeStringToken:
int Global.MakeStringToken(string a)---------------

Checks to see if the given hScript is a valid entity


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _Global.Msg:
void Global.Msg(string a)---------------

Print a message


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.PauseGame:
void Global.PauseGame(bool a)---------------

Pause or unpause the game.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.PlayerInstanceFromIndex:
handle Global.PlayerInstanceFromIndex(int a)---------------

Get a script instance of a player by index.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _Global.PrecacheEntityFromTable:
void Global.PrecacheEntityFromTable(string a, handle b, handle c)---------------

Precache an entity from KeyValues in ''table''


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
|  handle |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.PrecacheEntityListFromTable:
void Global.PrecacheEntityListFromTable(handle a, handle b)---------------

Precache a list of entity KeyValues table's


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.PrecacheItemByNameAsync:
void Global.PrecacheItemByNameAsync(string a, handle b)---------------

Asynchronously precaches a DOTA item by its dota_npc_items.txt name, provides a callback when it's finished.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.PrecacheItemByNameSync:
void Global.PrecacheItemByNameSync(string a, handle b)---------------

Precaches a DOTA item by its dota_npc_items.txt name


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.PrecacheModel:
void Global.PrecacheModel(string a, handle b)---------------

( modelName, context ) - Manually precache a single model


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.PrecacheResource:
void Global.PrecacheResource(string a, string b, handle c)---------------

Manually precache a single resource


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
|  string |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.PrecacheUnitByNameAsync:
void Global.PrecacheUnitByNameAsync(string a, handle b)---------------

Asynchronously precaches a DOTA unit by its dota_npc_units.txt name, provides a callback when it's finished.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.PrecacheUnitByNameSync:
void Global.PrecacheUnitByNameSync(string a, handle b)---------------

Precaches a DOTA unit by its dota_npc_units.txt name


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.PrintLinkedConsoleMessage:
void Global.PrintLinkedConsoleMessage(string a, string b)---------------

Print a console message with a linked console command


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.RandomFloat:
float Global.RandomFloat(float a, float b)---------------

Get a random ''float'' within a range


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+
Returns:
float - No Description Set


 .. _Global.RandomInt:
int Global.RandomInt(int a, int b)---------------

Get a random ''int'' within a range


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _Global.RandomVector:
Vector Global.RandomVector(float a)---------------

Get a random 2D ''vector''. Argument (''float'') is the minimum length of the returned vector.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
+-----------+--------------+--------------+
Returns:
Vector - No Description Set


 .. _Global.RegisterSpawnGroupFilterProxy:
void Global.RegisterSpawnGroupFilterProxy(string a)---------------

Create a C proxy for a script-based spawn group filter


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.ReloadMOTD:
void Global.ReloadMOTD()---------------

Reloads the MotD file




 .. _Global.RemoveSpawnGroupFilterProxy:
void Global.RemoveSpawnGroupFilterProxy(string a)---------------

Remove the C proxy for a script-based spawn group filter


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.RollPercentage:
bool Global.RollPercentage(int a)---------------

Rolls a number from 1 to 100 and returns true if the roll is less than or equal to the number specified


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _Global.RotateOrientation:
QAngle Global.RotateOrientation(QAngle a, QAngle b)---------------

Rotate a ''QAngle'' by another ''QAngle''.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  QAngle |  | No Description Set |
|  QAngle |  | No Description Set |
+-----------+--------------+--------------+
Returns:
QAngle - No Description Set


 .. _Global.RotatePosition:
Vector Global.RotatePosition(Vector a, QAngle b, Vector c)---------------

Rotate a ''Vector'' around a point.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector |  | No Description Set |
|  QAngle |  | No Description Set |
|  Vector |  | No Description Set |
+-----------+--------------+--------------+
Returns:
Vector - No Description Set


 .. _Global.RotateQuaternionByAxisAngle:
Quaternion Global.RotateQuaternionByAxisAngle(Quaternion a, Vector b, float c)---------------

Rotates a quaternion by the specified angle around the specified ''vector'' axis


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Quaternion |  | No Description Set |
|  Vector |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+
Returns:
Quaternion - No Description Set


 .. _Global.RotationDelta:
QAngle Global.RotationDelta(QAngle a, QAngle b)---------------

Find the delta between two ''QAngle''s.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  QAngle |  | No Description Set |
|  QAngle |  | No Description Set |
+-----------+--------------+--------------+
Returns:
QAngle - No Description Set


 .. _Global.rr_AddDecisionRule:
bool Global.rr_AddDecisionRule(handle a)---------------

Add a rule to the decision database.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _Global.rr_CommitAIResponse:
bool Global.rr_CommitAIResponse(handle a, handle b)---------------

Commit the result of QueryBestResponse back to the given entity to play. Call with params (entity, airesponse)


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _Global.rr_GetResponseTargets:
handle Global.rr_GetResponseTargets()---------------

Retrieve a ''table'' of all available expresser targets, in the form { name : ''handle'', name: ''handle'' }.


Returns:
handle - No Description Set


 .. _Global.rr_QueryBestResponse:
bool Global.rr_QueryBestResponse(handle a, handle b, handle c)---------------

Params: ( hEnt, hQuery, hResult ) // Static : tests 'query' against entity's response system and returns the best response found (or ''nil'' if none found).


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
|  handle |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _Global.Say:
void Global.Say(handle entity, string message, bool teamOnly)---------------

Have Entity say ''string'', and teamOnly or not


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle | entity | No Description Set |
|  string | message | No Description Set |
|  bool | teamOnly | No Description Set |
+-----------+--------------+--------------+


 .. _Global.ScreenShake:
void Global.ScreenShake(Vector a, float b, float c, float d, float e, int f, bool g)---------------

Start a screenshake with the following parameters. vecCenter, flAmplitude, flFrequency, flDuration, flRadius, eCommand( SHAKE_START = 0, SHAKE_STOP = 1 ), bAirShake


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector |  | No Description Set |
|  float |  | No Description Set |
|  float |  | No Description Set |
|  float |  | No Description Set |
|  float |  | No Description Set |
|  int |  | No Description Set |
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.SendFrostivusTimeElapsedToGC:
void Global.SendFrostivusTimeElapsedToGC()---------------

No Description Set




 .. _Global.SendFrostyPointsMessageToGC:
void Global.SendFrostyPointsMessageToGC(handle a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.SendToConsole:
void Global.SendToConsole(string a)---------------

Send a ''string'' to the console as a client command


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.SendToServerConsole:
void Global.SendToServerConsole(string a)---------------

Send a ''string'' to the console as a server command


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.SetOpvarFloatAll:
void Global.SetOpvarFloatAll(string a, string b, string c, float d)---------------

Sets an opvar value for all players


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
|  string |  | No Description Set |
|  string |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.SetOpvarFloatPlayer:
void Global.SetOpvarFloatPlayer(string a, string b, string c, float d, handle e)---------------

Sets an opvar value for a single player ( szStackName, szOperatorName, szOpvarName, flOpvarValue, hEnt )


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
|  string |  | No Description Set |
|  string |  | No Description Set |
|  float |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.SetQuestName:
void Global.SetQuestName(string a)---------------

Set the current quest name.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.SetQuestPhase:
void Global.SetQuestPhase(int a)---------------

Set the current quest phase.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.SetRenderingEnabled:
void Global.SetRenderingEnabled(ehandle a, bool b)---------------

Set rendering on/off for an ''ehandle''


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  ehandle |  | No Description Set |
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.ShowGenericPopup:
void Global.ShowGenericPopup(string title, string content, string unknown, string unknown, int containerType)---------------




+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string | title | No Description Set |
|  string | content | No Description Set |
|  string | unknown | No Description Set |
|  string | unknown | No Description Set |
|  int | containerType | No Description Set |
+-----------+--------------+--------------+


 .. _Global.ShowGenericPopupToPlayer:
void Global.ShowGenericPopupToPlayer(handle a, string b, string c, string d, string e, int f)---------------

Show a generic popup dialog to a specific player.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
|  string |  | No Description Set |
|  string |  | No Description Set |
|  string |  | No Description Set |
|  string |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.ShowMessage:
void Global.ShowMessage(string a)---------------

Print a hud message on all clients


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.SpawnEntityFromTableSynchronous:
handle Global.SpawnEntityFromTableSynchronous(string a, handle b)---------------

Synchronously spawns a single entity from a ''table''


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _Global.SpawnEntityGroupFromTable:
bool Global.SpawnEntityGroupFromTable(handle groupSpawnTables, bool bAsync, handle hCallback)---------------

Hierarchically spawn an entity group from a set of spawn tables.


::
    --some code here
+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle | groupSpawnTables | No Description Set |
|  bool | bAsync | true if running asynchronously |
|  handle | hCallback | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _Global.SpawnEntityListFromTableAsynchronous:
int Global.SpawnEntityListFromTableAsynchronous(handle a, handle b)---------------

Asynchronously spawn an entity group from a list of spawn table's. A callback will be triggered when the spawning is complete


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _Global.SpawnEntityListFromTableSynchronous:
handle Global.SpawnEntityListFromTableSynchronous(handle a)---------------

Synchronously spawn an entity group from a list of spawn table's.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _Global.SplineQuaternions:
Quaternion Global.SplineQuaternions(Quaternion a, Quaternion b, float c)---------------

(quaternion,quaternion,''float'') very basic interpolation of v0 to v1 over t on [0,1]


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Quaternion |  | No Description Set |
|  Quaternion |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+
Returns:
Quaternion - No Description Set


 .. _Global.SplineVectors:
Vector Global.SplineVectors(Vector a, Vector b, float c)---------------

(''vector'',''vector'',''float'') very basic interpolation of v0 to v1 over t on [0,1]


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector |  | No Description Set |
|  Vector |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+
Returns:
Vector - No Description Set


 .. _Global.StartSoundEvent:
void Global.StartSoundEvent(string a, handle b)---------------

Start a sound event


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.StopEffect:
void Global.StopEffect(handle a, string b)---------------

(hEntity, szEffectName)


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.StopListeningToAllGameEvents:
void Global.StopListeningToAllGameEvents(handle a)---------------

Stop listening to all game events within a specific context.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.StopListeningToGameEvent:
bool Global.StopListeningToGameEvent(int a)---------------

Stop listening to a particular game event.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _Global.StopSoundEvent:
void Global.StopSoundEvent(string a, handle b)---------------

Stops a sound event


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.StopSoundOn:
void Global.StopSoundOn(string soundName, handle playingEntity)---------------

Stop named sound on Entity


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string | soundName | No Description Set |
|  handle | playingEntity | No Description Set |
+-----------+--------------+--------------+


 .. _Global.StringToFile:
bool Global.StringToFile(string a, string b)---------------

Store a ''string'' to a file for later reading


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
|  string |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _Global.Time:
float Global.Time()---------------

Get the current server time


Returns:
float - No Description Set


 .. _Global.TraceCollideable:
bool Global.TraceCollideable(handle a)---------------

Pass ''table'' - Inputs: start, end, ent, (optional mins, maxs) -- outputs: pos, fraction, hit, startsolid, normal


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _Global.TraceHull:
bool Global.TraceHull(handle a)---------------

Pass ''table'' - Inputs: start, end, min, max, mask, ignore  -- outputs: pos, fraction, hit, enthit, startsolid


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _Global.TraceLine:
bool Global.TraceLine(handle a)---------------

Pass ''table'' - Inputs: startpos, endpos, mask, ignore  -- outputs: pos, fraction, hit, enthit, startsolid


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _Global.UnloadSpawnGroup:
void Global.UnloadSpawnGroup(string a)---------------

Unload a spawn group by name


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.UnloadSpawnGroupByHandle:
void Global.UnloadSpawnGroupByHandle(int a)---------------

Unload a spawn group by ''handle''


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.UpdateEventPoints:
void Global.UpdateEventPoints(handle a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.UTIL_Remove:
void Global.UTIL_Remove(handle a)---------------

Removes the specified entity


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.UTIL_RemoveImmediate:
void Global.UTIL_RemoveImmediate(handle a)---------------

Immediately removes the specified entity


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.VectorToAngles:
QAngle Global.VectorToAngles(Vector a)---------------

Get Qangles (with no roll) for a ''Vector''.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector |  | No Description Set |
+-----------+--------------+--------------+
Returns:
QAngle - No Description Set


 .. _Global.Warning:
void Global.Warning(string a)---------------

Print a warning


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseEntity.ApplyAbsVelocityImpulse:
void CBaseEntity.ApplyAbsVelocityImpulse(Vector a)---------------

Apply a Velocity Impulse


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector |  | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseEntity.ApplyLocalAngularVelocityImpulse:
void CBaseEntity.ApplyLocalAngularVelocityImpulse(Vector a)---------------

Apply an Ang Velocity Impulse


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector |  | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseEntity.EmitSound:
void CBaseEntity.EmitSound(string soundName)---------------

 


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string | soundName | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseEntity.EmitSoundParams:
void CBaseEntity.EmitSoundParams(string soundName, int pitch, float volume, float soundTime)---------------

Plays/modifies a sound from this entity. changes sound if Pitch and/or Volume or SoundTime is > 0.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string | soundName | No Description Set |
|  int | pitch | No Description Set |
|  float | volume | No Description Set |
|  float | soundTime | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseEntity.EyeAngles:
QAngle CBaseEntity.EyeAngles()---------------

Get the qangles that this entity is looking at.


Returns:
QAngle - No Description Set


 .. _CBaseEntity.EyePosition:
Vector CBaseEntity.EyePosition()---------------

Get ''vector'' to eye position - absolute coords


Returns:
Vector - No Description Set


 .. _CBaseEntity.FirstMoveChild:
handle CBaseEntity.FirstMoveChild()---------------

No Description Set


Returns:
handle - No Description Set


 .. _CBaseEntity.GatherCriteria:
void CBaseEntity.GatherCriteria(handle a)---------------

Returns a ''table'' containing the criteria that would be used for response queries on this entity. This is the same as the ''table'' that is passed to response rule script function callbacks.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseEntity.GetAbsOrigin:
Vector CBaseEntity.GetAbsOrigin()---------------

No Description Set


Returns:
Vector - No Description Set


 .. _CBaseEntity.GetAngles:
QAngle CBaseEntity.GetAngles()---------------

No Description Set


Returns:
QAngle - No Description Set


 .. _CBaseEntity.GetAnglesAsVector:
Vector CBaseEntity.GetAnglesAsVector()---------------

Get entity pitch, yaw, roll as a ''vector''


Returns:
Vector - No Description Set


 .. _CBaseEntity.GetAngularVelocity:
Vector CBaseEntity.GetAngularVelocity()---------------

Get the local angular velocity - returns a ''vector'' of pitch,yaw,roll


Returns:
Vector - No Description Set


 .. _CBaseEntity.GetBaseVelocity:
Vector CBaseEntity.GetBaseVelocity()---------------

Get Base velocity


Returns:
Vector - No Description Set


 .. _CBaseEntity.GetBoundingMaxs:
Vector CBaseEntity.GetBoundingMaxs()---------------

Get a ''vector'' containing max bounds, centered on object


Returns:
Vector - No Description Set


 .. _CBaseEntity.GetBoundingMins:
Vector CBaseEntity.GetBoundingMins()---------------

Get a ''vector'' containing min bounds, centered on object


Returns:
Vector - No Description Set


 .. _CBaseEntity.GetBounds:
table CBaseEntity.GetBounds()---------------

Get a ''table'' containing the 'Mins' & 'Maxs' ''vector'' bounds, centered on object


Returns:
table - No Description Set


 .. _CBaseEntity.GetCenter:
Vector CBaseEntity.GetCenter()---------------

Get ''vector'' to center of object - absolute coords


Returns:
Vector - No Description Set


 .. _CBaseEntity.GetChildren:
handle CBaseEntity.GetChildren()---------------

Get the entities parented to this entity.


Returns:
handle - No Description Set


 .. _CBaseEntity.GetContext:
table CBaseEntity.GetContext(string a)---------------

GetContext( name ): looks up a context and returns it if available. May return ''string'', ''float'', or ''nil'' (if the context isn't found)


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
+-----------+--------------+--------------+
Returns:
table - No Description Set


 .. _CBaseEntity.GetForwardVector:
Vector CBaseEntity.GetForwardVector()---------------

Get the forward ''vector'' of the entity


Returns:
Vector - No Description Set


 .. _CBaseEntity.GetHealth:
int CBaseEntity.GetHealth()---------------

No Description Set


Returns:
int - No Description Set


 .. _CBaseEntity.GetLocalAngularVelocity:
QAngle CBaseEntity.GetLocalAngularVelocity()---------------

Maybe local angvel


Returns:
QAngle - No Description Set


 .. _CBaseEntity.GetLocalVelocity:
Vector CBaseEntity.GetLocalVelocity()---------------

Get Entity relative velocity


Returns:
Vector - No Description Set


 .. _CBaseEntity.GetMaxHealth:
int CBaseEntity.GetMaxHealth()---------------

No Description Set


Returns:
int - No Description Set


 .. _CBaseEntity.GetModelName:
string CBaseEntity.GetModelName()---------------

Returns the name of the model


Returns:
string - No Description Set


 .. _CBaseEntity.GetMoveParent:
handle CBaseEntity.GetMoveParent()---------------

If in hierarchy, retrieves the entity's parent


Returns:
handle - No Description Set


 .. _CBaseEntity.GetOrigin:
Vector CBaseEntity.GetOrigin()---------------

No Description Set


Returns:
Vector - No Description Set


 .. _CBaseEntity.GetOwner:
handle CBaseEntity.GetOwner()---------------

Gets this entity's owner


Returns:
handle - No Description Set


 .. _CBaseEntity.GetOwnerEntity:
handle CBaseEntity.GetOwnerEntity()---------------

Get the owner entity, if there is one


Returns:
handle - No Description Set


 .. _CBaseEntity.GetRightVector:
Vector CBaseEntity.GetRightVector()---------------

Get the right ''vector'' of the entity


Returns:
Vector - No Description Set


 .. _CBaseEntity.GetRootMoveParent:
handle CBaseEntity.GetRootMoveParent()---------------

If in hierarchy, walks up the hierarchy to find the root parent


Returns:
handle - No Description Set


 .. _CBaseEntity.GetSoundDuration:
float CBaseEntity.GetSoundDuration(string soundName, string actormodelname)---------------

Returns ''float'' duration of the sound. Takes soundname and optional actormodelname.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string | soundName | No Description Set |
|  string | actormodelname | No Description Set |
+-----------+--------------+--------------+
Returns:
float - No Description Set


 .. _CBaseEntity.GetTeam:
int CBaseEntity.GetTeam()---------------

No Description Set


Returns:
int - No Description Set


 .. _CBaseEntity.GetUpVector:
Vector CBaseEntity.GetUpVector()---------------

Get the up ''vector'' of the entity


Returns:
Vector - No Description Set


 .. _CBaseEntity.GetVelocity:
Vector CBaseEntity.GetVelocity()---------------

No Description Set


Returns:
Vector - No Description Set


 .. _CBaseEntity.IsAlive:
bool CBaseEntity.IsAlive()---------------

No Description Set.


Returns:
bool - No Description Set


 .. _CBaseEntity.IsPlayer:
bool CBaseEntity.IsPlayer()---------------

Is this a player entity?


Returns:
bool - No Description Set


 .. _CBaseEntity.Kill:
void CBaseEntity.Kill()---------------

No Description Set




 .. _CBaseEntity.NextMovePeer:
handle CBaseEntity.NextMovePeer()---------------

No Description Set


Returns:
handle - No Description Set


 .. _CBaseEntity.OverrideFriction:
void CBaseEntity.OverrideFriction(float a, float b)---------------

Takes duration, value for a temporary override


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseEntity.PrecacheScriptSound:
void CBaseEntity.PrecacheScriptSound(string a)---------------

Precache a sound for later playing.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseEntity.SetAbsOrigin:
void CBaseEntity.SetAbsOrigin(Vector origin)---------------

SetAbsOrigin


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector | origin | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseEntity.SetAngles:
void CBaseEntity.SetAngles(float pitch, float yaw, float roll)---------------

Set entity pitch, yaw, roll


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float | pitch | No Description Set |
|  float | yaw | No Description Set |
|  float | roll | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseEntity.SetAngularVelocity:
void CBaseEntity.SetAngularVelocity(float pitch, float yaw, float roll)---------------

Set the local angular velocity - takes ''float'' pitch,yaw,roll velocities


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float | pitch | No Description Set |
|  float | yaw | No Description Set |
|  float | roll | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseEntity.SetContext:
void CBaseEntity.SetContext(string a, string b, float c)---------------

SetContext( name , value, duration ): store any key/value pair in this entity's dialog contexts. Value must be a ''string''. Will last for duration (set 0 to mean 'forever').


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
|  string |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseEntity.SetContextNum:
void CBaseEntity.SetContextNum(string a, float b, float c)---------------

SetContext( name , value, duration ): store any key/value pair in this entity's dialog contexts. Value must be a number (''int'' or ''float''). Will last for duration (set 0 to mean 'forever').


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
|  float |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseEntity.SetContextThink:
void CBaseEntity.SetContextThink(string a, handle b, float c)---------------

Set a think function on this entity.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
|  handle |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseEntity.SetForwardVector:
void CBaseEntity.SetForwardVector(Vector forwardVec)---------------

Set the orientation of the entity to have this forward ''forwardVec''


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector | forwardVec | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseEntity.SetFriction:
void CBaseEntity.SetFriction(float a)---------------

Set PLAYER friction, ignored for objects


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseEntity.SetGravity:
void CBaseEntity.SetGravity(float a)---------------

Set PLAYER gravity, ignored for objects


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseEntity.SetHealth:
void CBaseEntity.SetHealth(int hp)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int | hp | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseEntity.SetMaxHealth:
void CBaseEntity.SetMaxHealth(int maxHP)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int | maxHP | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseEntity.SetModel:
void CBaseEntity.SetModel(string modelName)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string | modelName | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseEntity.SetOrigin:
void CBaseEntity.SetOrigin(Vector origin)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector | origin | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseEntity.SetOwner:
void CBaseEntity.SetOwner(handle owningEntity)---------------

Sets this entity's owner


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle | owningEntity | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseEntity.SetParent:
void CBaseEntity.SetParent(handle a, string b)---------------

Set the parent for this entity.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseEntity.SetRenderColor:
void CBaseEntity.SetRenderColor(int a, int b, int c)---------------

SetRenderColor( r, g, b ): Sets the render color of the entity.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseEntity.SetSize:
void CBaseEntity.SetSize(Vector a, Vector b)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector |  | No Description Set |
|  Vector |  | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseEntity.SetTeam:
void CBaseEntity.SetTeam(int team)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int | team | DOTA_TEAM |
+-----------+--------------+--------------+


 .. _CBaseEntity.SetVelocity:
void CBaseEntity.SetVelocity(Vector a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector |  | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseEntity.StopSound:
void CBaseEntity.StopSound(string soundName)---------------

Stops a named sound playing from this entity.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string | soundName | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseEntity.Trigger:
void CBaseEntity.Trigger()---------------

Fires off this entity's OnTrigger responses




 .. _CEntities.CreateByClassname:
handle CEntities.CreateByClassname(string className)---------------

Creates an entity by classname


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string | className | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _CEntities.FindAllByClassname:
table CEntities.FindAllByClassname(string a)---------------

Finds all entities by class name. Returns an array containing all the found entities.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
+-----------+--------------+--------------+
Returns:
table - No Description Set


 .. _CEntities.FindAllByClassnameWithin:
table CEntities.FindAllByClassnameWithin(string a, Vector b, float c)---------------

Find entities by class name within a radius.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
|  Vector |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+
Returns:
table - No Description Set


 .. _CEntities.FindAllByModel:
table CEntities.FindAllByModel(string modelName)---------------

Find entities by model name.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string | modelName | No Description Set |
+-----------+--------------+--------------+
Returns:
table - No Description Set


 .. _CEntities.FindAllByName:
table CEntities.FindAllByName(string name)---------------

Find all entities by name. Returns an array containing all the found entities in it.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string | name | No Description Set |
+-----------+--------------+--------------+
Returns:
table - No Description Set


 .. _CEntities.FindAllByNameWithin:
table CEntities.FindAllByNameWithin(string name, Vector origin, float maxRadius)---------------

Find entities by name within a radius.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string | name | No Description Set |
|  Vector | origin | No Description Set |
|  float | maxRadius | No Description Set |
+-----------+--------------+--------------+
Returns:
table - No Description Set


 .. _CEntities.FindAllByTarget:
table CEntities.FindAllByTarget(string targetName)---------------

Find entities by targetname.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string | targetName | No Description Set |
+-----------+--------------+--------------+
Returns:
table - No Description Set


 .. _CEntities.FindAllInSphere:
table CEntities.FindAllInSphere(Vector origin, float maxRadius)---------------

Find entities within a radius.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector | origin | No Description Set |
|  float | maxRadius | No Description Set |
+-----------+--------------+--------------+
Returns:
table - No Description Set


 .. _CEntities.FindByClassname:
handle CEntities.FindByClassname(handle startFrom, string className)---------------

Find entities by class name. Pass ''nil'' to start an iteration, or reference to a previously found entity to continue a search


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle | startFrom | No Description Set |
|  string | className | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _CEntities.FindByClassnameNearest:
handle CEntities.FindByClassnameNearest(string className, Vector origin, float maxRadius)---------------

Find entities by class name nearest to a point.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string | className | No Description Set |
|  Vector | origin | No Description Set |
|  float | maxRadius | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _CEntities.FindByClassnameWithin:
handle CEntities.FindByClassnameWithin(handle startFrom, string className, Vector origin, float maxRadius)---------------

Find entities by class name within a radius. Pass ''nil'' to start an iteration, or reference to a previously found entity to continue a search


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle | startFrom | No Description Set |
|  string | className | No Description Set |
|  Vector | origin | No Description Set |
|  float | maxRadius | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _CEntities.FindByModel:
handle CEntities.FindByModel(handle startFrom, string modelName)---------------

Find entities by model name. Pass ''nil'' to start an iteration, or reference to a previously found entity to continue a search


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle | startFrom | No Description Set |
|  string | modelName | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _CEntities.FindByModelWithin:
handle CEntities.FindByModelWithin(handle startFrom, string modelName, Vector origin, float maxRadius)---------------

Find entities by model name within a radius. Pass ''nil'' to start an iteration, or reference to a previously found entity to continue a search


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle | startFrom | No Description Set |
|  string | modelName | No Description Set |
|  Vector | origin | No Description Set |
|  float | maxRadius | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _CEntities.FindByName:
handle CEntities.FindByName(handle lastEnt, string searchString)---------------

Find entities by name. Pass ''nil'' to start an iteration, or reference to a previously found entity to continue a search


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle | lastEnt | No Description Set |
|  string | searchString | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _CEntities.FindByNameNearest:
handle CEntities.FindByNameNearest(string name, Vector origin, float maxRadius)---------------

Find entities by name nearest to a point.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string | name | No Description Set |
|  Vector | origin | No Description Set |
|  float | maxRadius | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _CEntities.FindByNameWithin:
handle CEntities.FindByNameWithin(handle startFrom, string name, Vector origin, float maxRadius)---------------

Find entities by name within a radius. Pass ''nil'' to start an iteration, or reference to a previously found entity to continue a search


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle | startFrom | No Description Set |
|  string | name | No Description Set |
|  Vector | origin | No Description Set |
|  float | maxRadius | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _CEntities.FindByTarget:
handle CEntities.FindByTarget(handle startFrom, string targetName)---------------

Find entities by targetname. Pass ''nil'' to start an iteration, or reference to a previously found entity to continue a search


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle | startFrom | No Description Set |
|  string | targetName | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _CEntities.FindInSphere:
handle CEntities.FindInSphere(handle startFrom, Vector origin, float maxRadius)---------------

Find entities within a radius. Pass ''nil'' to start an iteration, or reference to a previously found entity to continue a search


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle | startFrom | No Description Set |
|  Vector | origin | No Description Set |
|  float | maxRadius | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _CEntities.First:
handle CEntities.First()---------------

Begin an iteration over the list of entities


Returns:
handle - No Description Set


 .. _CEntities.Next:
handle CEntities.Next(handle startFrom)---------------

Continue an iteration over the list of entities, providing reference to a previously found entity


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle | startFrom | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _CEntityInstance.ConnectOutput:
void CEntityInstance.ConnectOutput(string a, string b)---------------

Adds an I/O connection that will call the named function on this entity when the specified output fires.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _CEntityInstance.Destroy:
void CEntityInstance.Destroy()---------------

No Description Set




 .. _CEntityInstance.DisconnectOutput:
void CEntityInstance.DisconnectOutput(string a, string b)---------------

Removes a connected script function from an I/O event on this entity.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _CEntityInstance.DisconnectRedirectedOutput:
void CEntityInstance.DisconnectRedirectedOutput(string a, string b, handle c)---------------

Removes a connected script function from an I/O event on the passed entity.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
|  string |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CEntityInstance.entindex:
int CEntityInstance.entindex()---------------

No Description Set


Returns:
int - No Description Set


 .. _CEntityInstance.FireOutput:
void CEntityInstance.FireOutput(string a, handle b, handle c, table d, float e)---------------

Fire an entity output


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
|  handle |  | No Description Set |
|  handle |  | No Description Set |
|  table |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CEntityInstance.GetClassname:
string CEntityInstance.GetClassname()---------------

No Description Set


Returns:
string - No Description Set


 .. _CEntityInstance.GetDebugName:
string CEntityInstance.GetDebugName()---------------

Get the entity name w/help if not defined (i.e. classname/etc)


Returns:
string - No Description Set


 .. _CEntityInstance.GetEntityHandle:
ehandle CEntityInstance.GetEntityHandle()---------------

Get the entity as an EHANDLE


Returns:
ehandle - No Description Set


 .. _CEntityInstance.GetEntityIndex:
int CEntityInstance.GetEntityIndex()---------------

No Description Set


Returns:
int - No Description Set


 .. _CEntityInstance.GetIntAttr:
int CEntityInstance.GetIntAttr(string a)---------------

Get Integer Attribute


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CEntityInstance.GetName:
string CEntityInstance.GetName()---------------

No Description Set


Returns:
string - No Description Set


 .. _CEntityInstance.GetOrCreatePrivateScriptScope:
handle CEntityInstance.GetOrCreatePrivateScriptScope()---------------

Retrieve, creating if necessary, the private per-instance script-side data associated with an entity


Returns:
handle - No Description Set


 .. _CEntityInstance.GetOrCreatePublicScriptScope:
handle CEntityInstance.GetOrCreatePublicScriptScope()---------------

Retrieve, creating if necessary, the public script-side data associated with an entity


Returns:
handle - No Description Set


 .. _CEntityInstance.GetPrivateScriptScope:
handle CEntityInstance.GetPrivateScriptScope()---------------

Retrieve the private per-instance script-side data associated with an entity


Returns:
handle - No Description Set


 .. _CEntityInstance.GetPublicScriptScope:
handle CEntityInstance.GetPublicScriptScope()---------------

Retrieve the public script-side data associated with an entity


Returns:
handle - No Description Set


 .. _CEntityInstance.RedirectOutput:
void CEntityInstance.RedirectOutput(string a, string b, handle c)---------------

Adds an I/O connection that will call the named function on the passed entity when the specified output fires.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
|  string |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CEntityInstance.RemoveSelf:
void CEntityInstance.RemoveSelf()---------------

Delete this entity




 .. _CEntityInstance.SetIntAttr:
void CEntityInstance.SetIntAttr(string a, int b)---------------

Set Integer Attribute


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseAbility.CastAbility:
void CDOTABaseAbility.CastAbility()---------------

No Description Set




 .. _CDOTABaseAbility.ContinueCasting:
bool CDOTABaseAbility.ContinueCasting()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTABaseAbility.CreateVisibilityNode:
void CDOTABaseAbility.CreateVisibilityNode(Vector a, float b, float c)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector |  | No Description Set |
|  float |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseAbility.DecrementModifierRefCount:
void CDOTABaseAbility.DecrementModifierRefCount()---------------

No Description Set




 .. _CDOTABaseAbility.EndChannel:
void CDOTABaseAbility.EndChannel(bool a)---------------

Param: ''bool'' bInterrupted


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseAbility.EndCooldown:
void CDOTABaseAbility.EndCooldown()---------------

Clear the cooldown remaining on this ability.




 .. _CDOTABaseAbility.GetAbilityDamage:
int CDOTABaseAbility.GetAbilityDamage()---------------

No Description Set


Returns:
int - No Description Set


 .. _CDOTABaseAbility.GetAbilityDamageType:
int CDOTABaseAbility.GetAbilityDamageType()---------------

No Description Set


Returns:
int - No Description Set


 .. _CDOTABaseAbility.GetAbilityIndex:
int CDOTABaseAbility.GetAbilityIndex()---------------

No Description Set


Returns:
int - No Description Set


 .. _CDOTABaseAbility.GetAbilityName:
string CDOTABaseAbility.GetAbilityName()---------------

No Description Set


Returns:
string - No Description Set


 .. _CDOTABaseAbility.GetAbilityTargetFlags:
int CDOTABaseAbility.GetAbilityTargetFlags()---------------

No Description Set


Returns:
int - No Description Set


 .. _CDOTABaseAbility.GetAbilityTargetTeam:
int CDOTABaseAbility.GetAbilityTargetTeam()---------------

No Description Set


Returns:
int - No Description Set


 .. _CDOTABaseAbility.GetAbilityTargetType:
int CDOTABaseAbility.GetAbilityTargetType()---------------

No Description Set


Returns:
int - No Description Set


 .. _CDOTABaseAbility.GetAbilityType:
int CDOTABaseAbility.GetAbilityType()---------------

No Description Set


Returns:
int - No Description Set


 .. _CDOTABaseAbility.GetAnimationIgnoresModelScale:
bool CDOTABaseAbility.GetAnimationIgnoresModelScale()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTABaseAbility.GetAssociatedPrimaryAbilities:
string CDOTABaseAbility.GetAssociatedPrimaryAbilities()---------------

No Description Set


Returns:
string - No Description Set


 .. _CDOTABaseAbility.GetAssociatedSecondaryAbilities:
string CDOTABaseAbility.GetAssociatedSecondaryAbilities()---------------

No Description Set


Returns:
string - No Description Set


 .. _CDOTABaseAbility.GetAutoCastState:
bool CDOTABaseAbility.GetAutoCastState()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTABaseAbility.GetBackswingTime:
float CDOTABaseAbility.GetBackswingTime()---------------

No Description Set


Returns:
float - No Description Set


 .. _CDOTABaseAbility.GetBehavior:
int CDOTABaseAbility.GetBehavior()---------------

No Description Set


Returns:
int - No Description Set


 .. _CDOTABaseAbility.GetCaster:
handle CDOTABaseAbility.GetCaster()---------------

No Description Set


Returns:
handle - No Description Set


 .. _CDOTABaseAbility.GetCastPoint:
float CDOTABaseAbility.GetCastPoint()---------------

No Description Set


Returns:
float - No Description Set


 .. _CDOTABaseAbility.GetCastRange:
int CDOTABaseAbility.GetCastRange()---------------

No Description Set


Returns:
int - No Description Set


 .. _CDOTABaseAbility.GetChannelledManaCostPerSecond:
int CDOTABaseAbility.GetChannelledManaCostPerSecond(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTABaseAbility.GetChannelStartTime:
float CDOTABaseAbility.GetChannelStartTime()---------------

No Description Set


Returns:
float - No Description Set


 .. _CDOTABaseAbility.GetChannelTime:
float CDOTABaseAbility.GetChannelTime()---------------

No Description Set


Returns:
float - No Description Set


 .. _CDOTABaseAbility.GetCloneSource:
handle CDOTABaseAbility.GetCloneSource()---------------

No Description Set


Returns:
handle - No Description Set


 .. _CDOTABaseAbility.GetConceptRecipientType:
int CDOTABaseAbility.GetConceptRecipientType()---------------

No Description Set


Returns:
int - No Description Set


 .. _CDOTABaseAbility.GetCooldown:
float CDOTABaseAbility.GetCooldown(int a)---------------

Get the cooldown duration for this ability at a given level, not the amount of cooldown actually left.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
float - No Description Set


 .. _CDOTABaseAbility.GetCooldownTime:
float CDOTABaseAbility.GetCooldownTime()---------------

No Description Set


Returns:
float - No Description Set


 .. _CDOTABaseAbility.GetCooldownTimeRemaining:
float CDOTABaseAbility.GetCooldownTimeRemaining()---------------

No Description Set


Returns:
float - No Description Set


 .. _CDOTABaseAbility.GetCursorPosition:
Vector CDOTABaseAbility.GetCursorPosition()---------------

No Description Set


Returns:
Vector - No Description Set


 .. _CDOTABaseAbility.GetCursorTarget:
handle CDOTABaseAbility.GetCursorTarget()---------------

No Description Set


Returns:
handle - No Description Set


 .. _CDOTABaseAbility.GetCursorTargetingNothing:
bool CDOTABaseAbility.GetCursorTargetingNothing()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTABaseAbility.GetDuration:
float CDOTABaseAbility.GetDuration()---------------

No Description Set


Returns:
float - No Description Set


 .. _CDOTABaseAbility.GetGoldCost:
int CDOTABaseAbility.GetGoldCost(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTABaseAbility.GetGoldCostForUpgrade:
int CDOTABaseAbility.GetGoldCostForUpgrade(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTABaseAbility.GetHeroLevelRequiredToUpgrade:
int CDOTABaseAbility.GetHeroLevelRequiredToUpgrade()---------------

No Description Set


Returns:
int - No Description Set


 .. _CDOTABaseAbility.GetIntrinsicModifierName:
string CDOTABaseAbility.GetIntrinsicModifierName()---------------

No Description Set


Returns:
string - No Description Set


 .. _CDOTABaseAbility.GetLevel:
int CDOTABaseAbility.GetLevel()---------------

Get the current level of the ability


Returns:
int - No Description Set


 .. _CDOTABaseAbility.GetLevelSpecialValueFor:
table CDOTABaseAbility.GetLevelSpecialValueFor(string a, int b)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
table - No Description Set


 .. _CDOTABaseAbility.GetManaCost:
int CDOTABaseAbility.GetManaCost(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTABaseAbility.GetMaxLevel:
int CDOTABaseAbility.GetMaxLevel()---------------

No Description Set


Returns:
int - No Description Set


 .. _CDOTABaseAbility.GetModifierValue:
float CDOTABaseAbility.GetModifierValue()---------------

No Description Set


Returns:
float - No Description Set


 .. _CDOTABaseAbility.GetModifierValueBonus:
float CDOTABaseAbility.GetModifierValueBonus()---------------

No Description Set


Returns:
float - No Description Set


 .. _CDOTABaseAbility.GetPlaybackRateOverride:
float CDOTABaseAbility.GetPlaybackRateOverride()---------------

No Description Set


Returns:
float - No Description Set


 .. _CDOTABaseAbility.GetSharedCooldownName:
string CDOTABaseAbility.GetSharedCooldownName()---------------

No Description Set


Returns:
string - No Description Set


 .. _CDOTABaseAbility.GetSpecialValueFor:
table CDOTABaseAbility.GetSpecialValueFor(string a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
+-----------+--------------+--------------+
Returns:
table - No Description Set


 .. _CDOTABaseAbility.GetStolenActivityModifier:
string CDOTABaseAbility.GetStolenActivityModifier()---------------

No Description Set


Returns:
string - No Description Set


 .. _CDOTABaseAbility.GetToggleState:
bool CDOTABaseAbility.GetToggleState()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTABaseAbility.HeroXPChange:
bool CDOTABaseAbility.HeroXPChange(float a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _CDOTABaseAbility.IncrementModifierRefCount:
void CDOTABaseAbility.IncrementModifierRefCount()---------------

No Description Set




 .. _CDOTABaseAbility.IsActivated:
bool CDOTABaseAbility.IsActivated()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTABaseAbility.IsAttributeBonus:
bool CDOTABaseAbility.IsAttributeBonus()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTABaseAbility.IsChanneling:
bool CDOTABaseAbility.IsChanneling()---------------

Returns whether the ability is currently channeling.


Returns:
bool - No Description Set


 .. _CDOTABaseAbility.IsCooldownReady:
bool CDOTABaseAbility.IsCooldownReady()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTABaseAbility.IsCosmetic:
bool CDOTABaseAbility.IsCosmetic()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTABaseAbility.IsFullyCastable:
bool CDOTABaseAbility.IsFullyCastable()---------------

Returns whether the ability can be cast.


Returns:
bool - No Description Set


 .. _CDOTABaseAbility.IsHidden:
bool CDOTABaseAbility.IsHidden()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTABaseAbility.IsHiddenWhenStolen:
bool CDOTABaseAbility.IsHiddenWhenStolen()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTABaseAbility.IsInAbilityPhase:
bool CDOTABaseAbility.IsInAbilityPhase()---------------

Returns whether the ability is currently casting.


Returns:
bool - No Description Set


 .. _CDOTABaseAbility.IsItem:
bool CDOTABaseAbility.IsItem()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTABaseAbility.IsOwnersGoldEnough:
bool CDOTABaseAbility.IsOwnersGoldEnough(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _CDOTABaseAbility.IsOwnersGoldEnoughForUpgrade:
bool CDOTABaseAbility.IsOwnersGoldEnoughForUpgrade()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTABaseAbility.IsOwnersManaEnough:
bool CDOTABaseAbility.IsOwnersManaEnough()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTABaseAbility.IsPassive:
bool CDOTABaseAbility.IsPassive()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTABaseAbility.IsSharedWithTeammates:
bool CDOTABaseAbility.IsSharedWithTeammates()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTABaseAbility.IsStealable:
bool CDOTABaseAbility.IsStealable()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTABaseAbility.IsStolen:
bool CDOTABaseAbility.IsStolen()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTABaseAbility.IsToggle:
bool CDOTABaseAbility.IsToggle()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTABaseAbility.IsTrained:
bool CDOTABaseAbility.IsTrained()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTABaseAbility.MarkAbilityButtonDirty:
void CDOTABaseAbility.MarkAbilityButtonDirty()---------------

Mark the ability button for this ability as needing a refresh




 .. _CDOTABaseAbility.NumModifiersUsingAbility:
int CDOTABaseAbility.NumModifiersUsingAbility()---------------

No Description Set


Returns:
int - No Description Set


 .. _CDOTABaseAbility.OnAbilityPhaseInterrupted:
void CDOTABaseAbility.OnAbilityPhaseInterrupted()---------------

No Description Set




 .. _CDOTABaseAbility.OnAbilityPhaseStart:
bool CDOTABaseAbility.OnAbilityPhaseStart()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTABaseAbility.OnAbilityPinged:
void CDOTABaseAbility.OnAbilityPinged()---------------

No Description Set




 .. _CDOTABaseAbility.OnChannelFinish:
void CDOTABaseAbility.OnChannelFinish(bool a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseAbility.OnChannelThink:
void CDOTABaseAbility.OnChannelThink(float a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseAbility.OnHeroCalculateStatBonus:
void CDOTABaseAbility.OnHeroCalculateStatBonus()---------------

No Description Set




 .. _CDOTABaseAbility.OnHeroLevelUp:
void CDOTABaseAbility.OnHeroLevelUp()---------------

No Description Set




 .. _CDOTABaseAbility.OnInventoryContentsChanged:
void CDOTABaseAbility.OnInventoryContentsChanged()---------------

No Description Set




 .. _CDOTABaseAbility.OnOwnerDied:
void CDOTABaseAbility.OnOwnerDied()---------------

No Description Set




 .. _CDOTABaseAbility.OnOwnerSpawned:
void CDOTABaseAbility.OnOwnerSpawned()---------------

No Description Set




 .. _CDOTABaseAbility.OnSpellStart:
void CDOTABaseAbility.OnSpellStart()---------------

No Description Set




 .. _CDOTABaseAbility.OnToggle:
void CDOTABaseAbility.OnToggle()---------------

No Description Set




 .. _CDOTABaseAbility.OnUpgrade:
void CDOTABaseAbility.OnUpgrade()---------------

No Description Set




 .. _CDOTABaseAbility.PayGoldCost:
void CDOTABaseAbility.PayGoldCost()---------------

No Description Set




 .. _CDOTABaseAbility.PayGoldCostForUpgrade:
void CDOTABaseAbility.PayGoldCostForUpgrade()---------------

No Description Set




 .. _CDOTABaseAbility.PayManaCost:
void CDOTABaseAbility.PayManaCost()---------------

No Description Set




 .. _CDOTABaseAbility.PlaysDefaultAnimWhenStolen:
bool CDOTABaseAbility.PlaysDefaultAnimWhenStolen()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTABaseAbility.ProcsMagicStick:
bool CDOTABaseAbility.ProcsMagicStick()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTABaseAbility.RefCountsModifiers:
bool CDOTABaseAbility.RefCountsModifiers()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTABaseAbility.RefundManaCost:
void CDOTABaseAbility.RefundManaCost()---------------

No Description Set




 .. _CDOTABaseAbility.ResetToggleOnRespawn:
bool CDOTABaseAbility.ResetToggleOnRespawn()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTABaseAbility.SetAbilityIndex:
void CDOTABaseAbility.SetAbilityIndex(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseAbility.SetActivated:
void CDOTABaseAbility.SetActivated(bool a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseAbility.SetChanneling:
void CDOTABaseAbility.SetChanneling(bool a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseAbility.SetHidden:
void CDOTABaseAbility.SetHidden(bool a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseAbility.SetInAbilityPhase:
void CDOTABaseAbility.SetInAbilityPhase(bool a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseAbility.SetLevel:
void CDOTABaseAbility.SetLevel(int a)---------------

Sets the level of this ability.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseAbility.SetOverrideCastPoint:
void CDOTABaseAbility.SetOverrideCastPoint(float a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseAbility.SetRefCountsModifiers:
void CDOTABaseAbility.SetRefCountsModifiers(bool a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseAbility.SetStolen:
void CDOTABaseAbility.SetStolen(bool a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseAbility.ShouldUseResources:
bool CDOTABaseAbility.ShouldUseResources()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTABaseAbility.SpeakAbilityConcept:
void CDOTABaseAbility.SpeakAbilityConcept(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseAbility.SpeakTrigger:
bool CDOTABaseAbility.SpeakTrigger()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTABaseAbility.StartCooldown:
void CDOTABaseAbility.StartCooldown(float a)---------------

param: flCooldown


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseAbility.ToggleAbility:
void CDOTABaseAbility.ToggleAbility()---------------

No Description Set




 .. _CDOTABaseAbility.ToggleAutoCast:
void CDOTABaseAbility.ToggleAutoCast()---------------

No Description Set




 .. _CDOTABaseAbility.UpgradeAbility:
void CDOTABaseAbility.UpgradeAbility()---------------

No Description Set




 .. _CDOTABaseAbility.UseResources:
void CDOTABaseAbility.UseResources(bool a, bool b, bool c)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  bool |  | No Description Set |
|  bool |  | No Description Set |
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_Ability_Animation_Attack.SetPlaybackRate:
void CDOTA_Ability_Animation_Attack.SetPlaybackRate(float a)---------------

Override playbackrate


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_Ability_Animation_TailSpin.SetPlaybackRate:
void CDOTA_Ability_Animation_TailSpin.SetPlaybackRate(float a)---------------

Override playbackrate


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_Ability_Nian_Leap.SetPlaybackRate:
void CDOTA_Ability_Nian_Leap.SetPlaybackRate(float a)---------------

Override playbackrate


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_Ability_Nian_Dive.SetPlaybackRate:
void CDOTA_Ability_Nian_Dive.SetPlaybackRate(float a)---------------

Override playbackrate


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_Ability_Nian_Roar.GetCastCount:
int CDOTA_Ability_Nian_Roar.GetCastCount()---------------

Number of times Nian has used the roar


Returns:
int - No Description Set


 .. _CDOTA_Item.GetContainer:
handle CDOTA_Item.GetContainer()---------------

Get the container for this item.


Returns:
handle - No Description Set


 .. _CDOTA_Item.GetCost:
int CDOTA_Item.GetCost()---------------

No Description Set


Returns:
int - No Description Set


 .. _CDOTA_Item.GetCurrentCharges:
int CDOTA_Item.GetCurrentCharges()---------------

Get the number of charges this item currently has.


Returns:
int - No Description Set


 .. _CDOTA_Item.GetInitialCharges:
int CDOTA_Item.GetInitialCharges()---------------

Get the initial number of charges this item has.


Returns:
int - No Description Set


 .. _CDOTA_Item.GetPurchaser:
handle CDOTA_Item.GetPurchaser()---------------

Get the purchaser for this item.


Returns:
handle - No Description Set


 .. _CDOTA_Item.GetPurchaseTime:
float CDOTA_Item.GetPurchaseTime()---------------

Get the purchase time of this item


Returns:
float - No Description Set


 .. _CDOTA_Item.GetShareability:
int CDOTA_Item.GetShareability()---------------

No Description Set


Returns:
int - No Description Set


 .. _CDOTA_Item.IsPermanent:
bool CDOTA_Item.IsPermanent()---------------

Is this a permanent item?


Returns:
bool - No Description Set


 .. _CDOTA_Item.LaunchLoot:
void CDOTA_Item.LaunchLoot(bool a, float b, float c, Vector d)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  bool |  | No Description Set |
|  float |  | No Description Set |
|  float |  | No Description Set |
|  Vector |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_Item.SetCurrentCharges:
void CDOTA_Item.SetCurrentCharges(int a)---------------

Set the number of charges on this item


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_Item.SetPurchaser:
void CDOTA_Item.SetPurchaser(handle a)---------------

Set the purchaser of record for this item.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_Item.SetPurchaseTime:
void CDOTA_Item.SetPurchaseTime(float a)---------------

Set the purchase time of this item


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_Item.SetStacksWithOtherOwners:
void CDOTA_Item.SetStacksWithOtherOwners(bool a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_Item.StacksWithOtherOwners:
bool CDOTA_Item.StacksWithOtherOwners()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_Item.Think:
void CDOTA_Item.Think()---------------

Think this item




 .. _CDOTA_Item_Physical.GetContainedItem:
handle CDOTA_Item_Physical.GetContainedItem()---------------

Returned the contained item.


Returns:
handle - No Description Set


 .. _CDOTA_Item_Physical.GetCreationTime:
float CDOTA_Item_Physical.GetCreationTime()---------------

Returns the game time when this item was created in the world


Returns:
float - No Description Set


 .. _CDOTA_Item_Physical.SetContainedItem:
void CDOTA_Item_Physical.SetContainedItem(handle a)---------------

Set the contained item.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_Item_DataDriven.ApplyDataDrivenModifier:
void CDOTA_Item_DataDriven.ApplyDataDrivenModifier(handle source, handle target, string modifier_name, handle modifierArgs)---------------




+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle | source | No Description Set |
|  handle | target | No Description Set |
|  string | modifier_name | No Description Set |
|  handle | modifierArgs | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_Unit_Nian.GetHorn:
handle CDOTA_Unit_Nian.GetHorn()---------------

Is the Nian horn?


Returns:
handle - No Description Set


 .. _CDOTA_Unit_Nian.GetTail:
handle CDOTA_Unit_Nian.GetTail()---------------

Is the Nian's tail broken?


Returns:
handle - No Description Set


 .. _CDOTA_Unit_Nian.IsHornAlive:
bool CDOTA_Unit_Nian.IsHornAlive()---------------

Is the Nian's horn broken?


Returns:
bool - No Description Set


 .. _CDOTA_Unit_Nian.IsTailAlive:
bool CDOTA_Unit_Nian.IsTailAlive()---------------

Is the Nian's tail broken?


Returns:
bool - No Description Set


 .. _CBasePlayer.IsNoclipping:
bool CBasePlayer.IsNoclipping()---------------

Returns true if the player is in noclip mode.


Returns:
bool - No Description Set


 .. _CDOTAPlayer.GetAssignedHero:
handle CDOTAPlayer.GetAssignedHero()---------------

Get the player's hero.


Returns:
handle - No Description Set


 .. _CDOTAPlayer.GetControlledRPGUnit:
handle CDOTAPlayer.GetControlledRPGUnit()---------------

Get the RPG unit this player controls.


Returns:
handle - No Description Set


 .. _CDOTAPlayer.GetPlayerID:
int CDOTAPlayer.GetPlayerID()---------------

Get the player's official PlayerID; notably is -1 when the player isn't yet on a team.


Returns:
int - No Description Set


 .. _CDOTAPlayer.MakeRandomHeroSelection:
void CDOTAPlayer.MakeRandomHeroSelection()---------------

Randoms this player's hero.




 .. _CDOTAPlayer.SetKillCamUnit:
void CDOTAPlayer.SetKillCamUnit(handle a)---------------

Set the kill cam unit for this hero.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTAPlayer.SetMusicStatus:
void CDOTAPlayer.SetMusicStatus(int nMusicStatus, float flIntensity)---------------

Set the music status for this player, note this will only really apply if dota_music_battle_enable is off.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int | nMusicStatus | Status flag of the Music |
|  float | flIntensity | Intensity of the music |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.AddAegisPickup:
void CDOTA_PlayerResource.AddAegisPickup(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.AddClaimedFarm:
void CDOTA_PlayerResource.AddClaimedFarm(int a, float b)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.AddGoldSpentOnSupport:
void CDOTA_PlayerResource.AddGoldSpentOnSupport(int a, int b)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.AddRunePickup:
void CDOTA_PlayerResource.AddRunePickup(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.AreUnitsSharedWithPlayerID:
bool CDOTA_PlayerResource.AreUnitsSharedWithPlayerID(int a, int b)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _CDOTA_PlayerResource.ClearKillsMatrix:
void CDOTA_PlayerResource.ClearKillsMatrix(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.ClearLastHitMultikill:
void CDOTA_PlayerResource.ClearLastHitMultikill(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.ClearLastHitStreak:
void CDOTA_PlayerResource.ClearLastHitStreak(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.ClearRawPlayerDamageMatrix:
void CDOTA_PlayerResource.ClearRawPlayerDamageMatrix(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.ClearStreak:
void CDOTA_PlayerResource.ClearStreak(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.GetAegisPickups:
int CDOTA_PlayerResource.GetAegisPickups(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetAssists:
int CDOTA_PlayerResource.GetAssists(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetBroadcasterChannel:
<> CDOTA_PlayerResource.GetBroadcasterChannel(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
<> - No Description Set


 .. _CDOTA_PlayerResource.GetBroadcasterChannelSlot:
<> CDOTA_PlayerResource.GetBroadcasterChannelSlot(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
<> - No Description Set


 .. _CDOTA_PlayerResource.GetClaimedDenies:
int CDOTA_PlayerResource.GetClaimedDenies(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetClaimedFarm:
float CDOTA_PlayerResource.GetClaimedFarm(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
float - No Description Set


 .. _CDOTA_PlayerResource.GetClaimedMisses:
int CDOTA_PlayerResource.GetClaimedMisses(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetConnectionState:
<> CDOTA_PlayerResource.GetConnectionState(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
<> - No Description Set


 .. _CDOTA_PlayerResource.GetCreepDamageTaken:
int CDOTA_PlayerResource.GetCreepDamageTaken(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetCustomBuybackCooldown:
float CDOTA_PlayerResource.GetCustomBuybackCooldown(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
float - No Description Set


 .. _CDOTA_PlayerResource.GetCustomBuybackCost:
int CDOTA_PlayerResource.GetCustomBuybackCost(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetDamageDoneToHero:
int CDOTA_PlayerResource.GetDamageDoneToHero(int a, int b)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetDeaths:
int CDOTA_PlayerResource.GetDeaths(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetDenies:
int CDOTA_PlayerResource.GetDenies(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetEventPointsForPlayerID:
int CDOTA_PlayerResource.GetEventPointsForPlayerID(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetEventPremiumPointsGranted:
int CDOTA_PlayerResource.GetEventPremiumPointsGranted(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetEventRankGranted:
int CDOTA_PlayerResource.GetEventRankGranted(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetGold:
int CDOTA_PlayerResource.GetGold(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetGoldBagsCollected:
int CDOTA_PlayerResource.GetGoldBagsCollected(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetGoldLostToDeath:
int CDOTA_PlayerResource.GetGoldLostToDeath(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetGoldPerMin:
float CDOTA_PlayerResource.GetGoldPerMin(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
float - No Description Set


 .. _CDOTA_PlayerResource.GetGoldSpentOnBuybacks:
int CDOTA_PlayerResource.GetGoldSpentOnBuybacks(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetGoldSpentOnConsumables:
int CDOTA_PlayerResource.GetGoldSpentOnConsumables(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetGoldSpentOnItems:
int CDOTA_PlayerResource.GetGoldSpentOnItems(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetGoldSpentOnSupport:
int CDOTA_PlayerResource.GetGoldSpentOnSupport(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetHealing:
float CDOTA_PlayerResource.GetHealing(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
float - No Description Set


 .. _CDOTA_PlayerResource.GetHeroDamageTaken:
int CDOTA_PlayerResource.GetHeroDamageTaken(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetKills:
int CDOTA_PlayerResource.GetKills(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetKillsDoneToHero:
int CDOTA_PlayerResource.GetKillsDoneToHero(int a, int b)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetLastHitMultikill:
int CDOTA_PlayerResource.GetLastHitMultikill(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetLastHits:
int CDOTA_PlayerResource.GetLastHits(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetLastHitStreak:
int CDOTA_PlayerResource.GetLastHitStreak(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetLevel:
int CDOTA_PlayerResource.GetLevel(int playerID)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int | playerID | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetMisses:
int CDOTA_PlayerResource.GetMisses(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetNearbyCreepDeaths:
int CDOTA_PlayerResource.GetNearbyCreepDeaths(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetNthCourierForTeam:
handle CDOTA_PlayerResource.GetNthCourierForTeam(int a, int b)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _CDOTA_PlayerResource.GetNthPlayerIDOnTeam:
int CDOTA_PlayerResource.GetNthPlayerIDOnTeam(int a, int b)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetNumConsumablesPurchased:
int CDOTA_PlayerResource.GetNumConsumablesPurchased(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetNumCouriersForTeam:
int CDOTA_PlayerResource.GetNumCouriersForTeam(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetNumItemsPurchased:
int CDOTA_PlayerResource.GetNumItemsPurchased(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetPlayer:
handle CDOTA_PlayerResource.GetPlayer(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _CDOTA_PlayerResource.GetPlayerLoadedCompletely:
bool CDOTA_PlayerResource.GetPlayerLoadedCompletely(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _CDOTA_PlayerResource.GetPlayerName:
string CDOTA_PlayerResource.GetPlayerName(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
string - No Description Set


 .. _CDOTA_PlayerResource.GetPlayerReservedState:
bool CDOTA_PlayerResource.GetPlayerReservedState(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _CDOTA_PlayerResource.GetRawPlayerDamage:
int CDOTA_PlayerResource.GetRawPlayerDamage(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetReliableGold:
int CDOTA_PlayerResource.GetReliableGold(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetRespawnSeconds:
int CDOTA_PlayerResource.GetRespawnSeconds(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetRoshanKills:
int CDOTA_PlayerResource.GetRoshanKills(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetRunePickups:
int CDOTA_PlayerResource.GetRunePickups(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetSelectedHeroEntity:
handle CDOTA_PlayerResource.GetSelectedHeroEntity(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _CDOTA_PlayerResource.GetSelectedHeroID:
int CDOTA_PlayerResource.GetSelectedHeroID(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetSelectedHeroName:
string CDOTA_PlayerResource.GetSelectedHeroName(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
string - No Description Set


 .. _CDOTA_PlayerResource.GetSteamAccountID:
<> CDOTA_PlayerResource.GetSteamAccountID(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
<> - No Description Set


 .. _CDOTA_PlayerResource.GetStreak:
int CDOTA_PlayerResource.GetStreak(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetStuns:
float CDOTA_PlayerResource.GetStuns(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
float - No Description Set


 .. _CDOTA_PlayerResource.GetTeam:
int CDOTA_PlayerResource.GetTeam(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetTeamKills:
int CDOTA_PlayerResource.GetTeamKills(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetTimeOfLastConsumablePurchase:
float CDOTA_PlayerResource.GetTimeOfLastConsumablePurchase(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
float - No Description Set


 .. _CDOTA_PlayerResource.GetTimeOfLastDeath:
float CDOTA_PlayerResource.GetTimeOfLastDeath(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
float - No Description Set


 .. _CDOTA_PlayerResource.GetTimeOfLastItemPurchase:
float CDOTA_PlayerResource.GetTimeOfLastItemPurchase(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
float - No Description Set


 .. _CDOTA_PlayerResource.GetTotalEarnedGold:
int CDOTA_PlayerResource.GetTotalEarnedGold(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetTotalEarnedXP:
int CDOTA_PlayerResource.GetTotalEarnedXP(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetTotalGoldSpent:
int CDOTA_PlayerResource.GetTotalGoldSpent(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetTowerDamageTaken:
int CDOTA_PlayerResource.GetTowerDamageTaken(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetTowerKills:
int CDOTA_PlayerResource.GetTowerKills(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetUnitShareMaskForPlayer:
int CDOTA_PlayerResource.GetUnitShareMaskForPlayer(int a, int b)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetUnreliableGold:
int CDOTA_PlayerResource.GetUnreliableGold(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetXPPerMin:
float CDOTA_PlayerResource.GetXPPerMin(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
float - No Description Set


 .. _CDOTA_PlayerResource.HasRandomed:
bool CDOTA_PlayerResource.HasRandomed(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _CDOTA_PlayerResource.HasRepicked:
bool CDOTA_PlayerResource.HasRepicked(int playerID)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int | playerID | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _CDOTA_PlayerResource.HasSelectedHero:
bool CDOTA_PlayerResource.HasSelectedHero(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _CDOTA_PlayerResource.HaveAllPlayersJoined:
bool CDOTA_PlayerResource.HaveAllPlayersJoined()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_PlayerResource.HeroLevelUp:
void CDOTA_PlayerResource.HeroLevelUp(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.IncrementAssists:
void CDOTA_PlayerResource.IncrementAssists(int playerID)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int | playerID | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.IncrementClaimedDenies:
void CDOTA_PlayerResource.IncrementClaimedDenies(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.IncrementClaimedMisses:
void CDOTA_PlayerResource.IncrementClaimedMisses(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.IncrementDeaths:
void CDOTA_PlayerResource.IncrementDeaths(int playerID)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int | playerID | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.IncrementDenies:
void CDOTA_PlayerResource.IncrementDenies(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.IncrementGoldBagsCollected:
void CDOTA_PlayerResource.IncrementGoldBagsCollected(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.IncrementKills:
void CDOTA_PlayerResource.IncrementKills(int playerID, int kills)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int | playerID | No Description Set |
|  int | kills | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.IncrementLastHitMultikill:
void CDOTA_PlayerResource.IncrementLastHitMultikill(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.IncrementLastHits:
void CDOTA_PlayerResource.IncrementLastHits(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.IncrementLastHitStreak:
void CDOTA_PlayerResource.IncrementLastHitStreak(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.IncrementMisses:
void CDOTA_PlayerResource.IncrementMisses(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.IncrementNearbyCreepDeaths:
void CDOTA_PlayerResource.IncrementNearbyCreepDeaths(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.IncrementStreak:
void CDOTA_PlayerResource.IncrementStreak(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.IncrementTotalEarnedXP:
void CDOTA_PlayerResource.IncrementTotalEarnedXP(int a, int b)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.IsBroadcaster:
bool CDOTA_PlayerResource.IsBroadcaster(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _CDOTA_PlayerResource.IsDisableHelpSetForPlayerID:
bool CDOTA_PlayerResource.IsDisableHelpSetForPlayerID(int a, int b)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _CDOTA_PlayerResource.IsFakeClient:
bool CDOTA_PlayerResource.IsFakeClient(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _CDOTA_PlayerResource.IsHeroSelected:
bool CDOTA_PlayerResource.IsHeroSelected(string a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _CDOTA_PlayerResource.IsHeroSharedWithPlayerID:
bool CDOTA_PlayerResource.IsHeroSharedWithPlayerID(int a, int b)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _CDOTA_PlayerResource.IsValidPlayer:
bool CDOTA_PlayerResource.IsValidPlayer(int playerID)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int | playerID | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _CDOTA_PlayerResource.IsValidPlayerID:
bool CDOTA_PlayerResource.IsValidPlayerID(int playerID)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int | playerID | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _CDOTA_PlayerResource.IsValidTeamPlayer:
bool CDOTA_PlayerResource.IsValidTeamPlayer(int playerID)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int | playerID | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _CDOTA_PlayerResource.IsValidTeamPlayerID:
bool CDOTA_PlayerResource.IsValidTeamPlayerID(int playerID)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int | playerID | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _CDOTA_PlayerResource.ModifyGold:
int CDOTA_PlayerResource.ModifyGold(int playerID, int goldAmmt, bool reliable, int d)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int | playerID | No Description Set |
|  int | goldAmmt | No Description Set |
|  bool | reliable | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.ReplaceHeroWith:
handle CDOTA_PlayerResource.ReplaceHeroWith(int a, string b, int c, int d)---------------

(playerID, heroClassName, gold, XP) - replaces the player's hero with a new one of the specified class, gold and XP


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
|  string |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _CDOTA_PlayerResource.ResetBuybackCostTime:
void CDOTA_PlayerResource.ResetBuybackCostTime(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.ResetTotalEarnedGold:
void CDOTA_PlayerResource.ResetTotalEarnedGold(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.SetBuybackCooldownTime:
void CDOTA_PlayerResource.SetBuybackCooldownTime(int a, float b)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.SetBuybackGoldLimitTime:
void CDOTA_PlayerResource.SetBuybackGoldLimitTime(int a, float b)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.SetCameraTarget:
void CDOTA_PlayerResource.SetCameraTarget(int a, handle b)---------------

(playerID, entity) - force the given player's camera to follow the given entity


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.SetCustomBuybackCooldown:
void CDOTA_PlayerResource.SetCustomBuybackCooldown(int a, float b)---------------

Set the buyback cooldown for this player.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.SetCustomBuybackCost:
void CDOTA_PlayerResource.SetCustomBuybackCost(int a, int b)---------------

Set the buyback cost for this player.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.SetGold:
void CDOTA_PlayerResource.SetGold(int a, int b, bool c)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
|  int |  | No Description Set |
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.SetHasRandomed:
void CDOTA_PlayerResource.SetHasRandomed(int playerID)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int | playerID | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.SetHasRepicked:
void CDOTA_PlayerResource.SetHasRepicked(int playerID)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int | playerID | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.SetLastBuybackTime:
void CDOTA_PlayerResource.SetLastBuybackTime(int a, int b)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.SetPlayerReservedState:
void CDOTA_PlayerResource.SetPlayerReservedState(int a, bool b)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.SetUnitShareMaskForPlayer:
void CDOTA_PlayerResource.SetUnitShareMaskForPlayer(int a, int b, int c, bool d)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.SpendGold:
void CDOTA_PlayerResource.SpendGold(int a, int b, int c)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.UpdateTeamSlot:
void CDOTA_PlayerResource.UpdateTeamSlot(int a, int b)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.WhoSelectedHero:
int CDOTA_PlayerResource.WhoSelectedHero(string a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_BaseNPC.AddAbility:
void CDOTA_BaseNPC.AddAbility(string a)---------------

Add an ability to this unit by name.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.AddItem:
void CDOTA_BaseNPC.AddItem(handle a)---------------

Add an item to this unit's inventory.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.AddNewModifier:
void CDOTA_BaseNPC.AddNewModifier(handle caster, handle optionalSourceAbility, string modifierName, handle modifierData)---------------




+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle | caster | No Description Set |
|  handle | optionalSourceAbility | No Description Set |
|  string | modifierName | No Description Set |
|  handle | modifierData | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.AddNoDraw:
void CDOTA_BaseNPC.AddNoDraw()---------------

Adds the no draw flag.




 .. _CDOTA_BaseNPC.AlertNearbyUnits:
void CDOTA_BaseNPC.AlertNearbyUnits(handle a, handle b)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.AngerNearbyUnits:
void CDOTA_BaseNPC.AngerNearbyUnits()---------------

No Description Set




 .. _CDOTA_BaseNPC.AttackNoEarlierThan:
void CDOTA_BaseNPC.AttackNoEarlierThan(float a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.AttackReady:
bool CDOTA_BaseNPC.AttackReady()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.BoundingRadius2D:
float CDOTA_BaseNPC.BoundingRadius2D()---------------

No Description Set


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.CastAbilityImmediately:
void CDOTA_BaseNPC.CastAbilityImmediately(handle a, int b)---------------

Cast an ability immediately.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.CastAbilityNoTarget:
void CDOTA_BaseNPC.CastAbilityNoTarget(handle ability, int playerIndex)---------------

Cast an ability with no target. ( hAbility, iPlayerIndex )


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle | ability | No Description Set |
|  int | playerIndex | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.CastAbilityOnPosition:
void CDOTA_BaseNPC.CastAbilityOnPosition(Vector a, handle b, int c)---------------

Cast an ability on a position.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector |  | No Description Set |
|  handle |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.CastAbilityOnTarget:
void CDOTA_BaseNPC.CastAbilityOnTarget(handle target, handle ability, int playerIndex)---------------

Cast an ability on a target entity.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle | target | No Description Set |
|  handle | ability | No Description Set |
|  int | playerIndex | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.CastAbilityToggle:
void CDOTA_BaseNPC.CastAbilityToggle(handle a, int b)---------------

Toggle an ability. ( hAbility, iPlayerIndex )


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.DisassembleItem:
void CDOTA_BaseNPC.DisassembleItem(handle a)---------------

Disassemble the passed item in this unit's inventory.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.DropItemAtPosition:
void CDOTA_BaseNPC.DropItemAtPosition(Vector a, handle b)---------------

Drop an item at a given point.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.DropItemAtPositionImmediate:
void CDOTA_BaseNPC.DropItemAtPositionImmediate(handle a, Vector b)---------------

Immediately drop a carried item at a given position.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
|  Vector |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.EjectItemFromStash:
void CDOTA_BaseNPC.EjectItemFromStash(handle a)---------------

Drops the selected item out of this unit's stash.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.FindAbilityByName:
handle CDOTA_BaseNPC.FindAbilityByName(string a)---------------

Retrieve an ability by name from the unit.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _CDOTA_BaseNPC.ForceKill:
void CDOTA_BaseNPC.ForceKill(bool a)---------------

Kill this unit immediately.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.GetAbilityByIndex:
handle CDOTA_BaseNPC.GetAbilityByIndex(int a)---------------

Retrieve an ability by index from the unit.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _CDOTA_BaseNPC.GetAbilityCount:
int CDOTA_BaseNPC.GetAbilityCount()---------------

No Description Set


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC.GetAcquisitionRange:
float CDOTA_BaseNPC.GetAcquisitionRange()---------------

Gets the range at which this unit will auto-acquire.


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetAdditionalBattleMusicWeight:
float CDOTA_BaseNPC.GetAdditionalBattleMusicWeight()---------------

Combat involving this creature will have this weight added to the music calcuations


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetAttackAnimationPoint:
float CDOTA_BaseNPC.GetAttackAnimationPoint()---------------

No Description Set


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetAttackDamage:
int CDOTA_BaseNPC.GetAttackDamage()---------------

Returns a random integer between the minimum and maximum base damage of the unit.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC.GetAttackRange:
float CDOTA_BaseNPC.GetAttackRange()---------------

Gets this unit's attack range after all modifiers.


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetAttackRangeBuffer:
float CDOTA_BaseNPC.GetAttackRangeBuffer()---------------

Gets the attack range buffer.


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetAttackSpeed:
float CDOTA_BaseNPC.GetAttackSpeed()---------------

No Description Set


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetAttacksPerSecond:
float CDOTA_BaseNPC.GetAttacksPerSecond()---------------

No Description Set


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetAttackTarget:
handle CDOTA_BaseNPC.GetAttackTarget()---------------

No Description Set


Returns:
handle - No Description Set


 .. _CDOTA_BaseNPC.GetAverageTrueAttackDamage:
int CDOTA_BaseNPC.GetAverageTrueAttackDamage()---------------

Returns the average value of the minimum and maximum damage values.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC.GetBaseAttackRange:
int CDOTA_BaseNPC.GetBaseAttackRange()---------------

Gets this unit's attack range before modifiers.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC.GetBaseAttackTime:
float CDOTA_BaseNPC.GetBaseAttackTime()---------------

No Description Set


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetBaseDamageMax:
int CDOTA_BaseNPC.GetBaseDamageMax()---------------

Gets the minimum base damage.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC.GetBaseDamageMin:
int CDOTA_BaseNPC.GetBaseDamageMin()---------------

Gets the minimum base damage.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC.GetBaseDayTimeVisionRange:
int CDOTA_BaseNPC.GetBaseDayTimeVisionRange()---------------

Returns the vision range before modifiers.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC.GetBaseHealthRegen:
float CDOTA_BaseNPC.GetBaseHealthRegen()---------------

No Description Set


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetBaseMagicalResistanceValue:
float CDOTA_BaseNPC.GetBaseMagicalResistanceValue()---------------

Returns base magical armor value.


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetBaseMaxHealth:
float CDOTA_BaseNPC.GetBaseMaxHealth()---------------

Gets the base max health value.


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetBaseMoveSpeed:
float CDOTA_BaseNPC.GetBaseMoveSpeed()---------------

No Description Set


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetBaseNightTimeVisionRange:
int CDOTA_BaseNPC.GetBaseNightTimeVisionRange()---------------

Returns the vision range before modifiers.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC.GetCastPoint:
float CDOTA_BaseNPC.GetCastPoint(bool a)---------------

Parameter: bAttack


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  bool |  | No Description Set |
+-----------+--------------+--------------+
Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetCollisionPadding:
float CDOTA_BaseNPC.GetCollisionPadding()---------------

Returns the size of the collision padding around the hull.


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetConstantBasedManaRegen:
float CDOTA_BaseNPC.GetConstantBasedManaRegen()---------------

This Mana regen is derived from constant bonuses like Basilius.


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetCreationTime:
float CDOTA_BaseNPC.GetCreationTime()---------------

No Description Set


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetCurrentActiveAbility:
handle CDOTA_BaseNPC.GetCurrentActiveAbility()---------------

Get the ability this unit is currently casting.


Returns:
handle - No Description Set


 .. _CDOTA_BaseNPC.GetCurrentVisionRange:
int CDOTA_BaseNPC.GetCurrentVisionRange()---------------

Gets the current vision range.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC.GetCursorCastTarget:
handle CDOTA_BaseNPC.GetCursorCastTarget()---------------

No Description Set


Returns:
handle - No Description Set


 .. _CDOTA_BaseNPC.GetCursorPosition:
Vector CDOTA_BaseNPC.GetCursorPosition()---------------

No Description Set


Returns:
Vector - No Description Set


 .. _CDOTA_BaseNPC.GetCursorTargetingNothing:
bool CDOTA_BaseNPC.GetCursorTargetingNothing()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.GetDayTimeVisionRange:
int CDOTA_BaseNPC.GetDayTimeVisionRange()---------------

Returns the vision range after modifiers.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC.GetDeathXP:
int CDOTA_BaseNPC.GetDeathXP()---------------

Get the XP bounty on this unit


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC.GetForceAttackTarget:
handle CDOTA_BaseNPC.GetForceAttackTarget()---------------

No Description Set


Returns:
handle - No Description Set


 .. _CDOTA_BaseNPC.GetGoldBounty:
int CDOTA_BaseNPC.GetGoldBounty()---------------

Get the gold bounty on this unit


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC.GetHasteFactor:
float CDOTA_BaseNPC.GetHasteFactor()---------------

No Description Set


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetHealth:
int CDOTA_BaseNPC.GetHealth()---------------

Get the health of this unit.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC.GetHealthDeficit:
int CDOTA_BaseNPC.GetHealthDeficit()---------------

Returns integer amount of health missing from max.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC.GetHealthPercent:
int CDOTA_BaseNPC.GetHealthPercent()---------------

Get the current health percent of the unit.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC.GetHealthRegen:
float CDOTA_BaseNPC.GetHealthRegen()---------------

No Description Set


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetHullRadius:
float CDOTA_BaseNPC.GetHullRadius()---------------

Get the collision hull radius of this NPC


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetIdealSpeed:
float CDOTA_BaseNPC.GetIdealSpeed()---------------

Returns speed after all modifiers.


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetIncreasedAttackSpeed:
float CDOTA_BaseNPC.GetIncreasedAttackSpeed()---------------

No Description Set


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetInitialGoalEntity:
handle CDOTA_BaseNPC.GetInitialGoalEntity()---------------

Returns the initial waypoint goal for this NPC


Returns:
handle - No Description Set


 .. _CDOTA_BaseNPC.GetItemInSlot:
handle CDOTA_BaseNPC.GetItemInSlot(int a)---------------

Returns nth item in inventory slot (index is zero based)


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _CDOTA_BaseNPC.GetLastIdleChangeTime:
float CDOTA_BaseNPC.GetLastIdleChangeTime()---------------

Get the last game time that this unit switched to/from idle state.


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetLevel:
int CDOTA_BaseNPC.GetLevel()---------------

Returns the level of this unit.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC.GetMagicalArmorValue:
float CDOTA_BaseNPC.GetMagicalArmorValue()---------------

Returns current magical armor value.


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetMainControllingPlayer:
int CDOTA_BaseNPC.GetMainControllingPlayer()---------------

Returns the player ID of the controlling player.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC.GetMana:
float CDOTA_BaseNPC.GetMana()---------------

Get the mana on this unit.


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetManaPercent:
int CDOTA_BaseNPC.GetManaPercent()---------------

Get the percent of mana remaining.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC.GetManaRegen:
float CDOTA_BaseNPC.GetManaRegen()---------------

No Description Set


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetMaxHealth:
int CDOTA_BaseNPC.GetMaxHealth()---------------

Get the maximum health of this unit.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC.GetMaxMana:
float CDOTA_BaseNPC.GetMaxMana()---------------

Get the maximum mana of this unit.


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetModelRadius:
float CDOTA_BaseNPC.GetModelRadius()---------------

No Description Set


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetModifierCount:
int CDOTA_BaseNPC.GetModifierCount()---------------

How many modifiers does this unit have?


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC.GetModifierNameByIndex:
string CDOTA_BaseNPC.GetModifierNameByIndex(int a)---------------

Get a modifier name by index.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
string - No Description Set


 .. _CDOTA_BaseNPC.GetMoveSpeedModifier:
float CDOTA_BaseNPC.GetMoveSpeedModifier(float a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
+-----------+--------------+--------------+
Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetMustReachEachGoalEntity:
bool CDOTA_BaseNPC.GetMustReachEachGoalEntity()---------------

Get whether this NPC is required to reach each goal entity, rather than being allowed to 'unkink' their path


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.GetNightTimeVisionRange:
int CDOTA_BaseNPC.GetNightTimeVisionRange()---------------

Returns the vision range after modifiers.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC.GetOpposingTeamNumber:
int CDOTA_BaseNPC.GetOpposingTeamNumber()---------------

No Description Set


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC.GetPaddedCollisionRadius:
float CDOTA_BaseNPC.GetPaddedCollisionRadius()---------------

Get the collision hull radius (including padding) of this NPC


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetPercentageBasedManaRegen:
float CDOTA_BaseNPC.GetPercentageBasedManaRegen()---------------

This Mana regen is derived from % bonuses (from items like Void Stone).


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetPhysicalArmorBaseValue:
float CDOTA_BaseNPC.GetPhysicalArmorBaseValue()---------------

Returns base physical armor value.


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetPhysicalArmorValue:
float CDOTA_BaseNPC.GetPhysicalArmorValue()---------------

Returns current physical armor value.


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetPlayerOwner:
handle CDOTA_BaseNPC.GetPlayerOwner()---------------

Returns the player that owns this unit


Returns:
handle - No Description Set


 .. _CDOTA_BaseNPC.GetPlayerOwnerID:
int CDOTA_BaseNPC.GetPlayerOwnerID()---------------

Get the owner player ID for this unit.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC.GetProjectileSpeed:
int CDOTA_BaseNPC.GetProjectileSpeed()---------------

No Description Set


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC.GetRangeToUnit:
float CDOTA_BaseNPC.GetRangeToUnit(handle a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
+-----------+--------------+--------------+
Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetSecondsPerAttack:
float CDOTA_BaseNPC.GetSecondsPerAttack()---------------

No Description Set


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetStatsBasedManaRegen:
float CDOTA_BaseNPC.GetStatsBasedManaRegen()---------------

Returns mana regen rate per intelligence.


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetTeamNumber:
int CDOTA_BaseNPC.GetTeamNumber()---------------

Get the team number of this unit.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC.GetTotalPurchasedUpgradeGoldCost:
int CDOTA_BaseNPC.GetTotalPurchasedUpgradeGoldCost()---------------

Get how much gold has been spent on ability upgrades.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC.GetUnitLabel:
string CDOTA_BaseNPC.GetUnitLabel()---------------

No Description Set


Returns:
string - No Description Set


 .. _CDOTA_BaseNPC.GetUnitName:
string CDOTA_BaseNPC.GetUnitName()---------------

No Description Set


Returns:
string - No Description Set


 .. _CDOTA_BaseNPC.GiveMana:
void CDOTA_BaseNPC.GiveMana(float a)---------------

Give mana to this unit, this can be used for mana gained by abilities or item usage.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.HasAbility:
bool CDOTA_BaseNPC.HasAbility(string a)---------------

See whether this unit has an ability by name.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.HasAttackCapability:
bool CDOTA_BaseNPC.HasAttackCapability()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.HasFlyingVision:
bool CDOTA_BaseNPC.HasFlyingVision()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.HasFlyMovementCapability:
bool CDOTA_BaseNPC.HasFlyMovementCapability()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.HasGroundMovementCapability:
bool CDOTA_BaseNPC.HasGroundMovementCapability()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.HasInventory:
bool CDOTA_BaseNPC.HasInventory()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.HasItemInInventory:
bool CDOTA_BaseNPC.HasItemInInventory(string a)---------------

See whether this unit has an item by name.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.HasModifier:
bool CDOTA_BaseNPC.HasModifier(string a)---------------

Sees if this unit has a given modifier


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.HasMovementCapability:
bool CDOTA_BaseNPC.HasMovementCapability()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.HasScepter:
bool CDOTA_BaseNPC.HasScepter()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.Heal:
void CDOTA_BaseNPC.Heal(float a, handle b)---------------

Heal this unit.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.Hold:
void CDOTA_BaseNPC.Hold()---------------

Hold position.




 .. _CDOTA_BaseNPC.Interrupt:
void CDOTA_BaseNPC.Interrupt()---------------

No Description Set




 .. _CDOTA_BaseNPC.InterruptChannel:
void CDOTA_BaseNPC.InterruptChannel()---------------

No Description Set




 .. _CDOTA_BaseNPC.InterruptMotionControllers:
void CDOTA_BaseNPC.InterruptMotionControllers(bool a)---------------

Parameter boolean determines finding clear space.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.IsAlive:
bool CDOTA_BaseNPC.IsAlive()---------------

Is this unit alive?


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsAncient:
bool CDOTA_BaseNPC.IsAncient()---------------

Is this creature an Ancient?


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsAttackImmune:
bool CDOTA_BaseNPC.IsAttackImmune()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsAttacking:
bool CDOTA_BaseNPC.IsAttacking()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsAttackingEntity:
bool CDOTA_BaseNPC.IsAttackingEntity(handle a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsBlind:
bool CDOTA_BaseNPC.IsBlind()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsBlockDisabled:
bool CDOTA_BaseNPC.IsBlockDisabled()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsCommandRestricted:
bool CDOTA_BaseNPC.IsCommandRestricted()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsControllableByAnyPlayer:
bool CDOTA_BaseNPC.IsControllableByAnyPlayer()---------------

Is this unit controlled by any non-bot player?


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsCreature:
bool CDOTA_BaseNPC.IsCreature()---------------

Is this a Creature type NPC


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsDeniable:
bool CDOTA_BaseNPC.IsDeniable()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsDisarmed:
bool CDOTA_BaseNPC.IsDisarmed()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsDominated:
bool CDOTA_BaseNPC.IsDominated()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsEvadeDisabled:
bool CDOTA_BaseNPC.IsEvadeDisabled()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsFrozen:
bool CDOTA_BaseNPC.IsFrozen()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsHardDisarmed:
bool CDOTA_BaseNPC.IsHardDisarmed()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsHero:
bool CDOTA_BaseNPC.IsHero()---------------

Is this a hero or hero illusion?


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsHexed:
bool CDOTA_BaseNPC.IsHexed()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsIdle:
bool CDOTA_BaseNPC.IsIdle()---------------

Is this creature currently idle?


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsIllusion:
bool CDOTA_BaseNPC.IsIllusion()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsInvisible:
bool CDOTA_BaseNPC.IsInvisible()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsInvulnerable:
bool CDOTA_BaseNPC.IsInvulnerable()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsLowAttackPriority:
bool CDOTA_BaseNPC.IsLowAttackPriority()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsMagicImmune:
bool CDOTA_BaseNPC.IsMagicImmune()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsMechanical:
bool CDOTA_BaseNPC.IsMechanical()---------------

Is the unit mechanical?


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsMovementImpaired:
bool CDOTA_BaseNPC.IsMovementImpaired()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsMuted:
bool CDOTA_BaseNPC.IsMuted()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsNeutralUnitType:
bool CDOTA_BaseNPC.IsNeutralUnitType()---------------

Is this a neutral?


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsNightmared:
bool CDOTA_BaseNPC.IsNightmared()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsOpposingTeam:
bool CDOTA_BaseNPC.IsOpposingTeam(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsOutOfGame:
bool CDOTA_BaseNPC.IsOutOfGame()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsOwnedByAnyPlayer:
bool CDOTA_BaseNPC.IsOwnedByAnyPlayer()---------------

Is this unit owned by any non-bot player?


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsPhantom:
bool CDOTA_BaseNPC.IsPhantom()---------------

Is this a phantom unit?


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsPhantomBlocker:
bool CDOTA_BaseNPC.IsPhantomBlocker()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsPhased:
bool CDOTA_BaseNPC.IsPhased()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsPositionInRange:
bool CDOTA_BaseNPC.IsPositionInRange(Vector a, float b)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsRangedAttacker:
bool CDOTA_BaseNPC.IsRangedAttacker()---------------

Is this unit a ranged attacker?


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsRealHero:
bool CDOTA_BaseNPC.IsRealHero()---------------

Returns true if the hero is a true Hero, not a creep or an Illusion of a hero


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsRooted:
bool CDOTA_BaseNPC.IsRooted()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsSilenced:
bool CDOTA_BaseNPC.IsSilenced()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsSoftDisarmed:
bool CDOTA_BaseNPC.IsSoftDisarmed()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsSpeciallyDeniable:
bool CDOTA_BaseNPC.IsSpeciallyDeniable()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsStunned:
bool CDOTA_BaseNPC.IsStunned()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsSummoned:
bool CDOTA_BaseNPC.IsSummoned()---------------

Is this unit summoned?


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsTower:
bool CDOTA_BaseNPC.IsTower()---------------

Is this a tower?


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsUnableToMiss:
bool CDOTA_BaseNPC.IsUnableToMiss()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsUnselectable:
bool CDOTA_BaseNPC.IsUnselectable()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.Kill:
void CDOTA_BaseNPC.Kill(handle a, handle b)---------------

Kills this NPC, with the params Ability and Attacker


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.MakeIllusion:
void CDOTA_BaseNPC.MakeIllusion()---------------

No Description Set




 .. _CDOTA_BaseNPC.MakePhantomBlocker:
void CDOTA_BaseNPC.MakePhantomBlocker()---------------

No Description Set




 .. _CDOTA_BaseNPC.MakeVisibleDueToAttack:
void CDOTA_BaseNPC.MakeVisibleDueToAttack(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.MakeVisibleToTeam:
void CDOTA_BaseNPC.MakeVisibleToTeam(int a, float b)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.ModifyHealth:
void CDOTA_BaseNPC.ModifyHealth(int a, handle b, bool c, int d)---------------

Sets the health to a specific value, with optional flags or inflictors.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
|  handle |  | No Description Set |
|  bool |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.MoveToNPC:
void CDOTA_BaseNPC.MoveToNPC(handle a)---------------

Move to follow a unit.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.MoveToNPCToGiveItem:
void CDOTA_BaseNPC.MoveToNPCToGiveItem(handle a, handle b)---------------

Give an item to another unit.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.MoveToPosition:
void CDOTA_BaseNPC.MoveToPosition(Vector a)---------------

Issue a Move-To command


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.MoveToPositionAggressive:
void CDOTA_BaseNPC.MoveToPositionAggressive(Vector a)---------------

Issue an Attack-Move-To command


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.MoveToTargetToAttack:
void CDOTA_BaseNPC.MoveToTargetToAttack(handle a)---------------

Move to a target to attack.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.NoHealthBar:
bool CDOTA_BaseNPC.NoHealthBar()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.NoTeamMoveTo:
bool CDOTA_BaseNPC.NoTeamMoveTo()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.NoTeamSelect:
bool CDOTA_BaseNPC.NoTeamSelect()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.NotOnMinimap:
bool CDOTA_BaseNPC.NotOnMinimap()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.NotOnMinimapForEnemies:
bool CDOTA_BaseNPC.NotOnMinimapForEnemies()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.NoUnitCollision:
bool CDOTA_BaseNPC.NoUnitCollision()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.PassivesDisabled:
bool CDOTA_BaseNPC.PassivesDisabled()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.PerformAttack:
void CDOTA_BaseNPC.PerformAttack(handle a, bool b, bool c, bool d, bool e)---------------

Performs an attack on a target. Params: Target, bUseCastAttackOrb, bProcessProcs, bSkipCooldown, bIgnoreInvis


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
|  bool |  | No Description Set |
|  bool |  | No Description Set |
|  bool |  | No Description Set |
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.PickupDroppedItem:
void CDOTA_BaseNPC.PickupDroppedItem(handle a)---------------

Pick up a dropped item.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.PickupRune:
void CDOTA_BaseNPC.PickupRune(handle a)---------------

Pick up a rune.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.ProvidesVision:
bool CDOTA_BaseNPC.ProvidesVision()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.ReduceMana:
void CDOTA_BaseNPC.ReduceMana(float a)---------------

Remove mana from this unit, this can be used for involuntary mana loss, not for mana that is spent.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.RemoveAbility:
void CDOTA_BaseNPC.RemoveAbility(string a)---------------

Remove an ability from this unit by name.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.RemoveItem:
void CDOTA_BaseNPC.RemoveItem(handle a)---------------

Removes the passed item from this unit's inventory.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.RemoveModifierByName:
void CDOTA_BaseNPC.RemoveModifierByName(string a)---------------

Removes a modifier


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.RemoveModifierByNameAndCaster:
void CDOTA_BaseNPC.RemoveModifierByNameAndCaster(string a, handle b)---------------

Removes a modifier that was cast by the given caster


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.RemoveNoDraw:
void CDOTA_BaseNPC.RemoveNoDraw()---------------

Remove the no draw flag.




 .. _CDOTA_BaseNPC.RespawnUnit:
void CDOTA_BaseNPC.RespawnUnit()---------------

Respawns the target unit if it can be respawned.




 .. _CDOTA_BaseNPC.SellItem:
void CDOTA_BaseNPC.SellItem(handle a)---------------

Sells the passed item in this unit's inventory.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetAdditionalBattleMusicWeight:
void CDOTA_BaseNPC.SetAdditionalBattleMusicWeight(float a)---------------

Combat involving this creature will have this weight added to the music calcuations


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetAttackCapability:
void CDOTA_BaseNPC.SetAttackCapability(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetAttacking:
void CDOTA_BaseNPC.SetAttacking(handle a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetBaseAttackTime:
void CDOTA_BaseNPC.SetBaseAttackTime(float a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetBaseDamageMax:
void CDOTA_BaseNPC.SetBaseDamageMax(int a)---------------

Sets the minimum base damage.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetBaseDamageMin:
void CDOTA_BaseNPC.SetBaseDamageMin(int a)---------------

Sets the minimum base damage.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetBaseHealthRegen:
void CDOTA_BaseNPC.SetBaseHealthRegen(float a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetBaseMagicalResistanceValue:
void CDOTA_BaseNPC.SetBaseMagicalResistanceValue(float a)---------------

Sets base magical armor value.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetBaseManaRegen:
void CDOTA_BaseNPC.SetBaseManaRegen(float a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetBaseMaxHealth:
void CDOTA_BaseNPC.SetBaseMaxHealth(float a)---------------

Set a new base max health value.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetBaseMoveSpeed:
void CDOTA_BaseNPC.SetBaseMoveSpeed(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetControllableByPlayer:
void CDOTA_BaseNPC.SetControllableByPlayer(int a, bool b)---------------

Set this unit controllable by the player with the passed ID.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetCursorCastTarget:
void CDOTA_BaseNPC.SetCursorCastTarget(handle a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetCursorPosition:
void CDOTA_BaseNPC.SetCursorPosition(Vector a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetCursorTargetingNothing:
void CDOTA_BaseNPC.SetCursorTargetingNothing(bool a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetDayTimeVisionRange:
void CDOTA_BaseNPC.SetDayTimeVisionRange(int a)---------------

Set the base vision range.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetDeathXP:
void CDOTA_BaseNPC.SetDeathXP(int a)---------------

Set the XP bounty on this unit


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetForceAttackTarget:
void CDOTA_BaseNPC.SetForceAttackTarget(handle a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetHasInventory:
void CDOTA_BaseNPC.SetHasInventory(bool a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetHullRadius:
void CDOTA_BaseNPC.SetHullRadius(float a)---------------

Set the collision hull radius of this NPC


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetIdleAcquire:
void CDOTA_BaseNPC.SetIdleAcquire(bool a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetInitialGoalEntity:
void CDOTA_BaseNPC.SetInitialGoalEntity(handle a)---------------

Sets the initial waypoint goal for this NPC


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetMana:
void CDOTA_BaseNPC.SetMana(float a)---------------

Set the mana on this unit.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetMaximumGoldBounty:
void CDOTA_BaseNPC.SetMaximumGoldBounty(int a)---------------

Set the maximum gold bounty for this unit.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetMinimumGoldBounty:
void CDOTA_BaseNPC.SetMinimumGoldBounty(int a)---------------

Set the minimum gold bounty for this unit.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetMoveCapability:
void CDOTA_BaseNPC.SetMoveCapability(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetMustReachEachGoalEntity:
void CDOTA_BaseNPC.SetMustReachEachGoalEntity(bool a)---------------

Set whether this NPC is required to reach each goal entity, rather than being allowed to 'unkink' their path


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetNeverMoveToClearSpace:
void CDOTA_BaseNPC.SetNeverMoveToClearSpace(bool a)---------------

If set to true, we will never attempt to move this unit to clear space, even when it unphases.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetNightTimeVisionRange:
void CDOTA_BaseNPC.SetNightTimeVisionRange(int a)---------------

Set the base vision range.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetOriginalModel:
void CDOTA_BaseNPC.SetOriginalModel(string originalModel)---------------

Sets the original model of this entity, which it will tend to fall back to anytime its state changes


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string | originalModel | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetPhysicalArmorBaseValue:
void CDOTA_BaseNPC.SetPhysicalArmorBaseValue(float a)---------------

Sets base physical armor value.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetRangedProjectileName:
void CDOTA_BaseNPC.SetRangedProjectileName(string a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetStolenScepter:
void CDOTA_BaseNPC.SetStolenScepter(bool a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetUnitName:
void CDOTA_BaseNPC.SetUnitName(string a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.ShouldIdleAcquire:
bool CDOTA_BaseNPC.ShouldIdleAcquire()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.SpendMana:
void CDOTA_BaseNPC.SpendMana(float a, handle b)---------------

Spend mana from this unit, this can be used for spending mana from abilities or item usage.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.Stop:
void CDOTA_BaseNPC.Stop()---------------

Stop the current order.




 .. _CDOTA_BaseNPC.SwapAbilities:
void CDOTA_BaseNPC.SwapAbilities(string a, string b, bool c, bool d)---------------

Swaps the slots of the two passed abilities and sets them enabled/disabled: const char* AbilityName1, const char* AbilityName2, ''bool'' bEnable1, ''bool'' bEnable2. The boolean controls which ability is active. The ability order is never swapped when swapping abilities, only the boolean statements are flipped.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
|  string |  | No Description Set |
|  bool |  | No Description Set |
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.TimeUntilNextAttack:
float CDOTA_BaseNPC.TimeUntilNextAttack()---------------

No Description Set


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.TriggerModifierDodge:
bool CDOTA_BaseNPC.TriggerModifierDodge()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.TriggerSpellAbsorb:
bool CDOTA_BaseNPC.TriggerSpellAbsorb(handle a)---------------

Query whether the passed ability will trigger spell absorb on this unit.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.UnitCanRespawn:
bool CDOTA_BaseNPC.UnitCanRespawn()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC_Hero.AddExperience:
bool CDOTA_BaseNPC_Hero.AddExperience(float amount, bool applyBotDifficultyScaling)---------------

Adds experience to this unit.


::
    --Upgrade any spawned hero to Level 6
function MyGameMode:OnNPCSpawned( keys )
  local spawnedUnit = EntIndexToHScript( keys.entindex )
  if spawnedUnit:IsHero() then
    local level = spawnedUnit:GetLevel()
      while level < 6 do
        spawnedUnit:AddExperience (2000,false)
        level = spawnedUnit:GetLevel()
      end
  end
end

+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float | amount | No Description Set |
|  bool | applyBotDifficultyScaling | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC_Hero.Buyback:
void CDOTA_BaseNPC_Hero.Buyback()---------------

Spend the gold and buyback with this hero.




 .. _CDOTA_BaseNPC_Hero.CalculateStatBonus:
void CDOTA_BaseNPC_Hero.CalculateStatBonus()---------------

Recalculate all stats after the hero gains stats.




 .. _CDOTA_BaseNPC_Hero.CanEarnGold:
bool CDOTA_BaseNPC_Hero.CanEarnGold()---------------

Returns boolean value result of buyback gold limit time less than game time.


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC_Hero.ClearLastHitMultikill:
void CDOTA_BaseNPC_Hero.ClearLastHitMultikill()---------------

Value is stored in PlayerResource.




 .. _CDOTA_BaseNPC_Hero.ClearLastHitStreak:
void CDOTA_BaseNPC_Hero.ClearLastHitStreak()---------------

Value is stored in PlayerResource.




 .. _CDOTA_BaseNPC_Hero.ClearStreak:
void CDOTA_BaseNPC_Hero.ClearStreak()---------------

Value is stored in PlayerResource.




 .. _CDOTA_BaseNPC_Hero.GetAbilityPoints:
int CDOTA_BaseNPC_Hero.GetAbilityPoints()---------------

Gets the current unspent ability point's.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetAgility:
float CDOTA_BaseNPC_Hero.GetAgility()---------------

No Description Set


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetAgilityGain:
float CDOTA_BaseNPC_Hero.GetAgilityGain()---------------

No Description Set


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetAssists:
int CDOTA_BaseNPC_Hero.GetAssists()---------------

Value is stored in PlayerResource.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetAttacker:
int CDOTA_BaseNPC_Hero.GetAttacker(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetBaseAgility:
float CDOTA_BaseNPC_Hero.GetBaseAgility()---------------

No Description Set


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetBaseDamageMax:
int CDOTA_BaseNPC_Hero.GetBaseDamageMax()---------------

Hero damage is also affected by attributes.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetBaseDamageMin:
int CDOTA_BaseNPC_Hero.GetBaseDamageMin()---------------

Hero damage is also affected by attributes.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetBaseIntellect:
float CDOTA_BaseNPC_Hero.GetBaseIntellect()---------------

No Description Set


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetBaseStrength:
float CDOTA_BaseNPC_Hero.GetBaseStrength()---------------

No Description Set


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetBonusDamageFromPrimaryStat:
int CDOTA_BaseNPC_Hero.GetBonusDamageFromPrimaryStat()---------------

No Description Set


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetBuybackCooldownTime:
float CDOTA_BaseNPC_Hero.GetBuybackCooldownTime()---------------

Return ''float'' value for the amount of time left on cooldown for this hero's buyback.


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetBuybackCost:
int CDOTA_BaseNPC_Hero.GetBuybackCost()---------------

Return integer value for the gold cost of a buyback.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetBuybackGoldLimitTime:
float CDOTA_BaseNPC_Hero.GetBuybackGoldLimitTime()---------------

Returns the amount of time gold gain is limited after buying back.


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetCurrentXP:
int CDOTA_BaseNPC_Hero.GetCurrentXP()---------------

Returns the amount of XP


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetDeathGoldCost:
int CDOTA_BaseNPC_Hero.GetDeathGoldCost()---------------

No Description Set


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetDeaths:
int CDOTA_BaseNPC_Hero.GetDeaths()---------------

Value is stored in PlayerResource.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetDenies:
int CDOTA_BaseNPC_Hero.GetDenies()---------------

Value is stored in PlayerResource.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetGold:
int CDOTA_BaseNPC_Hero.GetGold()---------------

Returns gold amount for the player owning this hero


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetGoldBounty:
int CDOTA_BaseNPC_Hero.GetGoldBounty()---------------

No Description Set


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetHealthRegen:
float CDOTA_BaseNPC_Hero.GetHealthRegen()---------------

Hero health regen is affected by attributes.


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetIncreasedAttackSpeed:
float CDOTA_BaseNPC_Hero.GetIncreasedAttackSpeed()---------------

Hero attack speed is also affected by agility.


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetIntellect:
float CDOTA_BaseNPC_Hero.GetIntellect()---------------

No Description Set


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetIntellectGain:
float CDOTA_BaseNPC_Hero.GetIntellectGain()---------------

No Description Set


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetKills:
int CDOTA_BaseNPC_Hero.GetKills()---------------

Value is stored in PlayerResource.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetLastHits:
int CDOTA_BaseNPC_Hero.GetLastHits()---------------

Value is stored in PlayerResource.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetManaRegen:
float CDOTA_BaseNPC_Hero.GetManaRegen()---------------

Hero mana regen is affected by attributes.


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetMostRecentDamageTime:
float CDOTA_BaseNPC_Hero.GetMostRecentDamageTime()---------------

No Description Set


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetMultipleKillCount:
int CDOTA_BaseNPC_Hero.GetMultipleKillCount()---------------

No Description Set


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetNumAttackers:
int CDOTA_BaseNPC_Hero.GetNumAttackers()---------------

No Description Set


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetPhysicalArmorValue:
float CDOTA_BaseNPC_Hero.GetPhysicalArmorValue()---------------

Hero armor is affected by attributes.


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetPlayerID:
int CDOTA_BaseNPC_Hero.GetPlayerID()---------------

Returns player ID of the player owning this hero


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetPrimaryAttribute:
int CDOTA_BaseNPC_Hero.GetPrimaryAttribute()---------------

0 = strength, 1 = agility, 2 = intelligence.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetPrimaryStatValue:
float CDOTA_BaseNPC_Hero.GetPrimaryStatValue()---------------

No Description Set


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetRespawnTime:
float CDOTA_BaseNPC_Hero.GetRespawnTime()---------------

No Description Set


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetStatsBasedManaRegen:
float CDOTA_BaseNPC_Hero.GetStatsBasedManaRegen()---------------

Returns only the regen based on Intelligence.


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetStreak:
int CDOTA_BaseNPC_Hero.GetStreak()---------------

Value is stored in PlayerResource.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetStrength:
float CDOTA_BaseNPC_Hero.GetStrength()---------------

No Description Set


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetStrengthGain:
float CDOTA_BaseNPC_Hero.GetStrengthGain()---------------

No Description Set


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetTimeUntilRespawn:
float CDOTA_BaseNPC_Hero.GetTimeUntilRespawn()---------------

No Description Set


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC_Hero.HasAnyAvailableInventorySpace:
bool CDOTA_BaseNPC_Hero.HasAnyAvailableInventorySpace()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC_Hero.HasFlyingVision:
bool CDOTA_BaseNPC_Hero.HasFlyingVision()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC_Hero.HasOwnerAbandoned:
bool CDOTA_BaseNPC_Hero.HasOwnerAbandoned()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC_Hero.HasRoomForItem:
int CDOTA_BaseNPC_Hero.HasRoomForItem(string a, bool b, bool c)---------------

Args: const char* pItemName, ''bool'' bIncludeStashCombines, ''bool'' bAllowSelling


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
|  bool |  | No Description Set |
|  bool |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_BaseNPC_Hero.HeroLevelUp:
void CDOTA_BaseNPC_Hero.HeroLevelUp(bool a)---------------

Levels up the hero, true or false to play effects.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Hero.IncrementAssists:
void CDOTA_BaseNPC_Hero.IncrementAssists()---------------

Value is stored in PlayerResource.




 .. _CDOTA_BaseNPC_Hero.IncrementDeaths:
void CDOTA_BaseNPC_Hero.IncrementDeaths()---------------

Value is stored in PlayerResource.




 .. _CDOTA_BaseNPC_Hero.IncrementDenies:
void CDOTA_BaseNPC_Hero.IncrementDenies()---------------

Value is stored in PlayerResource.




 .. _CDOTA_BaseNPC_Hero.IncrementKills:
void CDOTA_BaseNPC_Hero.IncrementKills(int kills)---------------

Passed ID is for the victim, killer ID is ID of the current hero. Value is stored in PlayerResource.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int | kills | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Hero.IncrementLastHitMultikill:
void CDOTA_BaseNPC_Hero.IncrementLastHitMultikill()---------------

Value is stored in PlayerResource.




 .. _CDOTA_BaseNPC_Hero.IncrementLastHits:
void CDOTA_BaseNPC_Hero.IncrementLastHits()---------------

Value is stored in PlayerResource.




 .. _CDOTA_BaseNPC_Hero.IncrementLastHitStreak:
void CDOTA_BaseNPC_Hero.IncrementLastHitStreak()---------------

Value is stored in PlayerResource.




 .. _CDOTA_BaseNPC_Hero.IncrementNearbyCreepDeaths:
void CDOTA_BaseNPC_Hero.IncrementNearbyCreepDeaths()---------------

Value is stored in PlayerResource.




 .. _CDOTA_BaseNPC_Hero.IncrementStreak:
void CDOTA_BaseNPC_Hero.IncrementStreak()---------------

Value is stored in PlayerResource.




 .. _CDOTA_BaseNPC_Hero.IsBuybackDisabledByReapersScythe:
bool CDOTA_BaseNPC_Hero.IsBuybackDisabledByReapersScythe()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC_Hero.IsReincarnating:
bool CDOTA_BaseNPC_Hero.IsReincarnating()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC_Hero.KilledHero:
void CDOTA_BaseNPC_Hero.KilledHero(handle a, handle b)---------------

Args: Hero, Inflictor


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Hero.ModifyAgility:
void CDOTA_BaseNPC_Hero.ModifyAgility(float a)---------------

Adds passed value to base attribute value, then calls CalculateStatBonus.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Hero.ModifyGold:
int CDOTA_BaseNPC_Hero.ModifyGold(int goldAmmt, bool reliable, int reason)---------------

Gives this hero some gold. Args: ''int'' nGoldChange, ''bool'' bReliable, ''int'' reason


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int | goldAmmt | No Description Set |
|  bool | reliable | No Description Set |
|  int | reason | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_BaseNPC_Hero.ModifyIntellect:
void CDOTA_BaseNPC_Hero.ModifyIntellect(float a)---------------

Adds passed value to base attribute value, then calls CalculateStatBonus.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Hero.ModifyStrength:
void CDOTA_BaseNPC_Hero.ModifyStrength(float a)---------------

Adds passed value to base attribute value, then calls CalculateStatBonus.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Hero.PerformTaunt:
void CDOTA_BaseNPC_Hero.PerformTaunt()---------------

No Description Set




 .. _CDOTA_BaseNPC_Hero.RecordLastHit:
void CDOTA_BaseNPC_Hero.RecordLastHit()---------------

No Description Set




 .. _CDOTA_BaseNPC_Hero.RespawnHero:
void CDOTA_BaseNPC_Hero.RespawnHero(bool buyback, bool unknown1, bool unknown2)---------------




+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  bool | buyback | No Description Set |
|  bool | unknown1 | No Description Set |
|  bool | unknown2 | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Hero.SetAbilityPoints:
void CDOTA_BaseNPC_Hero.SetAbilityPoints(int a)---------------

Sets the current unspent ability point's.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Hero.SetBaseAgility:
void CDOTA_BaseNPC_Hero.SetBaseAgility(float a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Hero.SetBaseIntellect:
void CDOTA_BaseNPC_Hero.SetBaseIntellect(float a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Hero.SetBaseStrength:
void CDOTA_BaseNPC_Hero.SetBaseStrength(float a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Hero.SetBuybackCooldownTime:
void CDOTA_BaseNPC_Hero.SetBuybackCooldownTime(float a)---------------

Sets the buyback cooldown time.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Hero.SetBuyBackDisabledByReapersScythe:
void CDOTA_BaseNPC_Hero.SetBuyBackDisabledByReapersScythe(bool a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Hero.SetBuybackGoldLimitTime:
void CDOTA_BaseNPC_Hero.SetBuybackGoldLimitTime(float a)---------------

Set the amount of time gold gain is limited after buying back.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Hero.SetCustomDeathXP:
void CDOTA_BaseNPC_Hero.SetCustomDeathXP(int a)---------------

Sets a custom experience value for this hero. {{tip|GameRules boolean must be set for this to work!}}


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Hero.SetGold:
void CDOTA_BaseNPC_Hero.SetGold(int a, bool b)---------------

Sets the gold amount for the player owning this hero


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Hero.SetPlayerID:
void CDOTA_BaseNPC_Hero.SetPlayerID(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Hero.SetRespawnPosition:
void CDOTA_BaseNPC_Hero.SetRespawnPosition(Vector a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Hero.SetTimeUntilRespawn:
void CDOTA_BaseNPC_Hero.SetTimeUntilRespawn(float a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Hero.ShouldDoFlyHeightVisual:
bool CDOTA_BaseNPC_Hero.ShouldDoFlyHeightVisual()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC_Hero.SpendGold:
void CDOTA_BaseNPC_Hero.SpendGold(int a, int b)---------------

Args: ''int'' nGold, ''int'' nReason


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Hero.UnitCanRespawn:
bool CDOTA_BaseNPC_Hero.UnitCanRespawn()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC_Hero.UpgradeAbility:
void CDOTA_BaseNPC_Hero.UpgradeAbility(handle a)---------------

This upgrades the passed ability if it exists and the hero has enough ability point's.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Hero.WillReincarnate:
bool CDOTA_BaseNPC_Hero.WillReincarnate()---------------

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC_Creature.AddItemDrop:
void CDOTA_BaseNPC_Creature.AddItemDrop(handle a)---------------

Add the specified item drop to this creature


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Creature.CreatureLevelUp:
void CDOTA_BaseNPC_Creature.CreatureLevelUp(int a)---------------

Level the creature up by the specified number of levels


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Creature.IsChampion:
bool CDOTA_BaseNPC_Creature.IsChampion()---------------

Is this unit a champion?


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC_Creature.SetArmorGain:
void CDOTA_BaseNPC_Creature.SetArmorGain(float a)---------------

Set the armor gained per level on this creature.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Creature.SetAttackTimeGain:
void CDOTA_BaseNPC_Creature.SetAttackTimeGain(float a)---------------

Set the attack time gained per level on this creature.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Creature.SetBountyGain:
void CDOTA_BaseNPC_Creature.SetBountyGain(int a)---------------

Set the bounty gold gained per level on this creature.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Creature.SetChampion:
void CDOTA_BaseNPC_Creature.SetChampion(bool a)---------------

Flag this unit as a champion creature.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Creature.SetDamageGain:
void CDOTA_BaseNPC_Creature.SetDamageGain(int a)---------------

Set the damage gained per level on this creature.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Creature.SetDisableResistanceGain:
void CDOTA_BaseNPC_Creature.SetDisableResistanceGain(float a)---------------

Set the disable resistance gained per level on this creature.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Creature.SetHPGain:
void CDOTA_BaseNPC_Creature.SetHPGain(int a)---------------

Set the hit point's gained per level on this creature.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Creature.SetHPRegenGain:
void CDOTA_BaseNPC_Creature.SetHPRegenGain(float a)---------------

Set the hit point's regen gained per level on this creature.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Creature.SetMagicResistanceGain:
void CDOTA_BaseNPC_Creature.SetMagicResistanceGain(float a)---------------

Set the magic resistance gained per level on this creature.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Creature.SetManaGain:
void CDOTA_BaseNPC_Creature.SetManaGain(int a)---------------

Set the mana point's gained per level on this creature.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Creature.SetManaRegenGain:
void CDOTA_BaseNPC_Creature.SetManaRegenGain(float a)---------------

Set the mana point's regen gained per level on this creature.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Creature.SetMoveSpeedGain:
void CDOTA_BaseNPC_Creature.SetMoveSpeedGain(int a)---------------

Set the move speed gained per level on this creature.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Creature.SetXPGain:
void CDOTA_BaseNPC_Creature.SetXPGain(int a)---------------

Set the xp reward gained per level on this creature.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Building.GetInvulnCount:
int CDOTA_BaseNPC_Building.GetInvulnCount()---------------

Get the invulnerability count for a building.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC_Building.SetInvulnCount:
void CDOTA_BaseNPC_Building.SetInvulnCount(int a)---------------

Set the invulnerability counter of this building.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CRPG_Unit.ActionState:
handle CRPG_Unit.ActionState()---------------

return the ActionState object for this unit.


Returns:
handle - No Description Set


 .. _CRPG_Unit.ClearMovementTarget:
void CRPG_Unit.ClearMovementTarget()---------------

Clear any movement target entity/position.




 .. _CRPG_Unit.FindSensedEnemies:
table CRPG_Unit.FindSensedEnemies()---------------

returns list of all enemy units within this unit's sight cone or sensing sphere


Returns:
table - No Description Set


 .. _CRPG_Unit.GetMaxSpeed:
float CRPG_Unit.GetMaxSpeed()---------------

returns unit's max speed


Returns:
float - No Description Set


 .. _CRPG_Unit.GetMaxStamina:
float CRPG_Unit.GetMaxStamina()---------------

returns maximum stamina amount.


Returns:
float - No Description Set


 .. _CRPG_Unit.GetMovementTargetEntity:
handle CRPG_Unit.GetMovementTargetEntity()---------------

Returs the movement target entity, if set.


Returns:
handle - No Description Set


 .. _CRPG_Unit.GetSensingSphereRange:
float CRPG_Unit.GetSensingSphereRange()---------------

returns range of unit's 360 degree sensing sphere


Returns:
float - No Description Set


 .. _CRPG_Unit.GetSightConeAngle:
float CRPG_Unit.GetSightConeAngle()---------------

returns angle in which the unit can see things up to sight range


Returns:
float - No Description Set


 .. _CRPG_Unit.GetSightConeRange:
float CRPG_Unit.GetSightConeRange()---------------

returns range of unit's sight cone


Returns:
float - No Description Set


 .. _CRPG_Unit.GetStamina:
float CRPG_Unit.GetStamina()---------------

returns current stamina amount.


Returns:
float - No Description Set


 .. _CRPG_Unit.GetTurnRate:
float CRPG_Unit.GetTurnRate()---------------

returns unit's turn rate in degrees per second


Returns:
float - No Description Set


 .. _CRPG_Unit.GetUnitName:
string CRPG_Unit.GetUnitName()---------------

get the unit name for this unit.


Returns:
string - No Description Set


 .. _CRPG_Unit.GrantItem:
void CRPG_Unit.GrantItem(string a, bool b)---------------

( sItemName ) - grant an item to the unit by name.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CRPG_Unit.IsBlocking:
bool CRPG_Unit.IsBlocking()---------------

is this unit blocking?


Returns:
bool - No Description Set


 .. _CRPG_Unit.IsFacing:
bool CRPG_Unit.IsFacing(Vector a, float b)---------------

( vecTargetPosition, flAngleTolerance ) - returns true if the unit is within flAngleTolerance degrees of the target position


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _CRPG_Unit.SetBlocking:
void CRPG_Unit.SetBlocking(bool a)---------------

( bShouldBlock ) - Set the blocking state of this unit.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CRPG_Unit.SetMaxSpeed:
void CRPG_Unit.SetMaxSpeed(float a)---------------

( flMaxSpeed ) - sets unit's max speed


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CRPG_Unit.SetMovementTargetEntity:
void CRPG_Unit.SetMovementTargetEntity(handle a, float b)---------------

( hTargetEntity, flTargetRange ) - Try to move this unit to the given range from the target entity.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CRPG_Unit.SetMovementTargetPosition:
void CRPG_Unit.SetMovementTargetPosition(Vector a, float b)---------------

( vecTargetPosition, flTargetRange ) - Try to move this unit to the given range from the target point.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CRPG_Unit.SetSensingSphereRange:
void CRPG_Unit.SetSensingSphereRange(float a)---------------

( flSightRange ) - set range of unit's 360 degree sensing sphere


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CRPG_Unit.SetSightConeAngle:
void CRPG_Unit.SetSightConeAngle(float a)---------------

( flAngleDegrees ) - sets angle in which the unit can see things up to sight range


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CRPG_Unit.SetSightConeRange:
void CRPG_Unit.SetSightConeRange(float a)---------------

( fRange ) - set range of unit's sight cone


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CRPG_Unit.SetTurnRate:
void CRPG_Unit.SetTurnRate(float a)---------------

( flTurnRate ) - sets unit's turn rate in degrees per second


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseGameMode.ClientLoadGridNav:
void CDOTABaseGameMode.ClientLoadGridNav()---------------

Tell clients that they need to load gridnav information. Used for things like allowing clients to identify valid locations to place buildings.




 .. _CDOTABaseGameMode.SetAlwaysShowPlayerInventory:
void CDOTABaseGameMode.SetAlwaysShowPlayerInventory(bool a)---------------

Show the player hero's inventory in the HUD, regardless of what unit is selected.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseGameMode.SetBotThinkingEnabled:
void CDOTABaseGameMode.SetBotThinkingEnabled(bool a)---------------

Enables/Disables bot thinking. Requires a very Dota PvP-like map with 3 lanes, a shop, etc.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseGameMode.SetBuybackEnabled:
void CDOTABaseGameMode.SetBuybackEnabled(bool a)---------------

Enables or disables buyback completely


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseGameMode.SetCameraDistanceOverride:
void CDOTABaseGameMode.SetCameraDistanceOverride(float a)---------------

Set a different camera distance; dota default is 1134.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseGameMode.SetCustomBuybackCooldownEnabled:
void CDOTABaseGameMode.SetCustomBuybackCooldownEnabled(bool a)---------------

Turns on capability to define custom buyback cooldowns.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseGameMode.SetCustomBuybackCostEnabled:
void CDOTABaseGameMode.SetCustomBuybackCostEnabled(bool a)---------------

Turns on capability to define custom buyback costs.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseGameMode.SetCustomHeroMaxLevel:
void CDOTABaseGameMode.SetCustomHeroMaxLevel(int maxLevel)---------------

Allows definition of the max level heroes can achieve (default is 25).


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int | maxLevel | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseGameMode.SetCustomXPRequiredToReachNextLevel:
void CDOTABaseGameMode.SetCustomXPRequiredToReachNextLevel(handle a)---------------

Allows definition of a ''table'' of hero XP values.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseGameMode.SetFogOfWarDisabled:
void CDOTABaseGameMode.SetFogOfWarDisabled(bool a)---------------

Turn the fog of war on or off.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseGameMode.SetGoldSoundDisabled:
void CDOTABaseGameMode.SetGoldSoundDisabled(bool a)---------------

Turn the sound when gold is acquired off/on. Takes a ''bool''.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseGameMode.SetOverrideSelectionEntity:
void CDOTABaseGameMode.SetOverrideSelectionEntity(handle unit)---------------

Set an override for the default selection entity, instead of each player's hero.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle | unit | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseGameMode.SetRecommendedItemsDisabled:
void CDOTABaseGameMode.SetRecommendedItemsDisabled(bool a)---------------

Turn the panel for showing recommended items at the shop off/on. Takes a ''bool''.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseGameMode.SetRemoveIllusionsOnDeath:
void CDOTABaseGameMode.SetRemoveIllusionsOnDeath(bool a)---------------

Make it so illusions are immediately removed upon death, rather than sticking around for a few seconds.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseGameMode.SetTopBarTeamValue:
void CDOTABaseGameMode.SetTopBarTeamValue(int a, int b)---------------

Set the team values on the top game bar.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseGameMode.SetTopBarTeamValuesOverride:
void CDOTABaseGameMode.SetTopBarTeamValuesOverride(bool a)---------------

Override the values of the team values on the top game bar.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseGameMode.SetTopBarTeamValuesVisible:
void CDOTABaseGameMode.SetTopBarTeamValuesVisible(bool a)---------------

Turning on/off the team values on the top game bar.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseGameMode.SetTowerBackdoorProtectionEnabled:
void CDOTABaseGameMode.SetTowerBackdoorProtectionEnabled(bool a)---------------

Enables/Disables tower backdoor protection


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseGameMode.SetUseCustomHeroLevels:
void CDOTABaseGameMode.SetUseCustomHeroLevels(bool a)---------------

Turn on custom-defined XP values for hero level ups. The ''table'' should be defined before switching this on.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDotaQuest.AddSubquest:
void CDotaQuest.AddSubquest(handle a)---------------

Add a subquest to this quest


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDotaQuest.CompleteQuest:
void CDotaQuest.CompleteQuest()---------------

Mark this quest complete




 .. _CDotaQuest.GetSubquest:
handle CDotaQuest.GetSubquest(int a)---------------

Finds a subquest from this quest by index


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _CDotaQuest.GetSubquestByName:
handle CDotaQuest.GetSubquestByName(string a)---------------

Finds a subquest from this quest by name


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _CDotaQuest.RemoveSubquest:
void CDotaQuest.RemoveSubquest(handle a)---------------

Remove a subquest from this quest


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDotaQuest.SetTextReplaceString:
void CDotaQuest.SetTextReplaceString(string a)---------------

Set the text replace ''string'' for this quest


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDotaQuest.SetTextReplaceValue:
void CDotaQuest.SetTextReplaceValue(int a, int b)---------------

Set a quest value


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDotaSubquestBase.CompleteSubquest:
void CDotaSubquestBase.CompleteSubquest()---------------

Mark this subquest complete




 .. _CDotaSubquestBase.SetTextReplaceString:
void CDotaSubquestBase.SetTextReplaceString(string a)---------------

Set the text replace ''string'' for this subquest


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDotaSubquestBase.SetTextReplaceValue:
void CDotaSubquestBase.SetTextReplaceValue(int a, int b)---------------

Set a subquest value


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CPhysicsComponent.ExpensiveInstantRayCast:
bool CPhysicsComponent.ExpensiveInstantRayCast(Vector a, Vector b, handle c)---------------

Do an instant (i.e. blocking) Ray Cast. Will do a handle/queue version later. Don't plan to use this for real!


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector |  | No Description Set |
|  Vector |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _CPointTemplate.DeleteCreatedSpawnGroups:
void CPointTemplate.DeleteCreatedSpawnGroups()---------------

DeleteCreatedSpawnGroups() : Deletes any spawn groups that this point_template has spawned. Note: The point_template will not be deleted by this.




 .. _CPointTemplate.ForceSpawn:
void CPointTemplate.ForceSpawn()---------------

ForceSpawn() : Spawns all of the entities the point_template is pointing at.




 .. _CPointTemplate.GetSpawnedEntities:
handle CPointTemplate.GetSpawnedEntities()---------------

GetSpawnedEntities() : Get the list of the most recent spawned entities


Returns:
handle - No Description Set


 .. _CPointTemplate.SetSpawnCallback:
void CPointTemplate.SetSpawnCallback(handle a, handle b)---------------

SetSpawnCallback( hCallbackFunc, hCallbackScope, hCallbackData ) : Set a callback for when the template spawns entities. The spawned entities will be passed in as an array.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CBodyComponent.AddImpulseAtPosition:
void CBodyComponent.AddImpulseAtPosition(Vector a, Vector b)---------------

Apply an impulse at a worldspace position to the physics


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector |  | No Description Set |
|  Vector |  | No Description Set |
+-----------+--------------+--------------+


 .. _CBodyComponent.AddVelocity:
void CBodyComponent.AddVelocity(Vector a, Vector b)---------------

Add linear and angular velocity to the physics object


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector |  | No Description Set |
|  Vector |  | No Description Set |
+-----------+--------------+--------------+


 .. _CBodyComponent.DetachFromParent:
void CBodyComponent.DetachFromParent()---------------

Detach from its parent




 .. _CBodyComponent.GetSequence:
<> CBodyComponent.GetSequence()---------------

Returns the active sequence


Returns:
<> - No Description Set


 .. _CBodyComponent.IsAttachedToParent:
bool CBodyComponent.IsAttachedToParent()---------------

Is attached to parent


Returns:
bool - No Description Set


 .. _CBodyComponent.LookupSequence:
<> CBodyComponent.LookupSequence(string a)---------------

Returns a sequence id given a name


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
+-----------+--------------+--------------+
Returns:
<> - No Description Set


 .. _CBodyComponent.SequenceDuration:
float CBodyComponent.SequenceDuration(string a)---------------

Returns the duration in seconds of the specified sequence


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
+-----------+--------------+--------------+
Returns:
float - No Description Set


 .. _CBodyComponent.SetAngularVelocity:
void CBodyComponent.SetAngularVelocity(Vector a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector |  | No Description Set |
+-----------+--------------+--------------+


 .. _CBodyComponent.SetAnimation:
void CBodyComponent.SetAnimation(string a)---------------

Pass ''string'' for the animation to play on this model


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _CBodyComponent.SetBodyGroup:
void CBodyComponent.SetBodyGroup(string a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _CBodyComponent.SetMaterialGroup:
void CBodyComponent.SetMaterialGroup(utlstringtoken a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  utlstringtoken |  | No Description Set |
+-----------+--------------+--------------+


 .. _CBodyComponent.SetVelocity:
void CBodyComponent.SetVelocity(Vector velocity)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector | velocity | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseAnimating.GetAttachmentAngles:
Vector CBaseAnimating.GetAttachmentAngles(int a)---------------

Get the attachement id's angles as a p,y,r ''vector''


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
Vector - No Description Set


 .. _CBaseAnimating.GetAttachmentOrigin:
Vector CBaseAnimating.GetAttachmentOrigin(int a)---------------

Get the attachement id's origin ''vector''


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
Vector - No Description Set


 .. _CBaseAnimating.IsSequenceFinished:
bool CBaseAnimating.IsSequenceFinished()---------------

Ask whether the main sequence is done playing


Returns:
bool - No Description Set


 .. _CBaseAnimating.ScriptLookupAttachment:
int CBaseAnimating.ScriptLookupAttachment(string a)---------------

Get the named attachment id


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CBaseAnimating.SetBodygroup:
void CBaseAnimating.SetBodygroup(int a, int b)---------------

Sets a bodygroup


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseAnimating.SetModelScale:
void CBaseAnimating.SetModelScale(float scale)---------------

Sets the model's scale to <i>scale</i>, <br/>so if a unit had its model scale at 1, and you use <i>SetModelScale(<b>10.0</b>)</i>, it would set the scale to <b>10.0</b>.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float | scale | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseAnimating.SetPoseParameter:
float CBaseAnimating.SetPoseParameter(string a, float b)---------------

Set the specified pose parameter to the specified value


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+
Returns:
float - No Description Set


 .. _CBaseCombatCharacter.GetEquippedWeapons:
table CBaseCombatCharacter.GetEquippedWeapons()---------------

GetEquippedWeapons() : Returns an array of all the equipped weapons


Returns:
table - No Description Set


 .. _CBaseCombatCharacter.GetWeaponCount:
int CBaseCombatCharacter.GetWeaponCount()---------------

GetWeaponCount() : Gets the number of weapons currently equipped


Returns:
int - No Description Set


 .. _ProjectileManager.CreateLinearProjectile:
int ProjectileManager.CreateLinearProjectile(handle a)---------------

Creates a linear projectile and returns the projectile ID


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _ProjectileManager.CreateTrackingProjectile:
void ProjectileManager.CreateTrackingProjectile(handle a)---------------

Creates a tracking projectile


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _ProjectileManager.DestroyLinearProjectile:
void ProjectileManager.DestroyLinearProjectile(int a)---------------

Destroys the linear projectile matching the argument ID


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _ProjectileManager.ProjectileDodge:
void ProjectileManager.ProjectileDodge(handle a)---------------

Makes the specified unit dodge projectiles


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseTrigger.Disable:
void CBaseTrigger.Disable()---------------

Disable the trigger




 .. _CBaseTrigger.Enable:
void CBaseTrigger.Enable()---------------

Enable the trigger




 .. _CBaseTrigger.IsTouching:
bool CBaseTrigger.IsTouching(handle a)---------------

Checks whether the passed entity is touching the trigger.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _CEnvEntityMaker.SpawnEntity:
void CEnvEntityMaker.SpawnEntity()---------------

Create an entity at the location of the maker




 .. _CEnvEntityMaker.SpawnEntityAtEntityOrigin:
void CEnvEntityMaker.SpawnEntityAtEntityOrigin(handle a)---------------

Create an entity at the location of a specified entity instance


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CEnvEntityMaker.SpawnEntityAtLocation:
void CEnvEntityMaker.SpawnEntityAtLocation(Vector a, Vector b)---------------

Create an entity at a specified location and orientaton, orientation is Euler angle in degrees (pitch, yaw, roll)


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector |  | No Description Set |
|  Vector |  | No Description Set |
+-----------+--------------+--------------+


 .. _CEnvEntityMaker.SpawnEntityAtNamedEntityOrigin:
void CEnvEntityMaker.SpawnEntityAtNamedEntityOrigin(string a)---------------

Create an entity at the location of a named entity


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTAVoteSystem.StartVote:
void CDOTAVoteSystem.StartVote(handle a)---------------

Starts a vote, based upon a ''table'' of parameters


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CMarkupVolumeTagged.HasTag:
bool CMarkupVolumeTagged.HasTag(string a)---------------

Does this volume have the given tag.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _CScriptPrecacheContext.AddResource:
void CScriptPrecacheContext.AddResource(string a)---------------

Precaches a specific resource


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _CScriptPrecacheContext.GetValue:
table CScriptPrecacheContext.GetValue(string a)---------------

Reads a spawn key


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
+-----------+--------------+--------------+
Returns:
table - No Description Set


 .. _CScriptKeyValues.GetValue:
table CScriptKeyValues.GetValue(string a)---------------

Reads a spawn key


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
+-----------+--------------+--------------+
Returns:
table - No Description Set


 .. _CScriptParticleManager.CreateParticle:
int CScriptParticleManager.CreateParticle(string particleName, int particleAttach, handle owningEntity)---------------

Creates a new particle effect


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string | particleName | No Description Set |
|  int | particleAttach | No Description Set |
|  handle | owningEntity | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CScriptParticleManager.CreateParticleForPlayer:
int CScriptParticleManager.CreateParticleForPlayer(string particleName, int particleAttach, handle owningEntity, handle owningPlayer)---------------

Creates a new particle effect that only plays for the specified player


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string | particleName | No Description Set |
|  int | particleAttach | No Description Set |
|  handle | owningEntity | No Description Set |
|  handle | owningPlayer | No Description Set |
+-----------+--------------+--------------+
Returns:
int - Particle ID


 .. _CScriptParticleManager.GetParticleReplacement:
string CScriptParticleManager.GetParticleReplacement(string a, handle b)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+
Returns:
string - No Description Set


 .. _CScriptParticleManager.ReleaseParticleIndex:
void CScriptParticleManager.ReleaseParticleIndex(int particleId)---------------

Frees the specified particle index


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int | particleId | No Description Set |
+-----------+--------------+--------------+


 .. _CScriptParticleManager.SetParticleAlwaysSimulate:
void CScriptParticleManager.SetParticleAlwaysSimulate(int a)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CScriptParticleManager.SetParticleControl:
void CScriptParticleManager.SetParticleControl(int particleId, int controlIndex, Vector controlData)---------------

Set the control point data for a control on a particle effect


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int | particleId | No Description Set |
|  int | controlIndex | No Description Set |
|  Vector | controlData | No Description Set |
+-----------+--------------+--------------+


 .. _CScriptParticleManager.SetParticleControlEnt:
void CScriptParticleManager.SetParticleControlEnt(int a, int b, handle c, int d, string e, Vector f, bool g)---------------

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
|  int |  | No Description Set |
|  handle |  | No Description Set |
|  int |  | No Description Set |
|  string |  | No Description Set |
|  Vector |  | No Description Set |
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CScriptHeroList.GetAllHeroes:
table CScriptHeroList.GetAllHeroes()---------------

Returns all the heroes in the world


Returns:
table - No Description Set


 .. _CScriptHeroList.GetHero:
handle CScriptHeroList.GetHero(int heroId)---------------

Get the Nth hero in the Hero List


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int | heroId | A value between 0 and 9 |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _CScriptHeroList.GetHeroCount:
int CScriptHeroList.GetHeroCount()---------------

Returns the number of heroes in the world


Returns:
int - No Description Set


 .. _CNativeOutputs.AddOutput:
void CNativeOutputs.AddOutput(string a, string b)---------------

Add an output


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _CNativeOutputs.Init:
void CNativeOutputs.Init(int a)---------------

Initialize with number of outputs


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CEnvProjectedTexture.SetFarRange:
void CEnvProjectedTexture.SetFarRange(float a)---------------

Set light maximum range


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CEnvProjectedTexture.SetLinearAttenuation:
void CEnvProjectedTexture.SetLinearAttenuation(float a)---------------

Set light linear attenuation value


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CEnvProjectedTexture.SetNearRange:
void CEnvProjectedTexture.SetNearRange(float a)---------------

Set light minimum range


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CEnvProjectedTexture.SetQuadraticAttenuation:
void CEnvProjectedTexture.SetQuadraticAttenuation(float a)---------------

Set light quadratic attenuation value


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CEnvProjectedTexture.SetVolumetrics:
void CEnvProjectedTexture.SetVolumetrics(bool a, float b, float c, int d, float e)---------------

Turn on/off light volumetrics: ''bool'' bOn, ''float'' flIntensity, ''float'' flNoise, ''int'' nPlanes, ''float'' flPlaneOffset


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  bool |  | No Description Set |
|  float |  | No Description Set |
|  float |  | No Description Set |
|  int |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CInfoData.QueryColor:
Vector CInfoData.QueryColor(utlstringtoken a, Vector b)---------------

Query color data for this key


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  utlstringtoken |  | No Description Set |
|  Vector |  | No Description Set |
+-----------+--------------+--------------+
Returns:
Vector - No Description Set


 .. _CInfoData.QueryFloat:
float CInfoData.QueryFloat(utlstringtoken a, float b)---------------

Query ''float'' data for this key


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  utlstringtoken |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+
Returns:
float - No Description Set


 .. _CInfoData.QueryInt:
int CInfoData.QueryInt(utlstringtoken a, int b)---------------

Query ''int'' data for this key


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  utlstringtoken |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CInfoData.QueryNumber:
float CInfoData.QueryNumber(utlstringtoken a, float b)---------------

Query number data for this key


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  utlstringtoken |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+
Returns:
float - No Description Set


 .. _CInfoData.QueryString:
string CInfoData.QueryString(utlstringtoken a, string b)---------------

Query ''string'' data for this key


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  utlstringtoken |  | No Description Set |
|  string |  | No Description Set |
+-----------+--------------+--------------+
Returns:
string - No Description Set


 .. _CInfoData.QueryVector:
Vector CInfoData.QueryVector(utlstringtoken a, Vector b)---------------

Query ''vector'' data for this key


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  utlstringtoken |  | No Description Set |
|  Vector |  | No Description Set |
+-----------+--------------+--------------+
Returns:
Vector - No Description Set


 .. _CPhysicsProp.DisableMotion:
void CPhysicsProp.DisableMotion()---------------

Enable motion for the prop




 .. _CPhysicsProp.EnableMotion:
void CPhysicsProp.EnableMotion()---------------

Enable motion for the prop




 .. _CDOTAGamerules.Defeated:
void CDOTAGamerules.Defeated()---------------

Kills the ancient, etc.




 .. _CDOTAGamerules.DidMatchSignoutTimeOut:
bool CDOTAGamerules.DidMatchSignoutTimeOut()---------------

true when we have waited some time after end of the game and not received signout


Returns:
bool - No Description Set


 .. _CDOTAGamerules.GetCustomGameDifficulty:
int CDOTAGamerules.GetCustomGameDifficulty()---------------

Returns the difficulty level of the custom game mode


Returns:
int - No Description Set


 .. _CDOTAGamerules.GetDifficulty:
int CDOTAGamerules.GetDifficulty()---------------

Returns difficulty level of the custom game mode


Returns:
int - No Description Set


 .. _CDOTAGamerules.GetDroppedItem:
handle CDOTAGamerules.GetDroppedItem(int dropIndex)---------------

Gets the Xth dropped item


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int | dropIndex | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _CDOTAGamerules.GetGameModeEntity:
handle CDOTAGamerules.GetGameModeEntity()---------------

Get the game mode entity


Returns:
handle - No Description Set


 .. _CDOTAGamerules.GetGameTime:
float CDOTAGamerules.GetGameTime()---------------

Returns the number of seconds elapsed since map start. This time doesn't count up when the game is paused


Returns:
float - No Description Set


 .. _CDOTAGamerules.GetMatchSignoutComplete:
bool CDOTAGamerules.GetMatchSignoutComplete()---------------

Have we received the post match signout message that includes reward information


Returns:
bool - No Description Set


 .. _CDOTAGamerules.GetNianFightStartTime:
float CDOTAGamerules.GetNianFightStartTime()---------------

Gets the start time for the Nian fight


Returns:
float - No Description Set


 .. _CDOTAGamerules.GetNianTotalDamageTaken:
int CDOTAGamerules.GetNianTotalDamageTaken()---------------

For New Bloom, get total damage taken by the Nian / Year Beast


Returns:
int - No Description Set


 .. _CDOTAGamerules.GetTimeOfDay:
float CDOTAGamerules.GetTimeOfDay()---------------

Get the time of day


Returns:
float - No Description Set


 .. _CDOTAGamerules.IsDaytime:
bool CDOTAGamerules.IsDaytime()---------------

Is it day time.


Returns:
bool - No Description Set


 .. _CDOTAGamerules.MakeTeamLose:
void CDOTAGamerules.MakeTeamLose(int team)---------------

Makes ths specified team lose


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int | team | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTAGamerules.NumDroppedItems:
int CDOTAGamerules.NumDroppedItems()---------------

Returns the number of items currently dropped on the ground


Returns:
int - No Description Set


 .. _CDOTAGamerules.Playtesting_UpdateAddOnKeyValues:
void CDOTAGamerules.Playtesting_UpdateAddOnKeyValues()---------------

Updates custom hero, unit and ability KeyValues in memory with the latest values from disk




 .. _CDOTAGamerules.ResetDefeated:
void CDOTAGamerules.ResetDefeated()---------------

Restart after killing the ancient, etc.




 .. _CDOTAGamerules.ResetToHeroSelection:
void CDOTAGamerules.ResetToHeroSelection()---------------

Restart the game at hero selection




 .. _CDOTAGamerules.SendCustomMessage:
void CDOTAGamerules.SendCustomMessage(string message, int teamID, int unknown(1?))---------------

Displays a line of text in the left textbox (where usually deaths/denies/buysbacks are announced). This function takes restricted HTML as input! (&lt;br&gt;,&lt;u&gt;,&lt;font&gt;)


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string | message | No Description Set |
|  int | teamID | No Description Set |
|  int | unknown(1?) | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTAGamerules.SetCreepMinimapIconScale:
void CDOTAGamerules.SetCreepMinimapIconScale(float scale)---------------

Scale the creep icons on the minimap.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float | scale | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTAGamerules.SetCustomGameDifficulty:
void CDOTAGamerules.SetCustomGameDifficulty(int a)---------------

Set the difficulty level of the custom game mode


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTAGamerules.SetFirstBloodActive:
void CDOTAGamerules.SetFirstBloodActive(bool a)---------------

Sets whether First Blood has been triggered.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTAGamerules.SetGameWinner:
void CDOTAGamerules.SetGameWinner(int team)---------------

Makes ths specified team win


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int | team | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTAGamerules.SetGoldPerTick:
void CDOTAGamerules.SetGoldPerTick(int a)---------------

Set the auto gold increase per timed interval.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTAGamerules.SetGoldTickTime:
void CDOTAGamerules.SetGoldTickTime(float a)---------------

Set the time ''int''erval between auto gold increases.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTAGamerules.SetHeroMinimapIconSize:
void CDOTAGamerules.SetHeroMinimapIconSize(int iconSize)---------------

(nMinimapHeroIconSize) - Set the hero minimap icon size.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int | iconSize | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTAGamerules.SetHeroRespawnEnabled:
void CDOTAGamerules.SetHeroRespawnEnabled(bool canRespawn)---------------

Control if the normal DOTA hero respawn rules apply.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  bool | canRespawn | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTAGamerules.SetHeroSelectionTime:
void CDOTAGamerules.SetHeroSelectionTime(float time)---------------

Sets the amount of time players have to pick their hero.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float | time | Time In Seconds |
+-----------+--------------+--------------+


 .. _CDOTAGamerules.SetNianFightStartTime:
void CDOTAGamerules.SetNianFightStartTime(float a)---------------

Sets the start time for the Nian fight


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTAGamerules.SetOverlayHealthBarUnit:
void CDOTAGamerules.SetOverlayHealthBarUnit(handle unit, int style)---------------

Show this unit's health on the overlay health bar


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle | unit | No Description Set |
|  int | style | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTAGamerules.SetPostGameTime:
void CDOTAGamerules.SetPostGameTime(float time)---------------

Sets the amount of time players have between the game ending and the server disconnecting them.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float | time | Time in Seconds |
+-----------+--------------+--------------+


 .. _CDOTAGamerules.SetPreGameTime:
void CDOTAGamerules.SetPreGameTime(float time)---------------

Sets the amount of time players have between picking their hero and game start.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float | time | Time In Seconds |
+-----------+--------------+--------------+


 .. _CDOTAGamerules.SetRuneMinimapIconScale:
void CDOTAGamerules.SetRuneMinimapIconScale(float scale)---------------

Scale the rune icons on the minimap.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float | scale | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTAGamerules.SetRuneSpawnTime:
void CDOTAGamerules.SetRuneSpawnTime(float time)---------------

Sets the amount of time between rune spawns.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float | time | Time in seconds |
+-----------+--------------+--------------+


 .. _CDOTAGamerules.SetSafeToLeave:
void CDOTAGamerules.SetSafeToLeave(bool safeToLeave)---------------

Mark this game as safe to leave.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  bool | safeToLeave | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTAGamerules.SetSameHeroSelectionEnabled:
void CDOTAGamerules.SetSameHeroSelectionEnabled(bool enabled)---------------

When true, players can repeatedly pick the same hero.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  bool | enabled | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTAGamerules.SetTimeOfDay:
void CDOTAGamerules.SetTimeOfDay(float time)---------------

Set the time of day.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float | time | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTAGamerules.SetTreeRegrowTime:
void CDOTAGamerules.SetTreeRegrowTime(float time)---------------

Sets the tree regrow time in seconds.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float | time | Time in Seconds |
+-----------+--------------+--------------+


 .. _CDOTAGamerules.SetUseBaseGoldBountyOnHeroes:
void CDOTAGamerules.SetUseBaseGoldBountyOnHeroes(bool a)---------------

Heroes will use the basic NPC functionality for determining their bounty, rather than DOTA specific formulas.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTAGamerules.SetUseCustomHeroXPValues:
void CDOTAGamerules.SetUseCustomHeroXPValues(bool a)---------------

Allows heroes in the map to give a specific amount of XP (this value must be set).


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTAGamerules.SetUseUniversalShopMode:
void CDOTAGamerules.SetUseUniversalShopMode(bool enabled)---------------

When true, all items are available at as long as any shop is in range, including Secret Shop items


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  bool | enabled | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTAGamerules.State_Get:
<> CDOTAGamerules.State_Get()---------------

Get the current Gamerules state


Returns:
<> - No Description Set


 .. _CToneMapControllerComponent.GetBloomScale:
float CToneMapControllerComponent.GetBloomScale()---------------

Gets bloomscale for this tonemap controller


Returns:
float - No Description Set


 .. _CToneMapControllerComponent.GetMaxExposure:
float CToneMapControllerComponent.GetMaxExposure()---------------

Gets max exposure for this tonemap controller


Returns:
float - No Description Set


 .. _CToneMapControllerComponent.GetMinExposure:
float CToneMapControllerComponent.GetMinExposure()---------------

Gets min exposure for this tonemap controller


Returns:
float - No Description Set


 .. _CToneMapControllerComponent.SetBloomScale:
void CToneMapControllerComponent.SetBloomScale(float a)---------------

Sets bloom scale for this tonemap controller


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CToneMapControllerComponent.SetMaxExposure:
void CToneMapControllerComponent.SetMaxExposure(float a)---------------

Sets max exposure for this tonemap controller


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CToneMapControllerComponent.SetMinExposure:
void CToneMapControllerComponent.SetMinExposure(float a)---------------

Sets min exposure for this tonemap controller


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDebugOverlayScriptHelper.Axis:
void CDebugOverlayScriptHelper.Axis(Vector a, Quaternion b, float c, bool d, float e)---------------

Draws an axis. Specify origin + orientation in world space.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector |  | No Description Set |
|  Quaternion |  | No Description Set |
|  float |  | No Description Set |
|  bool |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDebugOverlayScriptHelper.Box:
void CDebugOverlayScriptHelper.Box(Vector a, Vector b, int c, int d, int e, int f, bool g, float h)---------------

Draws a world-space axis-aligned box. Specify bounds in world space.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector |  | No Description Set |
|  Vector |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  bool |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDebugOverlayScriptHelper.BoxAngles:
void CDebugOverlayScriptHelper.BoxAngles(Vector a, Vector b, Vector c, Quaternion d, int e, int f, int g, int h, bool i, float j)---------------

Draws an oriented box at the origin. Specify bounds in local space.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector |  | No Description Set |
|  Vector |  | No Description Set |
|  Vector |  | No Description Set |
|  Quaternion |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  bool |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDebugOverlayScriptHelper.Capsule:
void CDebugOverlayScriptHelper.Capsule(Vector a, Quaternion b, float c, float d, int e, int f, int g, int h, bool i, float j)---------------

Draws a capsule. Specify base in world space.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector |  | No Description Set |
|  Quaternion |  | No Description Set |
|  float |  | No Description Set |
|  float |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  bool |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDebugOverlayScriptHelper.Circle:
void CDebugOverlayScriptHelper.Circle(Vector a, Quaternion b, float c, int d, int e, int f, int g, bool h, float i)---------------

Draws a circle. Specify center in world space.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector |  | No Description Set |
|  Quaternion |  | No Description Set |
|  float |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  bool |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDebugOverlayScriptHelper.CircleScreenOriented:
void CDebugOverlayScriptHelper.CircleScreenOriented(Vector a, float b, int c, int d, int e, int f, bool g, float h)---------------

Draws a circle oriented to the screen. Specify center in world space.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector |  | No Description Set |
|  float |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  bool |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDebugOverlayScriptHelper.Cone:
void CDebugOverlayScriptHelper.Cone(Vector a, Vector b, float c, float d, int e, int f, int g, int h, bool i, float j)---------------

Draws a wireframe cone. Specify endpoint and direction in world space.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector |  | No Description Set |
|  Vector |  | No Description Set |
|  float |  | No Description Set |
|  float |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  bool |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDebugOverlayScriptHelper.Cross:
void CDebugOverlayScriptHelper.Cross(Vector a, float b, int c, int d, int e, int f, bool g, float h)---------------

Draws a screen-aligned cross. Specify origin in world space.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector |  | No Description Set |
|  float |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  bool |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDebugOverlayScriptHelper.Cross3D:
void CDebugOverlayScriptHelper.Cross3D(Vector a, float b, int c, int d, int e, int f, bool g, float h)---------------

Draws a world-aligned cross. Specify origin in world space.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector |  | No Description Set |
|  float |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  bool |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDebugOverlayScriptHelper.Cross3DOriented:
void CDebugOverlayScriptHelper.Cross3DOriented(Vector a, Quaternion b, float c, int d, int e, int f, int g, bool h, float i)---------------

Draws an oriented cross. Specify origin in world space.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector |  | No Description Set |
|  Quaternion |  | No Description Set |
|  float |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  bool |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDebugOverlayScriptHelper.DrawTickMarkedLine:
void CDebugOverlayScriptHelper.DrawTickMarkedLine(Vector a, Vector b, float c, int d, int e, int f, int g, int h, bool i, float j)---------------

Draws a dashed line. Specify endpoint's in world space.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector |  | No Description Set |
|  Vector |  | No Description Set |
|  float |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  bool |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDebugOverlayScriptHelper.EntityAttachments:
void CDebugOverlayScriptHelper.EntityAttachments(ehandle a, float b)---------------

Draws the attachments of the entity


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  ehandle |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDebugOverlayScriptHelper.EntityAxis:
void CDebugOverlayScriptHelper.EntityAxis(ehandle a, float b, bool c, float d)---------------

Draws the axis of the entity origin


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  ehandle |  | No Description Set |
|  float |  | No Description Set |
|  bool |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDebugOverlayScriptHelper.EntityBounds:
void CDebugOverlayScriptHelper.EntityBounds(ehandle a, int b, int c, int d, int e, bool f, float g)---------------

Draws bounds of an entity


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  ehandle |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  bool |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDebugOverlayScriptHelper.EntitySkeleton:
void CDebugOverlayScriptHelper.EntitySkeleton(ehandle a, float b)---------------

Draws the skeleton of the entity


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  ehandle |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDebugOverlayScriptHelper.EntityText:
void CDebugOverlayScriptHelper.EntityText(ehandle a, int b, string c, int d, int e, int f, int g, float h)---------------

Draws text on an entity


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  ehandle |  | No Description Set |
|  int |  | No Description Set |
|  string |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDebugOverlayScriptHelper.FilledRect2D:
void CDebugOverlayScriptHelper.FilledRect2D(Vector2D a, Vector2D b, int c, int d, int e, int f, float g)---------------

Draws a screen-space filled 2D rectangle. Coordinates are in pixels.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector2D |  | No Description Set |
|  Vector2D |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDebugOverlayScriptHelper.HorzArrow:
void CDebugOverlayScriptHelper.HorzArrow(Vector a, Vector b, float c, int d, int e, int f, int g, bool h, float i)---------------

Draws a horizontal arrow. Specify endpoint's in world space.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector |  | No Description Set |
|  Vector |  | No Description Set |
|  float |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  bool |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDebugOverlayScriptHelper.Line:
void CDebugOverlayScriptHelper.Line(Vector a, Vector b, int c, int d, int e, int f, bool g, float h)---------------

Draws a line between two point's


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector |  | No Description Set |
|  Vector |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  bool |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDebugOverlayScriptHelper.Line2D:
void CDebugOverlayScriptHelper.Line2D(Vector2D a, Vector2D b, int c, int d, int e, int f, float g)---------------

Draws a line between two point's in screenspace


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector2D |  | No Description Set |
|  Vector2D |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDebugOverlayScriptHelper.PopDebugOverlayScope:
void CDebugOverlayScriptHelper.PopDebugOverlayScope()---------------

Pops the identifier used to group overlays. Overlays marked with this identifier can be deleted in a big batch.




 .. _CDebugOverlayScriptHelper.PushAndClearDebugOverlayScope:
void CDebugOverlayScriptHelper.PushAndClearDebugOverlayScope(utlstringtoken a)---------------

Pushes an identifier used to group overlays. Deletes all existing overlays using this overlay id.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  utlstringtoken |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDebugOverlayScriptHelper.PushDebugOverlayScope:
void CDebugOverlayScriptHelper.PushDebugOverlayScope(utlstringtoken a)---------------

Pushes an identifier used to group overlays. Overlays marked with this identifier can be deleted in a big batch.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  utlstringtoken |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDebugOverlayScriptHelper.RemoveAllInScope:
void CDebugOverlayScriptHelper.RemoveAllInScope(utlstringtoken a)---------------

Removes all overlays marked with a specific identifier, regardless of their lifetime.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  utlstringtoken |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDebugOverlayScriptHelper.SolidCone:
void CDebugOverlayScriptHelper.SolidCone(Vector a, Vector b, float c, float d, int e, int f, int g, int h, bool i, float j)---------------

Draws a solid cone. Specify endpoint and direction in world space.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector |  | No Description Set |
|  Vector |  | No Description Set |
|  float |  | No Description Set |
|  float |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  bool |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDebugOverlayScriptHelper.Sphere:
void CDebugOverlayScriptHelper.Sphere(Vector a, float b, int c, int d, int e, int f, bool g, float h)---------------

Draws a wireframe sphere. Specify center in world space.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector |  | No Description Set |
|  float |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  bool |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDebugOverlayScriptHelper.SweptBox:
void CDebugOverlayScriptHelper.SweptBox(Vector a, Vector b, Vector c, Vector d, Quaternion e, int f, int g, int h, int i, float j)---------------

Draws a swept box. Specify endpoint's in world space and the bounds in local space.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector |  | No Description Set |
|  Vector |  | No Description Set |
|  Vector |  | No Description Set |
|  Vector |  | No Description Set |
|  Quaternion |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDebugOverlayScriptHelper.Text:
void CDebugOverlayScriptHelper.Text(Vector a, int b, string c, float d, int e, int f, int g, int h, float i)---------------

Draws 2D text. Specify origin in world space.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector |  | No Description Set |
|  int |  | No Description Set |
|  string |  | No Description Set |
|  float |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDebugOverlayScriptHelper.Texture:
void CDebugOverlayScriptHelper.Texture(string a, Vector2D b, Vector2D c, int d, int e, int f, int g, Vector2D h, Vector2D i, float j)---------------

Draws a screen-space texture. Coordinates are in pixels.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
|  Vector2D |  | No Description Set |
|  Vector2D |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  Vector2D |  | No Description Set |
|  Vector2D |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDebugOverlayScriptHelper.Triangle:
void CDebugOverlayScriptHelper.Triangle(Vector a, Vector b, Vector c, int d, int e, int f, int g, bool h, float i)---------------

Draws a filled triangle. Specify vertices in world space.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector |  | No Description Set |
|  Vector |  | No Description Set |
|  Vector |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  bool |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDebugOverlayScriptHelper.UnitTestCycleOverlayRenderType:
void CDebugOverlayScriptHelper.UnitTestCycleOverlayRenderType()---------------

Toggles the overlay render type, for unit tests




 .. _CDebugOverlayScriptHelper.VectorText3D:
void CDebugOverlayScriptHelper.VectorText3D(Vector a, Quaternion b, string c, int d, int e, int f, int g, bool h, float i)---------------

Draws 3D text. Specify origin + orientation in world space.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector |  | No Description Set |
|  Quaternion |  | No Description Set |
|  string |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  bool |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDebugOverlayScriptHelper.VertArrow:
void CDebugOverlayScriptHelper.VertArrow(Vector a, Vector b, float c, int d, int e, int f, int g, bool h, float i)---------------

Draws a vertical arrow. Specify endpoint's in world space.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector |  | No Description Set |
|  Vector |  | No Description Set |
|  float |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  bool |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDebugOverlayScriptHelper.YawArrow:
void CDebugOverlayScriptHelper.YawArrow(Vector a, float b, float c, float d, int e, int f, int g, int h, bool i, float j)---------------

Draws a arrow associated with a specific yaw. Specify endpoint's in world space.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector |  | No Description Set |
|  float |  | No Description Set |
|  float |  | No Description Set |
|  float |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  bool |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseFlex.GetCurrentScene:
handle CBaseFlex.GetCurrentScene()---------------

Returns the instance of the oldest active scene entity '''(if any).


Returns:
handle - No Description Set


 .. _CBaseFlex.GetSceneByIndex:
handle CBaseFlex.GetSceneByIndex(int a)---------------

Returns the instance of the scene entity at the specified index.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _CSceneEntity.AddBroadcastTeamTarget:
void CSceneEntity.AddBroadcastTeamTarget(int a)---------------

Adds a team (by index) to the broadcast list


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CSceneEntity.Cancel:
void CSceneEntity.Cancel()---------------

Cancel scene playback




 .. _CSceneEntity.EstimateLength:
float CSceneEntity.EstimateLength()---------------

Returns length of this scene in seconds.


Returns:
float - No Description Set


 .. _CSceneEntity.FindCamera:
handle CSceneEntity.FindCamera()---------------

Get the camera


Returns:
handle - No Description Set


 .. _CSceneEntity.FindNamedEntity:
handle CSceneEntity.FindNamedEntity(string a)---------------

given an entity reference, such as !target, get actual entity from scene object


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _CSceneEntity.IsPaused:
bool CSceneEntity.IsPaused()---------------

If this scene is currently paused.


Returns:
bool - No Description Set


 .. _CSceneEntity.IsPlayingBack:
bool CSceneEntity.IsPlayingBack()---------------

If this scene is currently playing.


Returns:
bool - No Description Set


 .. _CSceneEntity.LoadSceneFromString:
bool CSceneEntity.LoadSceneFromString(string a, string b)---------------

given a dummy scene name and a vcd ''string'', load the scene


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
|  string |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _CSceneEntity.RemoveBroadcastTeamTarget:
void CSceneEntity.RemoveBroadcastTeamTarget(int a)---------------

Removes a team (by index) from the broadcast list


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CSceneEntity.Start:
void CSceneEntity.Start(handle a)---------------

Start scene playback, takes activatorEntity as param


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _GridNav.GridPosToWorldCenterX:
float GridNav.GridPosToWorldCenterX(int a)---------------

Get the X position of the center of a given X index


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
float - No Description Set


 .. _GridNav.GridPosToWorldCenterY:
float GridNav.GridPosToWorldCenterY(int a)---------------

Get the Y position of the center of a given Y index


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
float - No Description Set


 .. _GridNav.IsBlocked:
bool GridNav.IsBlocked(Vector a)---------------

Checks whether the given position is blocked


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _GridNav.IsNearbyTree:
bool GridNav.IsNearbyTree(Vector position, float radius, bool c)---------------

 


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector | position | No Description Set |
|  float | radius | No Description Set |
|  bool |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _GridNav.IsTraversable:
bool GridNav.IsTraversable(Vector a)---------------

Checks whether the given position is traversable


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  Vector |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _GridNav.RegrowAllTrees:
void GridNav.RegrowAllTrees()---------------

 




 .. _GridNav.WorldToGridPosX:
int GridNav.WorldToGridPosX(float a)---------------

Get the X index of a given world X position


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _GridNav.WorldToGridPosY:
int GridNav.WorldToGridPosY(float a)---------------

Get the Y index of a given world Y position


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  float |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _Convars.GetBool:
table Convars.GetBool(string variableName)---------------

GetBool(name) : returns the convar as a boolean flag.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string | variableName | No Description Set |
+-----------+--------------+--------------+
Returns:
table - No Description Set


 .. _Convars.GetCommandClient:
handle Convars.GetCommandClient()---------------

GetCommandClient() : returns the player who issued this console command.


Returns:
handle - No Description Set


 .. _Convars.GetDOTACommandClient:
handle Convars.GetDOTACommandClient()---------------

GetDOTACommandClient() : returns the DOTA player who issued this console command.


Returns:
handle - No Description Set


 .. _Convars.GetFloat:
table Convars.GetFloat(string name)---------------

GetFloat(name) : returns the convar as a ''float''. May return ''nil'' if no such convar.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string | name | No Description Set |
+-----------+--------------+--------------+
Returns:
table - No Description Set


 .. _Convars.GetInt:
table Convars.GetInt(string a)---------------

GetInt(name) : returns the convar as an ''int''. May return ''nil'' if no such convar.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
+-----------+--------------+--------------+
Returns:
table - No Description Set


 .. _Convars.GetStr:
table Convars.GetStr(string variableName)---------------

GetStr(name) : returns the convar as a ''string''. May return ''nil'' if no such convar.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string | variableName | No Description Set |
+-----------+--------------+--------------+
Returns:
table - No Description Set


 .. _Convars.RegisterCommand:
void Convars.RegisterCommand(string variableName, handle function, string helpText, int flags)---------------

RegisterCommand(name, fn, helpString, flags) : register a console command.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string | variableName | No Description Set |
|  handle | function | A lua function to call when this concommand is run |
|  string | helpText | No Description Set |
|  int | flags | FCVAR flags |
+-----------+--------------+--------------+


 .. _Convars.RegisterConvar:
void Convars.RegisterConvar(string name, string defaultValue, string helpText, int flags)---------------

RegisterConvar(name, defaultValue, helpString, flags): register a new console variable.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string | name | No Description Set |
|  string | defaultValue | No Description Set |
|  string | helpText | No Description Set |
|  int | flags | FCVAR flags |
+-----------+--------------+--------------+


 .. _Convars.SetBool:
void Convars.SetBool(string variableName, bool value)---------------

SetBool(name, val) : sets the value of the convar to the ''bool''.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string | variableName | No Description Set |
|  bool | value | No Description Set |
+-----------+--------------+--------------+


 .. _Convars.SetFloat:
void Convars.SetFloat(string variableName, float value)---------------

SetFloat(name, val) : sets the value of the convar to the ''float''.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string | variableName | No Description Set |
|  float | value | No Description Set |
+-----------+--------------+--------------+


 .. _Convars.SetInt:
void Convars.SetInt(string a, int b)---------------

SetInt(name, val) : sets the value of the convar to the ''int''.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _Convars.SetStr:
void Convars.SetStr(string a, string b)---------------

SetStr(name, val) : sets the value of the convar to the ''string''.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+===========+==============+==============+
|  string |  | No Description Set |
|  string |  | No Description Set |
+-----------+--------------+--------------+


