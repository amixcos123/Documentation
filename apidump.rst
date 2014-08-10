Dota 2 Lua API
==============
{{Note | This page is automatically generated.  Any changes may be overwritten}}
  
==='''Accessing the DOTA 2 Scripting API from Lua===

While Lua is [http://en.wikipedia.org/wiki/Dynamically_typed dynamically typed], the DOTA 2 engine is written primarily in C++, which is [http://en.wikipedia.org/wiki/Type_system#Static_type-checking statically typed]. Thus, you'll need to be conscious of your data types when calling the API. (If you try to pass the wrong type to an API function, you'll get an error message in Vconsole telling you what you passed and what it was expecting.)


Global
############
Global functions.  These can be called without any class
  * :ref:`Global.AngleDiff`
  * :ref:`Global.AppendToLogFile`
  * :ref:`Global.ApplyDamage`
  * :ref:`Global.AxisAngleToQuaternion`
  * :ref:`Global.CancelEntityIOEvents`
  * :ref:`Global.CreateEffect`
  * :ref:`Global.CreateHeroForPlayer`
  * :ref:`Global.CreateItem`
  * :ref:`Global.CreateItemOnPositionSync`
  * :ref:`Global.CreateTrigger`
  * :ref:`Global.CreateTriggerRadiusApproximate`
  * :ref:`Global.CreateUnitByName`
  * :ref:`Global.CreateUnitByNameAsync`
  * :ref:`Global.cvar_getf`
  * :ref:`Global.cvar_setf`
  * :ref:`Global.DebugBreak`
  * :ref:`Global.DebugDrawBox`
  * :ref:`Global.DebugDrawBoxDirection`
  * :ref:`Global.DebugDrawCircle`
  * :ref:`Global.DebugDrawClear`
  * :ref:`Global.DebugDrawLine`
  * :ref:`Global.DebugDrawLine_vCol`
  * :ref:`Global.DebugDrawScreenTextLine`
  * :ref:`Global.DebugDrawSphere`
  * :ref:`Global.DebugDrawText`
  * :ref:`Global.DebugScreenTextPretty`
  * :ref:`Global.DoEntFire`
  * :ref:`Global.DoEntFireByInstanceHandle`
  * :ref:`Global.DoIncludeScript`
  * :ref:`Global.DoScriptAssert`
  * :ref:`Global.DoUniqueString`
  * :ref:`Global.EmitGlobalSound`
  * :ref:`Global.EmitSoundOn`
  * :ref:`Global.EmitSoundOnClient`
  * :ref:`Global.EntIndexToHScript`
  * :ref:`Global.ExecuteOrderFromTable`
  * :ref:`Global.ExponentialDecay`
  * :ref:`Global.FileToString`
  * :ref:`Global.FindClearSpaceForUnit`
  * :ref:`Global.FindUnitsInRadius`
  * :ref:`Global.FireEntityIOInputNameOnly`
  * :ref:`Global.FireEntityIOInputString`
  * :ref:`Global.FireEntityIOInputVec`
  * :ref:`Global.FireGameEvent`
  * :ref:`Global.FireGameEventLocal`
  * :ref:`Global.FrameTime`
  * :ref:`Global.GetFrameCount`
  * :ref:`Global.GetFrostyBoostAmount`
  * :ref:`Global.GetFrostyPointsForRound`
  * :ref:`Global.GetGoldFrostyBoostAmount`
  * :ref:`Global.GetGoldFrostyPointsForRound`
  * :ref:`Global.GetGroundPosition`
  * :ref:`Global.GetListenServerHost`
  * :ref:`Global.GetMapName`
  * :ref:`Global.GetMaxOutputDelay`
  * :ref:`Global.GetPhysAngularVelocity`
  * :ref:`Global.GetPhysVelocity`
  * :ref:`Global.GetSystemDate`
  * :ref:`Global.GetSystemTime`
  * :ref:`Global.GetWorldMaxX`
  * :ref:`Global.GetWorldMaxY`
  * :ref:`Global.GetWorldMinX`
  * :ref:`Global.GetWorldMinY`
  * :ref:`Global.InitLogFile`
  * :ref:`Global.IsDedicatedServer`
  * :ref:`Global.IsMarkedForDeletion`
  * :ref:`Global.IsValidEntity`
  * :ref:`Global.ListenToGameEvent`
  * :ref:`Global.LoadKeyValues`
  * :ref:`Global.LoadKeyValuesFromString`
  * :ref:`Global.MakeStringToken`
  * :ref:`Global.Msg`
  * :ref:`Global.PauseGame`
  * :ref:`Global.PlayerInstanceFromIndex`
  * :ref:`Global.PrecacheEntityFromTable`
  * :ref:`Global.PrecacheEntityListFromTable`
  * :ref:`Global.PrecacheItemByNameAsync`
  * :ref:`Global.PrecacheItemByNameSync`
  * :ref:`Global.PrecacheModel`
  * :ref:`Global.PrecacheResource`
  * :ref:`Global.PrecacheUnitByNameAsync`
  * :ref:`Global.PrecacheUnitByNameSync`
  * :ref:`Global.PrintLinkedConsoleMessage`
  * :ref:`Global.RandomFloat`
  * :ref:`Global.RandomInt`
  * :ref:`Global.RandomVector`
  * :ref:`Global.RegisterSpawnGroupFilterProxy`
  * :ref:`Global.ReloadMOTD`
  * :ref:`Global.RemoveSpawnGroupFilterProxy`
  * :ref:`Global.RollPercentage`
  * :ref:`Global.RotateOrientation`
  * :ref:`Global.RotatePosition`
  * :ref:`Global.RotateQuaternionByAxisAngle`
  * :ref:`Global.RotationDelta`
  * :ref:`Global.rr_AddDecisionRule`
  * :ref:`Global.rr_CommitAIResponse`
  * :ref:`Global.rr_GetResponseTargets`
  * :ref:`Global.rr_QueryBestResponse`
  * :ref:`Global.Say`
  * :ref:`Global.ScreenShake`
  * :ref:`Global.SendFrostivusTimeElapsedToGC`
  * :ref:`Global.SendFrostyPointsMessageToGC`
  * :ref:`Global.SendToConsole`
  * :ref:`Global.SendToServerConsole`
  * :ref:`Global.SetOpvarFloatAll`
  * :ref:`Global.SetOpvarFloatPlayer`
  * :ref:`Global.SetQuestName`
  * :ref:`Global.SetQuestPhase`
  * :ref:`Global.SetRenderingEnabled`
  * :ref:`Global.ShowGenericPopup`
  * :ref:`Global.ShowGenericPopupToPlayer`
  * :ref:`Global.ShowMessage`
  * :ref:`Global.SpawnEntityFromTableSynchronous`
  * :ref:`Global.SpawnEntityGroupFromTable`
  * :ref:`Global.SpawnEntityListFromTableAsynchronous`
  * :ref:`Global.SpawnEntityListFromTableSynchronous`
  * :ref:`Global.SplineQuaternions`
  * :ref:`Global.SplineVectors`
  * :ref:`Global.StartSoundEvent`
  * :ref:`Global.StopEffect`
  * :ref:`Global.StopListeningToAllGameEvents`
  * :ref:`Global.StopListeningToGameEvent`
  * :ref:`Global.StopSoundEvent`
  * :ref:`Global.StopSoundOn`
  * :ref:`Global.StringToFile`
  * :ref:`Global.Time`
  * :ref:`Global.TraceCollideable`
  * :ref:`Global.TraceHull`
  * :ref:`Global.TraceLine`
  * :ref:`Global.UnloadSpawnGroup`
  * :ref:`Global.UnloadSpawnGroupByHandle`
  * :ref:`Global.UpdateEventPoints`
  * :ref:`Global.UTIL_Remove`
  * :ref:`Global.UTIL_RemoveImmediate`
  * :ref:`Global.VectorToAngles`
  * :ref:`Global.Warning`
CBaseEntity
############
The base class for stuff
  * :ref:`CBaseEntity.ApplyAbsVelocityImpulse`
  * :ref:`CBaseEntity.ApplyLocalAngularVelocityImpulse`
  * :ref:`CBaseEntity.EmitSound`
  * :ref:`CBaseEntity.EmitSoundParams`
  * :ref:`CBaseEntity.EyeAngles`
  * :ref:`CBaseEntity.EyePosition`
  * :ref:`CBaseEntity.FirstMoveChild`
  * :ref:`CBaseEntity.GatherCriteria`
  * :ref:`CBaseEntity.GetAbsOrigin`
  * :ref:`CBaseEntity.GetAngles`
  * :ref:`CBaseEntity.GetAnglesAsVector`
  * :ref:`CBaseEntity.GetAngularVelocity`
  * :ref:`CBaseEntity.GetBaseVelocity`
  * :ref:`CBaseEntity.GetBoundingMaxs`
  * :ref:`CBaseEntity.GetBoundingMins`
  * :ref:`CBaseEntity.GetBounds`
  * :ref:`CBaseEntity.GetCenter`
  * :ref:`CBaseEntity.GetChildren`
  * :ref:`CBaseEntity.GetContext`
  * :ref:`CBaseEntity.GetForwardVector`
  * :ref:`CBaseEntity.GetHealth`
  * :ref:`CBaseEntity.GetLocalAngularVelocity`
  * :ref:`CBaseEntity.GetLocalVelocity`
  * :ref:`CBaseEntity.GetMaxHealth`
  * :ref:`CBaseEntity.GetModelName`
  * :ref:`CBaseEntity.GetMoveParent`
  * :ref:`CBaseEntity.GetOrigin`
  * :ref:`CBaseEntity.GetOwner`
  * :ref:`CBaseEntity.GetOwnerEntity`
  * :ref:`CBaseEntity.GetRightVector`
  * :ref:`CBaseEntity.GetRootMoveParent`
  * :ref:`CBaseEntity.GetSoundDuration`
  * :ref:`CBaseEntity.GetTeam`
  * :ref:`CBaseEntity.GetUpVector`
  * :ref:`CBaseEntity.GetVelocity`
  * :ref:`CBaseEntity.IsAlive`
  * :ref:`CBaseEntity.IsPlayer`
  * :ref:`CBaseEntity.Kill`
  * :ref:`CBaseEntity.NextMovePeer`
  * :ref:`CBaseEntity.OverrideFriction`
  * :ref:`CBaseEntity.PrecacheScriptSound`
  * :ref:`CBaseEntity.SetAbsOrigin`
  * :ref:`CBaseEntity.SetAngles`
  * :ref:`CBaseEntity.SetAngularVelocity`
  * :ref:`CBaseEntity.SetContext`
  * :ref:`CBaseEntity.SetContextNum`
  * :ref:`CBaseEntity.SetContextThink`
  * :ref:`CBaseEntity.SetForwardVector`
  * :ref:`CBaseEntity.SetFriction`
  * :ref:`CBaseEntity.SetGravity`
  * :ref:`CBaseEntity.SetHealth`
  * :ref:`CBaseEntity.SetMaxHealth`
  * :ref:`CBaseEntity.SetModel`
  * :ref:`CBaseEntity.SetOrigin`
  * :ref:`CBaseEntity.SetOwner`
  * :ref:`CBaseEntity.SetParent`
  * :ref:`CBaseEntity.SetRenderColor`
  * :ref:`CBaseEntity.SetSize`
  * :ref:`CBaseEntity.SetTeam`
  * :ref:`CBaseEntity.SetVelocity`
  * :ref:`CBaseEntity.StopSound`
  * :ref:`CBaseEntity.Trigger`
CEntities
############
No Description Set
  * :ref:`CEntities.CreateByClassname`
  * :ref:`CEntities.FindAllByClassname`
  * :ref:`CEntities.FindAllByClassnameWithin`
  * :ref:`CEntities.FindAllByModel`
  * :ref:`CEntities.FindAllByName`
  * :ref:`CEntities.FindAllByNameWithin`
  * :ref:`CEntities.FindAllByTarget`
  * :ref:`CEntities.FindAllInSphere`
  * :ref:`CEntities.FindByClassname`
  * :ref:`CEntities.FindByClassnameNearest`
  * :ref:`CEntities.FindByClassnameWithin`
  * :ref:`CEntities.FindByModel`
  * :ref:`CEntities.FindByModelWithin`
  * :ref:`CEntities.FindByName`
  * :ref:`CEntities.FindByNameNearest`
  * :ref:`CEntities.FindByNameWithin`
  * :ref:`CEntities.FindByTarget`
  * :ref:`CEntities.FindInSphere`
  * :ref:`CEntities.First`
  * :ref:`CEntities.Next`
CEntityInstance
############
extends CBaseEntity
No Description Set
  * :ref:`CEntityInstance.ConnectOutput`
  * :ref:`CEntityInstance.Destroy`
  * :ref:`CEntityInstance.DisconnectOutput`
  * :ref:`CEntityInstance.DisconnectRedirectedOutput`
  * :ref:`CEntityInstance.entindex`
  * :ref:`CEntityInstance.FireOutput`
  * :ref:`CEntityInstance.GetClassname`
  * :ref:`CEntityInstance.GetDebugName`
  * :ref:`CEntityInstance.GetEntityHandle`
  * :ref:`CEntityInstance.GetEntityIndex`
  * :ref:`CEntityInstance.GetIntAttr`
  * :ref:`CEntityInstance.GetName`
  * :ref:`CEntityInstance.GetOrCreatePrivateScriptScope`
  * :ref:`CEntityInstance.GetOrCreatePublicScriptScope`
  * :ref:`CEntityInstance.GetPrivateScriptScope`
  * :ref:`CEntityInstance.GetPublicScriptScope`
  * :ref:`CEntityInstance.RedirectOutput`
  * :ref:`CEntityInstance.RemoveSelf`
  * :ref:`CEntityInstance.SetIntAttr`
CDOTABaseAbility
############
extends CBaseEntity
No Description Set
  * :ref:`CDOTABaseAbility.CastAbility`
  * :ref:`CDOTABaseAbility.ContinueCasting`
  * :ref:`CDOTABaseAbility.CreateVisibilityNode`
  * :ref:`CDOTABaseAbility.DecrementModifierRefCount`
  * :ref:`CDOTABaseAbility.EndChannel`
  * :ref:`CDOTABaseAbility.EndCooldown`
  * :ref:`CDOTABaseAbility.GetAbilityDamage`
  * :ref:`CDOTABaseAbility.GetAbilityDamageType`
  * :ref:`CDOTABaseAbility.GetAbilityIndex`
  * :ref:`CDOTABaseAbility.GetAbilityName`
  * :ref:`CDOTABaseAbility.GetAbilityTargetFlags`
  * :ref:`CDOTABaseAbility.GetAbilityTargetTeam`
  * :ref:`CDOTABaseAbility.GetAbilityTargetType`
  * :ref:`CDOTABaseAbility.GetAbilityType`
  * :ref:`CDOTABaseAbility.GetAnimationIgnoresModelScale`
  * :ref:`CDOTABaseAbility.GetAssociatedPrimaryAbilities`
  * :ref:`CDOTABaseAbility.GetAssociatedSecondaryAbilities`
  * :ref:`CDOTABaseAbility.GetAutoCastState`
  * :ref:`CDOTABaseAbility.GetBackswingTime`
  * :ref:`CDOTABaseAbility.GetBehavior`
  * :ref:`CDOTABaseAbility.GetCaster`
  * :ref:`CDOTABaseAbility.GetCastPoint`
  * :ref:`CDOTABaseAbility.GetCastRange`
  * :ref:`CDOTABaseAbility.GetChannelledManaCostPerSecond`
  * :ref:`CDOTABaseAbility.GetChannelStartTime`
  * :ref:`CDOTABaseAbility.GetChannelTime`
  * :ref:`CDOTABaseAbility.GetCloneSource`
  * :ref:`CDOTABaseAbility.GetConceptRecipientType`
  * :ref:`CDOTABaseAbility.GetCooldown`
  * :ref:`CDOTABaseAbility.GetCooldownTime`
  * :ref:`CDOTABaseAbility.GetCooldownTimeRemaining`
  * :ref:`CDOTABaseAbility.GetCursorPosition`
  * :ref:`CDOTABaseAbility.GetCursorTarget`
  * :ref:`CDOTABaseAbility.GetCursorTargetingNothing`
  * :ref:`CDOTABaseAbility.GetDuration`
  * :ref:`CDOTABaseAbility.GetGoldCost`
  * :ref:`CDOTABaseAbility.GetGoldCostForUpgrade`
  * :ref:`CDOTABaseAbility.GetHeroLevelRequiredToUpgrade`
  * :ref:`CDOTABaseAbility.GetIntrinsicModifierName`
  * :ref:`CDOTABaseAbility.GetLevel`
  * :ref:`CDOTABaseAbility.GetLevelSpecialValueFor`
  * :ref:`CDOTABaseAbility.GetManaCost`
  * :ref:`CDOTABaseAbility.GetMaxLevel`
  * :ref:`CDOTABaseAbility.GetModifierValue`
  * :ref:`CDOTABaseAbility.GetModifierValueBonus`
  * :ref:`CDOTABaseAbility.GetPlaybackRateOverride`
  * :ref:`CDOTABaseAbility.GetSharedCooldownName`
  * :ref:`CDOTABaseAbility.GetSpecialValueFor`
  * :ref:`CDOTABaseAbility.GetStolenActivityModifier`
  * :ref:`CDOTABaseAbility.GetToggleState`
  * :ref:`CDOTABaseAbility.HeroXPChange`
  * :ref:`CDOTABaseAbility.IncrementModifierRefCount`
  * :ref:`CDOTABaseAbility.IsActivated`
  * :ref:`CDOTABaseAbility.IsAttributeBonus`
  * :ref:`CDOTABaseAbility.IsChanneling`
  * :ref:`CDOTABaseAbility.IsCooldownReady`
  * :ref:`CDOTABaseAbility.IsCosmetic`
  * :ref:`CDOTABaseAbility.IsFullyCastable`
  * :ref:`CDOTABaseAbility.IsHidden`
  * :ref:`CDOTABaseAbility.IsHiddenWhenStolen`
  * :ref:`CDOTABaseAbility.IsInAbilityPhase`
  * :ref:`CDOTABaseAbility.IsItem`
  * :ref:`CDOTABaseAbility.IsOwnersGoldEnough`
  * :ref:`CDOTABaseAbility.IsOwnersGoldEnoughForUpgrade`
  * :ref:`CDOTABaseAbility.IsOwnersManaEnough`
  * :ref:`CDOTABaseAbility.IsPassive`
  * :ref:`CDOTABaseAbility.IsSharedWithTeammates`
  * :ref:`CDOTABaseAbility.IsStealable`
  * :ref:`CDOTABaseAbility.IsStolen`
  * :ref:`CDOTABaseAbility.IsToggle`
  * :ref:`CDOTABaseAbility.IsTrained`
  * :ref:`CDOTABaseAbility.MarkAbilityButtonDirty`
  * :ref:`CDOTABaseAbility.NumModifiersUsingAbility`
  * :ref:`CDOTABaseAbility.OnAbilityPhaseInterrupted`
  * :ref:`CDOTABaseAbility.OnAbilityPhaseStart`
  * :ref:`CDOTABaseAbility.OnAbilityPinged`
  * :ref:`CDOTABaseAbility.OnChannelFinish`
  * :ref:`CDOTABaseAbility.OnChannelThink`
  * :ref:`CDOTABaseAbility.OnHeroCalculateStatBonus`
  * :ref:`CDOTABaseAbility.OnHeroLevelUp`
  * :ref:`CDOTABaseAbility.OnInventoryContentsChanged`
  * :ref:`CDOTABaseAbility.OnOwnerDied`
  * :ref:`CDOTABaseAbility.OnOwnerSpawned`
  * :ref:`CDOTABaseAbility.OnSpellStart`
  * :ref:`CDOTABaseAbility.OnToggle`
  * :ref:`CDOTABaseAbility.OnUpgrade`
  * :ref:`CDOTABaseAbility.PayGoldCost`
  * :ref:`CDOTABaseAbility.PayGoldCostForUpgrade`
  * :ref:`CDOTABaseAbility.PayManaCost`
  * :ref:`CDOTABaseAbility.PlaysDefaultAnimWhenStolen`
  * :ref:`CDOTABaseAbility.ProcsMagicStick`
  * :ref:`CDOTABaseAbility.RefCountsModifiers`
  * :ref:`CDOTABaseAbility.RefundManaCost`
  * :ref:`CDOTABaseAbility.ResetToggleOnRespawn`
  * :ref:`CDOTABaseAbility.SetAbilityIndex`
  * :ref:`CDOTABaseAbility.SetActivated`
  * :ref:`CDOTABaseAbility.SetChanneling`
  * :ref:`CDOTABaseAbility.SetHidden`
  * :ref:`CDOTABaseAbility.SetInAbilityPhase`
  * :ref:`CDOTABaseAbility.SetLevel`
  * :ref:`CDOTABaseAbility.SetOverrideCastPoint`
  * :ref:`CDOTABaseAbility.SetRefCountsModifiers`
  * :ref:`CDOTABaseAbility.SetStolen`
  * :ref:`CDOTABaseAbility.ShouldUseResources`
  * :ref:`CDOTABaseAbility.SpeakAbilityConcept`
  * :ref:`CDOTABaseAbility.SpeakTrigger`
  * :ref:`CDOTABaseAbility.StartCooldown`
  * :ref:`CDOTABaseAbility.ToggleAbility`
  * :ref:`CDOTABaseAbility.ToggleAutoCast`
  * :ref:`CDOTABaseAbility.UpgradeAbility`
  * :ref:`CDOTABaseAbility.UseResources`
CDOTA_Ability_Animation_Attack
############
extends CDOTABaseAbility
No Description Set
  * :ref:`CDOTA_Ability_Animation_Attack.SetPlaybackRate`
CDOTA_Ability_Animation_TailSpin
############
extends CDOTABaseAbility
No Description Set
  * :ref:`CDOTA_Ability_Animation_TailSpin.SetPlaybackRate`
CDOTA_Ability_Nian_Leap
############
extends CDOTABaseAbility
No Description Set
  * :ref:`CDOTA_Ability_Nian_Leap.SetPlaybackRate`
CDOTA_Ability_Nian_Dive
############
extends CDOTABaseAbility
No Description Set
  * :ref:`CDOTA_Ability_Nian_Dive.SetPlaybackRate`
CDOTA_Ability_Nian_Roar
############
extends CDOTABaseAbility
No Description Set
  * :ref:`CDOTA_Ability_Nian_Roar.GetCastCount`
CDOTA_Item
############
extends CDOTABaseAbility
No Description Set
  * :ref:`CDOTA_Item.GetContainer`
  * :ref:`CDOTA_Item.GetCost`
  * :ref:`CDOTA_Item.GetCurrentCharges`
  * :ref:`CDOTA_Item.GetInitialCharges`
  * :ref:`CDOTA_Item.GetPurchaser`
  * :ref:`CDOTA_Item.GetPurchaseTime`
  * :ref:`CDOTA_Item.GetShareability`
  * :ref:`CDOTA_Item.IsPermanent`
  * :ref:`CDOTA_Item.LaunchLoot`
  * :ref:`CDOTA_Item.SetCurrentCharges`
  * :ref:`CDOTA_Item.SetPurchaser`
  * :ref:`CDOTA_Item.SetPurchaseTime`
  * :ref:`CDOTA_Item.SetStacksWithOtherOwners`
  * :ref:`CDOTA_Item.StacksWithOtherOwners`
  * :ref:`CDOTA_Item.Think`
CDOTA_Item_Physical
############
extends CBaseAnimating
No Description Set
  * :ref:`CDOTA_Item_Physical.GetContainedItem`
  * :ref:`CDOTA_Item_Physical.GetCreationTime`
  * :ref:`CDOTA_Item_Physical.SetContainedItem`
CDOTA_Item_DataDriven
############
extends CDOTA_Item

  * :ref:`CDOTA_Item_DataDriven.ApplyDataDrivenModifier`
CDOTA_Unit_Nian
############
extends CDOTA_BaseNPC_Creature
No Description Set
  * :ref:`CDOTA_Unit_Nian.GetHorn`
  * :ref:`CDOTA_Unit_Nian.GetTail`
  * :ref:`CDOTA_Unit_Nian.IsHornAlive`
  * :ref:`CDOTA_Unit_Nian.IsTailAlive`
CBasePlayer
############
No Description Set
  * :ref:`CBasePlayer.IsNoclipping`
CDOTAPlayer
############
extends CBaseAnimating
No Description Set
  * :ref:`CDOTAPlayer.GetAssignedHero`
  * :ref:`CDOTAPlayer.GetControlledRPGUnit`
  * :ref:`CDOTAPlayer.GetPlayerID`
  * :ref:`CDOTAPlayer.MakeRandomHeroSelection`
  * :ref:`CDOTAPlayer.SetKillCamUnit`
  * :ref:`CDOTAPlayer.SetMusicStatus`
CDOTA_PlayerResource
############
extends CBaseEntity
No Description Set
  * :ref:`CDOTA_PlayerResource.AddAegisPickup`
  * :ref:`CDOTA_PlayerResource.AddClaimedFarm`
  * :ref:`CDOTA_PlayerResource.AddGoldSpentOnSupport`
  * :ref:`CDOTA_PlayerResource.AddRunePickup`
  * :ref:`CDOTA_PlayerResource.AreUnitsSharedWithPlayerID`
  * :ref:`CDOTA_PlayerResource.ClearKillsMatrix`
  * :ref:`CDOTA_PlayerResource.ClearLastHitMultikill`
  * :ref:`CDOTA_PlayerResource.ClearLastHitStreak`
  * :ref:`CDOTA_PlayerResource.ClearRawPlayerDamageMatrix`
  * :ref:`CDOTA_PlayerResource.ClearStreak`
  * :ref:`CDOTA_PlayerResource.GetAegisPickups`
  * :ref:`CDOTA_PlayerResource.GetAssists`
  * :ref:`CDOTA_PlayerResource.GetBroadcasterChannel`
  * :ref:`CDOTA_PlayerResource.GetBroadcasterChannelSlot`
  * :ref:`CDOTA_PlayerResource.GetClaimedDenies`
  * :ref:`CDOTA_PlayerResource.GetClaimedFarm`
  * :ref:`CDOTA_PlayerResource.GetClaimedMisses`
  * :ref:`CDOTA_PlayerResource.GetConnectionState`
  * :ref:`CDOTA_PlayerResource.GetCreepDamageTaken`
  * :ref:`CDOTA_PlayerResource.GetCustomBuybackCooldown`
  * :ref:`CDOTA_PlayerResource.GetCustomBuybackCost`
  * :ref:`CDOTA_PlayerResource.GetDamageDoneToHero`
  * :ref:`CDOTA_PlayerResource.GetDeaths`
  * :ref:`CDOTA_PlayerResource.GetDenies`
  * :ref:`CDOTA_PlayerResource.GetEventPointsForPlayerID`
  * :ref:`CDOTA_PlayerResource.GetEventPremiumPointsGranted`
  * :ref:`CDOTA_PlayerResource.GetEventRankGranted`
  * :ref:`CDOTA_PlayerResource.GetGold`
  * :ref:`CDOTA_PlayerResource.GetGoldBagsCollected`
  * :ref:`CDOTA_PlayerResource.GetGoldLostToDeath`
  * :ref:`CDOTA_PlayerResource.GetGoldPerMin`
  * :ref:`CDOTA_PlayerResource.GetGoldSpentOnBuybacks`
  * :ref:`CDOTA_PlayerResource.GetGoldSpentOnConsumables`
  * :ref:`CDOTA_PlayerResource.GetGoldSpentOnItems`
  * :ref:`CDOTA_PlayerResource.GetGoldSpentOnSupport`
  * :ref:`CDOTA_PlayerResource.GetHealing`
  * :ref:`CDOTA_PlayerResource.GetHeroDamageTaken`
  * :ref:`CDOTA_PlayerResource.GetKills`
  * :ref:`CDOTA_PlayerResource.GetKillsDoneToHero`
  * :ref:`CDOTA_PlayerResource.GetLastHitMultikill`
  * :ref:`CDOTA_PlayerResource.GetLastHits`
  * :ref:`CDOTA_PlayerResource.GetLastHitStreak`
  * :ref:`CDOTA_PlayerResource.GetLevel`
  * :ref:`CDOTA_PlayerResource.GetMisses`
  * :ref:`CDOTA_PlayerResource.GetNearbyCreepDeaths`
  * :ref:`CDOTA_PlayerResource.GetNthCourierForTeam`
  * :ref:`CDOTA_PlayerResource.GetNthPlayerIDOnTeam`
  * :ref:`CDOTA_PlayerResource.GetNumConsumablesPurchased`
  * :ref:`CDOTA_PlayerResource.GetNumCouriersForTeam`
  * :ref:`CDOTA_PlayerResource.GetNumItemsPurchased`
  * :ref:`CDOTA_PlayerResource.GetPlayer`
  * :ref:`CDOTA_PlayerResource.GetPlayerLoadedCompletely`
  * :ref:`CDOTA_PlayerResource.GetPlayerName`
  * :ref:`CDOTA_PlayerResource.GetPlayerReservedState`
  * :ref:`CDOTA_PlayerResource.GetRawPlayerDamage`
  * :ref:`CDOTA_PlayerResource.GetReliableGold`
  * :ref:`CDOTA_PlayerResource.GetRespawnSeconds`
  * :ref:`CDOTA_PlayerResource.GetRoshanKills`
  * :ref:`CDOTA_PlayerResource.GetRunePickups`
  * :ref:`CDOTA_PlayerResource.GetSelectedHeroEntity`
  * :ref:`CDOTA_PlayerResource.GetSelectedHeroID`
  * :ref:`CDOTA_PlayerResource.GetSelectedHeroName`
  * :ref:`CDOTA_PlayerResource.GetSteamAccountID`
  * :ref:`CDOTA_PlayerResource.GetStreak`
  * :ref:`CDOTA_PlayerResource.GetStuns`
  * :ref:`CDOTA_PlayerResource.GetTeam`
  * :ref:`CDOTA_PlayerResource.GetTeamKills`
  * :ref:`CDOTA_PlayerResource.GetTimeOfLastConsumablePurchase`
  * :ref:`CDOTA_PlayerResource.GetTimeOfLastDeath`
  * :ref:`CDOTA_PlayerResource.GetTimeOfLastItemPurchase`
  * :ref:`CDOTA_PlayerResource.GetTotalEarnedGold`
  * :ref:`CDOTA_PlayerResource.GetTotalEarnedXP`
  * :ref:`CDOTA_PlayerResource.GetTotalGoldSpent`
  * :ref:`CDOTA_PlayerResource.GetTowerDamageTaken`
  * :ref:`CDOTA_PlayerResource.GetTowerKills`
  * :ref:`CDOTA_PlayerResource.GetUnitShareMaskForPlayer`
  * :ref:`CDOTA_PlayerResource.GetUnreliableGold`
  * :ref:`CDOTA_PlayerResource.GetXPPerMin`
  * :ref:`CDOTA_PlayerResource.HasRandomed`
  * :ref:`CDOTA_PlayerResource.HasRepicked`
  * :ref:`CDOTA_PlayerResource.HasSelectedHero`
  * :ref:`CDOTA_PlayerResource.HaveAllPlayersJoined`
  * :ref:`CDOTA_PlayerResource.HeroLevelUp`
  * :ref:`CDOTA_PlayerResource.IncrementAssists`
  * :ref:`CDOTA_PlayerResource.IncrementClaimedDenies`
  * :ref:`CDOTA_PlayerResource.IncrementClaimedMisses`
  * :ref:`CDOTA_PlayerResource.IncrementDeaths`
  * :ref:`CDOTA_PlayerResource.IncrementDenies`
  * :ref:`CDOTA_PlayerResource.IncrementGoldBagsCollected`
  * :ref:`CDOTA_PlayerResource.IncrementKills`
  * :ref:`CDOTA_PlayerResource.IncrementLastHitMultikill`
  * :ref:`CDOTA_PlayerResource.IncrementLastHits`
  * :ref:`CDOTA_PlayerResource.IncrementLastHitStreak`
  * :ref:`CDOTA_PlayerResource.IncrementMisses`
  * :ref:`CDOTA_PlayerResource.IncrementNearbyCreepDeaths`
  * :ref:`CDOTA_PlayerResource.IncrementStreak`
  * :ref:`CDOTA_PlayerResource.IncrementTotalEarnedXP`
  * :ref:`CDOTA_PlayerResource.IsBroadcaster`
  * :ref:`CDOTA_PlayerResource.IsDisableHelpSetForPlayerID`
  * :ref:`CDOTA_PlayerResource.IsFakeClient`
  * :ref:`CDOTA_PlayerResource.IsHeroSelected`
  * :ref:`CDOTA_PlayerResource.IsHeroSharedWithPlayerID`
  * :ref:`CDOTA_PlayerResource.IsValidPlayer`
  * :ref:`CDOTA_PlayerResource.IsValidPlayerID`
  * :ref:`CDOTA_PlayerResource.IsValidTeamPlayer`
  * :ref:`CDOTA_PlayerResource.IsValidTeamPlayerID`
  * :ref:`CDOTA_PlayerResource.ModifyGold`
  * :ref:`CDOTA_PlayerResource.ReplaceHeroWith`
  * :ref:`CDOTA_PlayerResource.ResetBuybackCostTime`
  * :ref:`CDOTA_PlayerResource.ResetTotalEarnedGold`
  * :ref:`CDOTA_PlayerResource.SetBuybackCooldownTime`
  * :ref:`CDOTA_PlayerResource.SetBuybackGoldLimitTime`
  * :ref:`CDOTA_PlayerResource.SetCameraTarget`
  * :ref:`CDOTA_PlayerResource.SetCustomBuybackCooldown`
  * :ref:`CDOTA_PlayerResource.SetCustomBuybackCost`
  * :ref:`CDOTA_PlayerResource.SetGold`
  * :ref:`CDOTA_PlayerResource.SetHasRandomed`
  * :ref:`CDOTA_PlayerResource.SetHasRepicked`
  * :ref:`CDOTA_PlayerResource.SetLastBuybackTime`
  * :ref:`CDOTA_PlayerResource.SetPlayerReservedState`
  * :ref:`CDOTA_PlayerResource.SetUnitShareMaskForPlayer`
  * :ref:`CDOTA_PlayerResource.SpendGold`
  * :ref:`CDOTA_PlayerResource.UpdateTeamSlot`
  * :ref:`CDOTA_PlayerResource.WhoSelectedHero`
CDOTA_BaseNPC
############
extends CBaseFlex

  * :ref:`CDOTA_BaseNPC.AddAbility`
  * :ref:`CDOTA_BaseNPC.AddItem`
  * :ref:`CDOTA_BaseNPC.AddNewModifier`
  * :ref:`CDOTA_BaseNPC.AddNoDraw`
  * :ref:`CDOTA_BaseNPC.AlertNearbyUnits`
  * :ref:`CDOTA_BaseNPC.AngerNearbyUnits`
  * :ref:`CDOTA_BaseNPC.AttackNoEarlierThan`
  * :ref:`CDOTA_BaseNPC.AttackReady`
  * :ref:`CDOTA_BaseNPC.BoundingRadius2D`
  * :ref:`CDOTA_BaseNPC.CastAbilityImmediately`
  * :ref:`CDOTA_BaseNPC.CastAbilityNoTarget`
  * :ref:`CDOTA_BaseNPC.CastAbilityOnPosition`
  * :ref:`CDOTA_BaseNPC.CastAbilityOnTarget`
  * :ref:`CDOTA_BaseNPC.CastAbilityToggle`
  * :ref:`CDOTA_BaseNPC.DisassembleItem`
  * :ref:`CDOTA_BaseNPC.DropItemAtPosition`
  * :ref:`CDOTA_BaseNPC.DropItemAtPositionImmediate`
  * :ref:`CDOTA_BaseNPC.EjectItemFromStash`
  * :ref:`CDOTA_BaseNPC.FindAbilityByName`
  * :ref:`CDOTA_BaseNPC.ForceKill`
  * :ref:`CDOTA_BaseNPC.GetAbilityByIndex`
  * :ref:`CDOTA_BaseNPC.GetAbilityCount`
  * :ref:`CDOTA_BaseNPC.GetAcquisitionRange`
  * :ref:`CDOTA_BaseNPC.GetAdditionalBattleMusicWeight`
  * :ref:`CDOTA_BaseNPC.GetAttackAnimationPoint`
  * :ref:`CDOTA_BaseNPC.GetAttackDamage`
  * :ref:`CDOTA_BaseNPC.GetAttackRange`
  * :ref:`CDOTA_BaseNPC.GetAttackRangeBuffer`
  * :ref:`CDOTA_BaseNPC.GetAttackSpeed`
  * :ref:`CDOTA_BaseNPC.GetAttacksPerSecond`
  * :ref:`CDOTA_BaseNPC.GetAttackTarget`
  * :ref:`CDOTA_BaseNPC.GetAverageTrueAttackDamage`
  * :ref:`CDOTA_BaseNPC.GetBaseAttackRange`
  * :ref:`CDOTA_BaseNPC.GetBaseAttackTime`
  * :ref:`CDOTA_BaseNPC.GetBaseDamageMax`
  * :ref:`CDOTA_BaseNPC.GetBaseDamageMin`
  * :ref:`CDOTA_BaseNPC.GetBaseDayTimeVisionRange`
  * :ref:`CDOTA_BaseNPC.GetBaseHealthRegen`
  * :ref:`CDOTA_BaseNPC.GetBaseMagicalResistanceValue`
  * :ref:`CDOTA_BaseNPC.GetBaseMaxHealth`
  * :ref:`CDOTA_BaseNPC.GetBaseMoveSpeed`
  * :ref:`CDOTA_BaseNPC.GetBaseNightTimeVisionRange`
  * :ref:`CDOTA_BaseNPC.GetCastPoint`
  * :ref:`CDOTA_BaseNPC.GetCollisionPadding`
  * :ref:`CDOTA_BaseNPC.GetConstantBasedManaRegen`
  * :ref:`CDOTA_BaseNPC.GetCreationTime`
  * :ref:`CDOTA_BaseNPC.GetCurrentActiveAbility`
  * :ref:`CDOTA_BaseNPC.GetCurrentVisionRange`
  * :ref:`CDOTA_BaseNPC.GetCursorCastTarget`
  * :ref:`CDOTA_BaseNPC.GetCursorPosition`
  * :ref:`CDOTA_BaseNPC.GetCursorTargetingNothing`
  * :ref:`CDOTA_BaseNPC.GetDayTimeVisionRange`
  * :ref:`CDOTA_BaseNPC.GetDeathXP`
  * :ref:`CDOTA_BaseNPC.GetForceAttackTarget`
  * :ref:`CDOTA_BaseNPC.GetGoldBounty`
  * :ref:`CDOTA_BaseNPC.GetHasteFactor`
  * :ref:`CDOTA_BaseNPC.GetHealth`
  * :ref:`CDOTA_BaseNPC.GetHealthDeficit`
  * :ref:`CDOTA_BaseNPC.GetHealthPercent`
  * :ref:`CDOTA_BaseNPC.GetHealthRegen`
  * :ref:`CDOTA_BaseNPC.GetHullRadius`
  * :ref:`CDOTA_BaseNPC.GetIdealSpeed`
  * :ref:`CDOTA_BaseNPC.GetIncreasedAttackSpeed`
  * :ref:`CDOTA_BaseNPC.GetInitialGoalEntity`
  * :ref:`CDOTA_BaseNPC.GetItemInSlot`
  * :ref:`CDOTA_BaseNPC.GetLastIdleChangeTime`
  * :ref:`CDOTA_BaseNPC.GetLevel`
  * :ref:`CDOTA_BaseNPC.GetMagicalArmorValue`
  * :ref:`CDOTA_BaseNPC.GetMainControllingPlayer`
  * :ref:`CDOTA_BaseNPC.GetMana`
  * :ref:`CDOTA_BaseNPC.GetManaPercent`
  * :ref:`CDOTA_BaseNPC.GetManaRegen`
  * :ref:`CDOTA_BaseNPC.GetMaxHealth`
  * :ref:`CDOTA_BaseNPC.GetMaxMana`
  * :ref:`CDOTA_BaseNPC.GetModelRadius`
  * :ref:`CDOTA_BaseNPC.GetModifierCount`
  * :ref:`CDOTA_BaseNPC.GetModifierNameByIndex`
  * :ref:`CDOTA_BaseNPC.GetMoveSpeedModifier`
  * :ref:`CDOTA_BaseNPC.GetMustReachEachGoalEntity`
  * :ref:`CDOTA_BaseNPC.GetNightTimeVisionRange`
  * :ref:`CDOTA_BaseNPC.GetOpposingTeamNumber`
  * :ref:`CDOTA_BaseNPC.GetPaddedCollisionRadius`
  * :ref:`CDOTA_BaseNPC.GetPercentageBasedManaRegen`
  * :ref:`CDOTA_BaseNPC.GetPhysicalArmorBaseValue`
  * :ref:`CDOTA_BaseNPC.GetPhysicalArmorValue`
  * :ref:`CDOTA_BaseNPC.GetPlayerOwner`
  * :ref:`CDOTA_BaseNPC.GetPlayerOwnerID`
  * :ref:`CDOTA_BaseNPC.GetProjectileSpeed`
  * :ref:`CDOTA_BaseNPC.GetRangeToUnit`
  * :ref:`CDOTA_BaseNPC.GetSecondsPerAttack`
  * :ref:`CDOTA_BaseNPC.GetStatsBasedManaRegen`
  * :ref:`CDOTA_BaseNPC.GetTeamNumber`
  * :ref:`CDOTA_BaseNPC.GetTotalPurchasedUpgradeGoldCost`
  * :ref:`CDOTA_BaseNPC.GetUnitLabel`
  * :ref:`CDOTA_BaseNPC.GetUnitName`
  * :ref:`CDOTA_BaseNPC.GiveMana`
  * :ref:`CDOTA_BaseNPC.HasAbility`
  * :ref:`CDOTA_BaseNPC.HasAttackCapability`
  * :ref:`CDOTA_BaseNPC.HasFlyingVision`
  * :ref:`CDOTA_BaseNPC.HasFlyMovementCapability`
  * :ref:`CDOTA_BaseNPC.HasGroundMovementCapability`
  * :ref:`CDOTA_BaseNPC.HasInventory`
  * :ref:`CDOTA_BaseNPC.HasItemInInventory`
  * :ref:`CDOTA_BaseNPC.HasModifier`
  * :ref:`CDOTA_BaseNPC.HasMovementCapability`
  * :ref:`CDOTA_BaseNPC.HasScepter`
  * :ref:`CDOTA_BaseNPC.Heal`
  * :ref:`CDOTA_BaseNPC.Hold`
  * :ref:`CDOTA_BaseNPC.Interrupt`
  * :ref:`CDOTA_BaseNPC.InterruptChannel`
  * :ref:`CDOTA_BaseNPC.InterruptMotionControllers`
  * :ref:`CDOTA_BaseNPC.IsAlive`
  * :ref:`CDOTA_BaseNPC.IsAncient`
  * :ref:`CDOTA_BaseNPC.IsAttackImmune`
  * :ref:`CDOTA_BaseNPC.IsAttacking`
  * :ref:`CDOTA_BaseNPC.IsAttackingEntity`
  * :ref:`CDOTA_BaseNPC.IsBlind`
  * :ref:`CDOTA_BaseNPC.IsBlockDisabled`
  * :ref:`CDOTA_BaseNPC.IsCommandRestricted`
  * :ref:`CDOTA_BaseNPC.IsControllableByAnyPlayer`
  * :ref:`CDOTA_BaseNPC.IsCreature`
  * :ref:`CDOTA_BaseNPC.IsDeniable`
  * :ref:`CDOTA_BaseNPC.IsDisarmed`
  * :ref:`CDOTA_BaseNPC.IsDominated`
  * :ref:`CDOTA_BaseNPC.IsEvadeDisabled`
  * :ref:`CDOTA_BaseNPC.IsFrozen`
  * :ref:`CDOTA_BaseNPC.IsHardDisarmed`
  * :ref:`CDOTA_BaseNPC.IsHero`
  * :ref:`CDOTA_BaseNPC.IsHexed`
  * :ref:`CDOTA_BaseNPC.IsIdle`
  * :ref:`CDOTA_BaseNPC.IsIllusion`
  * :ref:`CDOTA_BaseNPC.IsInvisible`
  * :ref:`CDOTA_BaseNPC.IsInvulnerable`
  * :ref:`CDOTA_BaseNPC.IsLowAttackPriority`
  * :ref:`CDOTA_BaseNPC.IsMagicImmune`
  * :ref:`CDOTA_BaseNPC.IsMechanical`
  * :ref:`CDOTA_BaseNPC.IsMovementImpaired`
  * :ref:`CDOTA_BaseNPC.IsMuted`
  * :ref:`CDOTA_BaseNPC.IsNeutralUnitType`
  * :ref:`CDOTA_BaseNPC.IsNightmared`
  * :ref:`CDOTA_BaseNPC.IsOpposingTeam`
  * :ref:`CDOTA_BaseNPC.IsOutOfGame`
  * :ref:`CDOTA_BaseNPC.IsOwnedByAnyPlayer`
  * :ref:`CDOTA_BaseNPC.IsPhantom`
  * :ref:`CDOTA_BaseNPC.IsPhantomBlocker`
  * :ref:`CDOTA_BaseNPC.IsPhased`
  * :ref:`CDOTA_BaseNPC.IsPositionInRange`
  * :ref:`CDOTA_BaseNPC.IsRangedAttacker`
  * :ref:`CDOTA_BaseNPC.IsRealHero`
  * :ref:`CDOTA_BaseNPC.IsRooted`
  * :ref:`CDOTA_BaseNPC.IsSilenced`
  * :ref:`CDOTA_BaseNPC.IsSoftDisarmed`
  * :ref:`CDOTA_BaseNPC.IsSpeciallyDeniable`
  * :ref:`CDOTA_BaseNPC.IsStunned`
  * :ref:`CDOTA_BaseNPC.IsSummoned`
  * :ref:`CDOTA_BaseNPC.IsTower`
  * :ref:`CDOTA_BaseNPC.IsUnableToMiss`
  * :ref:`CDOTA_BaseNPC.IsUnselectable`
  * :ref:`CDOTA_BaseNPC.Kill`
  * :ref:`CDOTA_BaseNPC.MakeIllusion`
  * :ref:`CDOTA_BaseNPC.MakePhantomBlocker`
  * :ref:`CDOTA_BaseNPC.MakeVisibleDueToAttack`
  * :ref:`CDOTA_BaseNPC.MakeVisibleToTeam`
  * :ref:`CDOTA_BaseNPC.ModifyHealth`
  * :ref:`CDOTA_BaseNPC.MoveToNPC`
  * :ref:`CDOTA_BaseNPC.MoveToNPCToGiveItem`
  * :ref:`CDOTA_BaseNPC.MoveToPosition`
  * :ref:`CDOTA_BaseNPC.MoveToPositionAggressive`
  * :ref:`CDOTA_BaseNPC.MoveToTargetToAttack`
  * :ref:`CDOTA_BaseNPC.NoHealthBar`
  * :ref:`CDOTA_BaseNPC.NoTeamMoveTo`
  * :ref:`CDOTA_BaseNPC.NoTeamSelect`
  * :ref:`CDOTA_BaseNPC.NotOnMinimap`
  * :ref:`CDOTA_BaseNPC.NotOnMinimapForEnemies`
  * :ref:`CDOTA_BaseNPC.NoUnitCollision`
  * :ref:`CDOTA_BaseNPC.PassivesDisabled`
  * :ref:`CDOTA_BaseNPC.PerformAttack`
  * :ref:`CDOTA_BaseNPC.PickupDroppedItem`
  * :ref:`CDOTA_BaseNPC.PickupRune`
  * :ref:`CDOTA_BaseNPC.ProvidesVision`
  * :ref:`CDOTA_BaseNPC.ReduceMana`
  * :ref:`CDOTA_BaseNPC.RemoveAbility`
  * :ref:`CDOTA_BaseNPC.RemoveItem`
  * :ref:`CDOTA_BaseNPC.RemoveModifierByName`
  * :ref:`CDOTA_BaseNPC.RemoveModifierByNameAndCaster`
  * :ref:`CDOTA_BaseNPC.RemoveNoDraw`
  * :ref:`CDOTA_BaseNPC.RespawnUnit`
  * :ref:`CDOTA_BaseNPC.SellItem`
  * :ref:`CDOTA_BaseNPC.SetAdditionalBattleMusicWeight`
  * :ref:`CDOTA_BaseNPC.SetAttackCapability`
  * :ref:`CDOTA_BaseNPC.SetAttacking`
  * :ref:`CDOTA_BaseNPC.SetBaseAttackTime`
  * :ref:`CDOTA_BaseNPC.SetBaseDamageMax`
  * :ref:`CDOTA_BaseNPC.SetBaseDamageMin`
  * :ref:`CDOTA_BaseNPC.SetBaseHealthRegen`
  * :ref:`CDOTA_BaseNPC.SetBaseMagicalResistanceValue`
  * :ref:`CDOTA_BaseNPC.SetBaseManaRegen`
  * :ref:`CDOTA_BaseNPC.SetBaseMaxHealth`
  * :ref:`CDOTA_BaseNPC.SetBaseMoveSpeed`
  * :ref:`CDOTA_BaseNPC.SetControllableByPlayer`
  * :ref:`CDOTA_BaseNPC.SetCursorCastTarget`
  * :ref:`CDOTA_BaseNPC.SetCursorPosition`
  * :ref:`CDOTA_BaseNPC.SetCursorTargetingNothing`
  * :ref:`CDOTA_BaseNPC.SetDayTimeVisionRange`
  * :ref:`CDOTA_BaseNPC.SetDeathXP`
  * :ref:`CDOTA_BaseNPC.SetForceAttackTarget`
  * :ref:`CDOTA_BaseNPC.SetHasInventory`
  * :ref:`CDOTA_BaseNPC.SetHullRadius`
  * :ref:`CDOTA_BaseNPC.SetIdleAcquire`
  * :ref:`CDOTA_BaseNPC.SetInitialGoalEntity`
  * :ref:`CDOTA_BaseNPC.SetMana`
  * :ref:`CDOTA_BaseNPC.SetMaximumGoldBounty`
  * :ref:`CDOTA_BaseNPC.SetMinimumGoldBounty`
  * :ref:`CDOTA_BaseNPC.SetMoveCapability`
  * :ref:`CDOTA_BaseNPC.SetMustReachEachGoalEntity`
  * :ref:`CDOTA_BaseNPC.SetNeverMoveToClearSpace`
  * :ref:`CDOTA_BaseNPC.SetNightTimeVisionRange`
  * :ref:`CDOTA_BaseNPC.SetOriginalModel`
  * :ref:`CDOTA_BaseNPC.SetPhysicalArmorBaseValue`
  * :ref:`CDOTA_BaseNPC.SetRangedProjectileName`
  * :ref:`CDOTA_BaseNPC.SetStolenScepter`
  * :ref:`CDOTA_BaseNPC.SetUnitName`
  * :ref:`CDOTA_BaseNPC.ShouldIdleAcquire`
  * :ref:`CDOTA_BaseNPC.SpendMana`
  * :ref:`CDOTA_BaseNPC.Stop`
  * :ref:`CDOTA_BaseNPC.SwapAbilities`
  * :ref:`CDOTA_BaseNPC.TimeUntilNextAttack`
  * :ref:`CDOTA_BaseNPC.TriggerModifierDodge`
  * :ref:`CDOTA_BaseNPC.TriggerSpellAbsorb`
  * :ref:`CDOTA_BaseNPC.UnitCanRespawn`
CDOTA_BaseNPC_Hero
############
extends CDOTA_BaseNPC

  * :ref:`CDOTA_BaseNPC_Hero.AddExperience`
  * :ref:`CDOTA_BaseNPC_Hero.Buyback`
  * :ref:`CDOTA_BaseNPC_Hero.CalculateStatBonus`
  * :ref:`CDOTA_BaseNPC_Hero.CanEarnGold`
  * :ref:`CDOTA_BaseNPC_Hero.ClearLastHitMultikill`
  * :ref:`CDOTA_BaseNPC_Hero.ClearLastHitStreak`
  * :ref:`CDOTA_BaseNPC_Hero.ClearStreak`
  * :ref:`CDOTA_BaseNPC_Hero.GetAbilityPoints`
  * :ref:`CDOTA_BaseNPC_Hero.GetAgility`
  * :ref:`CDOTA_BaseNPC_Hero.GetAgilityGain`
  * :ref:`CDOTA_BaseNPC_Hero.GetAssists`
  * :ref:`CDOTA_BaseNPC_Hero.GetAttacker`
  * :ref:`CDOTA_BaseNPC_Hero.GetBaseAgility`
  * :ref:`CDOTA_BaseNPC_Hero.GetBaseDamageMax`
  * :ref:`CDOTA_BaseNPC_Hero.GetBaseDamageMin`
  * :ref:`CDOTA_BaseNPC_Hero.GetBaseIntellect`
  * :ref:`CDOTA_BaseNPC_Hero.GetBaseStrength`
  * :ref:`CDOTA_BaseNPC_Hero.GetBonusDamageFromPrimaryStat`
  * :ref:`CDOTA_BaseNPC_Hero.GetBuybackCooldownTime`
  * :ref:`CDOTA_BaseNPC_Hero.GetBuybackCost`
  * :ref:`CDOTA_BaseNPC_Hero.GetBuybackGoldLimitTime`
  * :ref:`CDOTA_BaseNPC_Hero.GetCurrentXP`
  * :ref:`CDOTA_BaseNPC_Hero.GetDeathGoldCost`
  * :ref:`CDOTA_BaseNPC_Hero.GetDeaths`
  * :ref:`CDOTA_BaseNPC_Hero.GetDenies`
  * :ref:`CDOTA_BaseNPC_Hero.GetGold`
  * :ref:`CDOTA_BaseNPC_Hero.GetGoldBounty`
  * :ref:`CDOTA_BaseNPC_Hero.GetHealthRegen`
  * :ref:`CDOTA_BaseNPC_Hero.GetIncreasedAttackSpeed`
  * :ref:`CDOTA_BaseNPC_Hero.GetIntellect`
  * :ref:`CDOTA_BaseNPC_Hero.GetIntellectGain`
  * :ref:`CDOTA_BaseNPC_Hero.GetKills`
  * :ref:`CDOTA_BaseNPC_Hero.GetLastHits`
  * :ref:`CDOTA_BaseNPC_Hero.GetManaRegen`
  * :ref:`CDOTA_BaseNPC_Hero.GetMostRecentDamageTime`
  * :ref:`CDOTA_BaseNPC_Hero.GetMultipleKillCount`
  * :ref:`CDOTA_BaseNPC_Hero.GetNumAttackers`
  * :ref:`CDOTA_BaseNPC_Hero.GetPhysicalArmorValue`
  * :ref:`CDOTA_BaseNPC_Hero.GetPlayerID`
  * :ref:`CDOTA_BaseNPC_Hero.GetPrimaryAttribute`
  * :ref:`CDOTA_BaseNPC_Hero.GetPrimaryStatValue`
  * :ref:`CDOTA_BaseNPC_Hero.GetRespawnTime`
  * :ref:`CDOTA_BaseNPC_Hero.GetStatsBasedManaRegen`
  * :ref:`CDOTA_BaseNPC_Hero.GetStreak`
  * :ref:`CDOTA_BaseNPC_Hero.GetStrength`
  * :ref:`CDOTA_BaseNPC_Hero.GetStrengthGain`
  * :ref:`CDOTA_BaseNPC_Hero.GetTimeUntilRespawn`
  * :ref:`CDOTA_BaseNPC_Hero.HasAnyAvailableInventorySpace`
  * :ref:`CDOTA_BaseNPC_Hero.HasFlyingVision`
  * :ref:`CDOTA_BaseNPC_Hero.HasOwnerAbandoned`
  * :ref:`CDOTA_BaseNPC_Hero.HasRoomForItem`
  * :ref:`CDOTA_BaseNPC_Hero.HeroLevelUp`
  * :ref:`CDOTA_BaseNPC_Hero.IncrementAssists`
  * :ref:`CDOTA_BaseNPC_Hero.IncrementDeaths`
  * :ref:`CDOTA_BaseNPC_Hero.IncrementDenies`
  * :ref:`CDOTA_BaseNPC_Hero.IncrementKills`
  * :ref:`CDOTA_BaseNPC_Hero.IncrementLastHitMultikill`
  * :ref:`CDOTA_BaseNPC_Hero.IncrementLastHits`
  * :ref:`CDOTA_BaseNPC_Hero.IncrementLastHitStreak`
  * :ref:`CDOTA_BaseNPC_Hero.IncrementNearbyCreepDeaths`
  * :ref:`CDOTA_BaseNPC_Hero.IncrementStreak`
  * :ref:`CDOTA_BaseNPC_Hero.IsBuybackDisabledByReapersScythe`
  * :ref:`CDOTA_BaseNPC_Hero.IsReincarnating`
  * :ref:`CDOTA_BaseNPC_Hero.KilledHero`
  * :ref:`CDOTA_BaseNPC_Hero.ModifyAgility`
  * :ref:`CDOTA_BaseNPC_Hero.ModifyGold`
  * :ref:`CDOTA_BaseNPC_Hero.ModifyIntellect`
  * :ref:`CDOTA_BaseNPC_Hero.ModifyStrength`
  * :ref:`CDOTA_BaseNPC_Hero.PerformTaunt`
  * :ref:`CDOTA_BaseNPC_Hero.RecordLastHit`
  * :ref:`CDOTA_BaseNPC_Hero.RespawnHero`
  * :ref:`CDOTA_BaseNPC_Hero.SetAbilityPoints`
  * :ref:`CDOTA_BaseNPC_Hero.SetBaseAgility`
  * :ref:`CDOTA_BaseNPC_Hero.SetBaseIntellect`
  * :ref:`CDOTA_BaseNPC_Hero.SetBaseStrength`
  * :ref:`CDOTA_BaseNPC_Hero.SetBuybackCooldownTime`
  * :ref:`CDOTA_BaseNPC_Hero.SetBuyBackDisabledByReapersScythe`
  * :ref:`CDOTA_BaseNPC_Hero.SetBuybackGoldLimitTime`
  * :ref:`CDOTA_BaseNPC_Hero.SetCustomDeathXP`
  * :ref:`CDOTA_BaseNPC_Hero.SetGold`
  * :ref:`CDOTA_BaseNPC_Hero.SetPlayerID`
  * :ref:`CDOTA_BaseNPC_Hero.SetRespawnPosition`
  * :ref:`CDOTA_BaseNPC_Hero.SetTimeUntilRespawn`
  * :ref:`CDOTA_BaseNPC_Hero.ShouldDoFlyHeightVisual`
  * :ref:`CDOTA_BaseNPC_Hero.SpendGold`
  * :ref:`CDOTA_BaseNPC_Hero.UnitCanRespawn`
  * :ref:`CDOTA_BaseNPC_Hero.UpgradeAbility`
  * :ref:`CDOTA_BaseNPC_Hero.WillReincarnate`
CDOTA_BaseNPC_Creature
############
extends CDOTA_BaseNPC
No Description Set
  * :ref:`CDOTA_BaseNPC_Creature.AddItemDrop`
  * :ref:`CDOTA_BaseNPC_Creature.CreatureLevelUp`
  * :ref:`CDOTA_BaseNPC_Creature.IsChampion`
  * :ref:`CDOTA_BaseNPC_Creature.SetArmorGain`
  * :ref:`CDOTA_BaseNPC_Creature.SetAttackTimeGain`
  * :ref:`CDOTA_BaseNPC_Creature.SetBountyGain`
  * :ref:`CDOTA_BaseNPC_Creature.SetChampion`
  * :ref:`CDOTA_BaseNPC_Creature.SetDamageGain`
  * :ref:`CDOTA_BaseNPC_Creature.SetDisableResistanceGain`
  * :ref:`CDOTA_BaseNPC_Creature.SetHPGain`
  * :ref:`CDOTA_BaseNPC_Creature.SetHPRegenGain`
  * :ref:`CDOTA_BaseNPC_Creature.SetMagicResistanceGain`
  * :ref:`CDOTA_BaseNPC_Creature.SetManaGain`
  * :ref:`CDOTA_BaseNPC_Creature.SetManaRegenGain`
  * :ref:`CDOTA_BaseNPC_Creature.SetMoveSpeedGain`
  * :ref:`CDOTA_BaseNPC_Creature.SetXPGain`
CDOTA_BaseNPC_Building
############
extends CDOTA_BaseNPC
No Description Set
  * :ref:`CDOTA_BaseNPC_Building.GetInvulnCount`
  * :ref:`CDOTA_BaseNPC_Building.SetInvulnCount`
CRPG_Unit
############
No Description Set
  * :ref:`CRPG_Unit.ActionState`
  * :ref:`CRPG_Unit.ClearMovementTarget`
  * :ref:`CRPG_Unit.FindSensedEnemies`
  * :ref:`CRPG_Unit.GetMaxSpeed`
  * :ref:`CRPG_Unit.GetMaxStamina`
  * :ref:`CRPG_Unit.GetMovementTargetEntity`
  * :ref:`CRPG_Unit.GetSensingSphereRange`
  * :ref:`CRPG_Unit.GetSightConeAngle`
  * :ref:`CRPG_Unit.GetSightConeRange`
  * :ref:`CRPG_Unit.GetStamina`
  * :ref:`CRPG_Unit.GetTurnRate`
  * :ref:`CRPG_Unit.GetUnitName`
  * :ref:`CRPG_Unit.GrantItem`
  * :ref:`CRPG_Unit.IsBlocking`
  * :ref:`CRPG_Unit.IsFacing`
  * :ref:`CRPG_Unit.SetBlocking`
  * :ref:`CRPG_Unit.SetMaxSpeed`
  * :ref:`CRPG_Unit.SetMovementTargetEntity`
  * :ref:`CRPG_Unit.SetMovementTargetPosition`
  * :ref:`CRPG_Unit.SetSensingSphereRange`
  * :ref:`CRPG_Unit.SetSightConeAngle`
  * :ref:`CRPG_Unit.SetSightConeRange`
  * :ref:`CRPG_Unit.SetTurnRate`
CDOTABaseGameMode
############
extends CBaseEntity
No Description Set
  * :ref:`CDOTABaseGameMode.ClientLoadGridNav`
  * :ref:`CDOTABaseGameMode.SetAlwaysShowPlayerInventory`
  * :ref:`CDOTABaseGameMode.SetBotThinkingEnabled`
  * :ref:`CDOTABaseGameMode.SetBuybackEnabled`
  * :ref:`CDOTABaseGameMode.SetCameraDistanceOverride`
  * :ref:`CDOTABaseGameMode.SetCustomBuybackCooldownEnabled`
  * :ref:`CDOTABaseGameMode.SetCustomBuybackCostEnabled`
  * :ref:`CDOTABaseGameMode.SetCustomHeroMaxLevel`
  * :ref:`CDOTABaseGameMode.SetCustomXPRequiredToReachNextLevel`
  * :ref:`CDOTABaseGameMode.SetFogOfWarDisabled`
  * :ref:`CDOTABaseGameMode.SetGoldSoundDisabled`
  * :ref:`CDOTABaseGameMode.SetOverrideSelectionEntity`
  * :ref:`CDOTABaseGameMode.SetRecommendedItemsDisabled`
  * :ref:`CDOTABaseGameMode.SetRemoveIllusionsOnDeath`
  * :ref:`CDOTABaseGameMode.SetTopBarTeamValue`
  * :ref:`CDOTABaseGameMode.SetTopBarTeamValuesOverride`
  * :ref:`CDOTABaseGameMode.SetTopBarTeamValuesVisible`
  * :ref:`CDOTABaseGameMode.SetTowerBackdoorProtectionEnabled`
  * :ref:`CDOTABaseGameMode.SetUseCustomHeroLevels`
CDotaQuest
############
extends CBaseEntity
A quest, as seen in the Tutorial and Frostivus
  * :ref:`CDotaQuest.AddSubquest`
  * :ref:`CDotaQuest.CompleteQuest`
  * :ref:`CDotaQuest.GetSubquest`
  * :ref:`CDotaQuest.GetSubquestByName`
  * :ref:`CDotaQuest.RemoveSubquest`
  * :ref:`CDotaQuest.SetTextReplaceString`
  * :ref:`CDotaQuest.SetTextReplaceValue`
CDotaSubquestBase
############
extends CDotaQuest
No Description Set
  * :ref:`CDotaSubquestBase.CompleteSubquest`
  * :ref:`CDotaSubquestBase.SetTextReplaceString`
  * :ref:`CDotaSubquestBase.SetTextReplaceValue`
CPhysicsComponent
############
No Description Set
  * :ref:`CPhysicsComponent.ExpensiveInstantRayCast`
CPointTemplate
############
No Description Set
  * :ref:`CPointTemplate.DeleteCreatedSpawnGroups`
  * :ref:`CPointTemplate.ForceSpawn`
  * :ref:`CPointTemplate.GetSpawnedEntities`
  * :ref:`CPointTemplate.SetSpawnCallback`
CBodyComponent
############
No Description Set
  * :ref:`CBodyComponent.AddImpulseAtPosition`
  * :ref:`CBodyComponent.AddVelocity`
  * :ref:`CBodyComponent.DetachFromParent`
  * :ref:`CBodyComponent.GetSequence`
  * :ref:`CBodyComponent.IsAttachedToParent`
  * :ref:`CBodyComponent.LookupSequence`
  * :ref:`CBodyComponent.SequenceDuration`
  * :ref:`CBodyComponent.SetAngularVelocity`
  * :ref:`CBodyComponent.SetAnimation`
  * :ref:`CBodyComponent.SetBodyGroup`
  * :ref:`CBodyComponent.SetMaterialGroup`
  * :ref:`CBodyComponent.SetVelocity`
CBaseAnimating
############
extends CBaseEntity
A class containing functions involved in animations
  * :ref:`CBaseAnimating.GetAttachmentAngles`
  * :ref:`CBaseAnimating.GetAttachmentOrigin`
  * :ref:`CBaseAnimating.IsSequenceFinished`
  * :ref:`CBaseAnimating.ScriptLookupAttachment`
  * :ref:`CBaseAnimating.SetBodygroup`
  * :ref:`CBaseAnimating.SetModelScale`
  * :ref:`CBaseAnimating.SetPoseParameter`
CBaseCombatCharacter
############
No Description Set
  * :ref:`CBaseCombatCharacter.GetEquippedWeapons`
  * :ref:`CBaseCombatCharacter.GetWeaponCount`
ProjectileManager
############
The projectile manager, it manages projectiles.
  * :ref:`ProjectileManager.CreateLinearProjectile`
  * :ref:`ProjectileManager.CreateTrackingProjectile`
  * :ref:`ProjectileManager.DestroyLinearProjectile`
  * :ref:`ProjectileManager.ProjectileDodge`
CBaseTrigger
############
No Description Set
  * :ref:`CBaseTrigger.Disable`
  * :ref:`CBaseTrigger.Enable`
  * :ref:`CBaseTrigger.IsTouching`
CEnvEntityMaker
############
extends CBaseEntity
No Description Set
  * :ref:`CEnvEntityMaker.SpawnEntity`
  * :ref:`CEnvEntityMaker.SpawnEntityAtEntityOrigin`
  * :ref:`CEnvEntityMaker.SpawnEntityAtLocation`
  * :ref:`CEnvEntityMaker.SpawnEntityAtNamedEntityOrigin`
CDOTAVoteSystem
############
No Description Set
  * :ref:`CDOTAVoteSystem.StartVote`
CMarkupVolumeTagged
############
No Description Set
  * :ref:`CMarkupVolumeTagged.HasTag`
CScriptPrecacheContext
############
No Description Set
  * :ref:`CScriptPrecacheContext.AddResource`
  * :ref:`CScriptPrecacheContext.GetValue`
CScriptKeyValues
############
No Description Set
  * :ref:`CScriptKeyValues.GetValue`
CScriptParticleManager
############
No Description Set
  * :ref:`CScriptParticleManager.CreateParticle`
  * :ref:`CScriptParticleManager.CreateParticleForPlayer`
  * :ref:`CScriptParticleManager.GetParticleReplacement`
  * :ref:`CScriptParticleManager.ReleaseParticleIndex`
  * :ref:`CScriptParticleManager.SetParticleAlwaysSimulate`
  * :ref:`CScriptParticleManager.SetParticleControl`
  * :ref:`CScriptParticleManager.SetParticleControlEnt`
CScriptHeroList
############
No Description Set
  * :ref:`CScriptHeroList.GetAllHeroes`
  * :ref:`CScriptHeroList.GetHero`
  * :ref:`CScriptHeroList.GetHeroCount`
CNativeOutputs
############
No Description Set
  * :ref:`CNativeOutputs.AddOutput`
  * :ref:`CNativeOutputs.Init`
CEnvProjectedTexture
############
extends CBaseEntity
No Description Set
  * :ref:`CEnvProjectedTexture.SetFarRange`
  * :ref:`CEnvProjectedTexture.SetLinearAttenuation`
  * :ref:`CEnvProjectedTexture.SetNearRange`
  * :ref:`CEnvProjectedTexture.SetQuadraticAttenuation`
  * :ref:`CEnvProjectedTexture.SetVolumetrics`
CInfoData
############
No Description Set
  * :ref:`CInfoData.QueryColor`
  * :ref:`CInfoData.QueryFloat`
  * :ref:`CInfoData.QueryInt`
  * :ref:`CInfoData.QueryNumber`
  * :ref:`CInfoData.QueryString`
  * :ref:`CInfoData.QueryVector`
CPhysicsProp
############
No Description Set
  * :ref:`CPhysicsProp.DisableMotion`
  * :ref:`CPhysicsProp.EnableMotion`
CDOTAGamerules
############

  * :ref:`CDOTAGamerules.Defeated`
  * :ref:`CDOTAGamerules.DidMatchSignoutTimeOut`
  * :ref:`CDOTAGamerules.GetCustomGameDifficulty`
  * :ref:`CDOTAGamerules.GetDifficulty`
  * :ref:`CDOTAGamerules.GetDroppedItem`
  * :ref:`CDOTAGamerules.GetGameModeEntity`
  * :ref:`CDOTAGamerules.GetGameTime`
  * :ref:`CDOTAGamerules.GetMatchSignoutComplete`
  * :ref:`CDOTAGamerules.GetNianFightStartTime`
  * :ref:`CDOTAGamerules.GetNianTotalDamageTaken`
  * :ref:`CDOTAGamerules.GetTimeOfDay`
  * :ref:`CDOTAGamerules.IsDaytime`
  * :ref:`CDOTAGamerules.MakeTeamLose`
  * :ref:`CDOTAGamerules.NumDroppedItems`
  * :ref:`CDOTAGamerules.Playtesting_UpdateAddOnKeyValues`
  * :ref:`CDOTAGamerules.ResetDefeated`
  * :ref:`CDOTAGamerules.ResetToHeroSelection`
  * :ref:`CDOTAGamerules.SendCustomMessage`
  * :ref:`CDOTAGamerules.SetCreepMinimapIconScale`
  * :ref:`CDOTAGamerules.SetCustomGameDifficulty`
  * :ref:`CDOTAGamerules.SetFirstBloodActive`
  * :ref:`CDOTAGamerules.SetGameWinner`
  * :ref:`CDOTAGamerules.SetGoldPerTick`
  * :ref:`CDOTAGamerules.SetGoldTickTime`
  * :ref:`CDOTAGamerules.SetHeroMinimapIconSize`
  * :ref:`CDOTAGamerules.SetHeroRespawnEnabled`
  * :ref:`CDOTAGamerules.SetHeroSelectionTime`
  * :ref:`CDOTAGamerules.SetNianFightStartTime`
  * :ref:`CDOTAGamerules.SetOverlayHealthBarUnit`
  * :ref:`CDOTAGamerules.SetPostGameTime`
  * :ref:`CDOTAGamerules.SetPreGameTime`
  * :ref:`CDOTAGamerules.SetRuneMinimapIconScale`
  * :ref:`CDOTAGamerules.SetRuneSpawnTime`
  * :ref:`CDOTAGamerules.SetSafeToLeave`
  * :ref:`CDOTAGamerules.SetSameHeroSelectionEnabled`
  * :ref:`CDOTAGamerules.SetTimeOfDay`
  * :ref:`CDOTAGamerules.SetTreeRegrowTime`
  * :ref:`CDOTAGamerules.SetUseBaseGoldBountyOnHeroes`
  * :ref:`CDOTAGamerules.SetUseCustomHeroXPValues`
  * :ref:`CDOTAGamerules.SetUseUniversalShopMode`
  * :ref:`CDOTAGamerules.State_Get`
CToneMapControllerComponent
############
No Description Set
  * :ref:`CToneMapControllerComponent.GetBloomScale`
  * :ref:`CToneMapControllerComponent.GetMaxExposure`
  * :ref:`CToneMapControllerComponent.GetMinExposure`
  * :ref:`CToneMapControllerComponent.SetBloomScale`
  * :ref:`CToneMapControllerComponent.SetMaxExposure`
  * :ref:`CToneMapControllerComponent.SetMinExposure`
CDebugOverlayScriptHelper
############
No Description Set
  * :ref:`CDebugOverlayScriptHelper.Axis`
  * :ref:`CDebugOverlayScriptHelper.Box`
  * :ref:`CDebugOverlayScriptHelper.BoxAngles`
  * :ref:`CDebugOverlayScriptHelper.Capsule`
  * :ref:`CDebugOverlayScriptHelper.Circle`
  * :ref:`CDebugOverlayScriptHelper.CircleScreenOriented`
  * :ref:`CDebugOverlayScriptHelper.Cone`
  * :ref:`CDebugOverlayScriptHelper.Cross`
  * :ref:`CDebugOverlayScriptHelper.Cross3D`
  * :ref:`CDebugOverlayScriptHelper.Cross3DOriented`
  * :ref:`CDebugOverlayScriptHelper.DrawTickMarkedLine`
  * :ref:`CDebugOverlayScriptHelper.EntityAttachments`
  * :ref:`CDebugOverlayScriptHelper.EntityAxis`
  * :ref:`CDebugOverlayScriptHelper.EntityBounds`
  * :ref:`CDebugOverlayScriptHelper.EntitySkeleton`
  * :ref:`CDebugOverlayScriptHelper.EntityText`
  * :ref:`CDebugOverlayScriptHelper.FilledRect2D`
  * :ref:`CDebugOverlayScriptHelper.HorzArrow`
  * :ref:`CDebugOverlayScriptHelper.Line`
  * :ref:`CDebugOverlayScriptHelper.Line2D`
  * :ref:`CDebugOverlayScriptHelper.PopDebugOverlayScope`
  * :ref:`CDebugOverlayScriptHelper.PushAndClearDebugOverlayScope`
  * :ref:`CDebugOverlayScriptHelper.PushDebugOverlayScope`
  * :ref:`CDebugOverlayScriptHelper.RemoveAllInScope`
  * :ref:`CDebugOverlayScriptHelper.SolidCone`
  * :ref:`CDebugOverlayScriptHelper.Sphere`
  * :ref:`CDebugOverlayScriptHelper.SweptBox`
  * :ref:`CDebugOverlayScriptHelper.Text`
  * :ref:`CDebugOverlayScriptHelper.Texture`
  * :ref:`CDebugOverlayScriptHelper.Triangle`
  * :ref:`CDebugOverlayScriptHelper.UnitTestCycleOverlayRenderType`
  * :ref:`CDebugOverlayScriptHelper.VectorText3D`
  * :ref:`CDebugOverlayScriptHelper.VertArrow`
  * :ref:`CDebugOverlayScriptHelper.YawArrow`
CBaseFlex
############
extends CBaseAnimating
Animated characters who have vertex flex capability (Hi hex6)
  * :ref:`CBaseFlex.GetCurrentScene`
  * :ref:`CBaseFlex.GetSceneByIndex`
CSceneEntity
############
extends CBaseEntity
Choreographed scene which controls animation and/or dialog on one or more actors.
  * :ref:`CSceneEntity.AddBroadcastTeamTarget`
  * :ref:`CSceneEntity.Cancel`
  * :ref:`CSceneEntity.EstimateLength`
  * :ref:`CSceneEntity.FindCamera`
  * :ref:`CSceneEntity.FindNamedEntity`
  * :ref:`CSceneEntity.IsPaused`
  * :ref:`CSceneEntity.IsPlayingBack`
  * :ref:`CSceneEntity.LoadSceneFromString`
  * :ref:`CSceneEntity.RemoveBroadcastTeamTarget`
  * :ref:`CSceneEntity.Start`
GridNav
############
A class that can communicate with the gridnav, useful for seeing if stuff should be able to move
  * :ref:`GridNav.GridPosToWorldCenterX`
  * :ref:`GridNav.GridPosToWorldCenterY`
  * :ref:`GridNav.IsBlocked`
  * :ref:`GridNav.IsNearbyTree`
  * :ref:`GridNav.IsTraversable`
  * :ref:`GridNav.RegrowAllTrees`
  * :ref:`GridNav.WorldToGridPosX`
  * :ref:`GridNav.WorldToGridPosY`
Convars
############
No Description Set
  * :ref:`Convars.GetBool`
  * :ref:`Convars.GetCommandClient`
  * :ref:`Convars.GetDOTACommandClient`
  * :ref:`Convars.GetFloat`
  * :ref:`Convars.GetInt`
  * :ref:`Convars.GetStr`
  * :ref:`Convars.RegisterCommand`
  * :ref:`Convars.RegisterConvar`
  * :ref:`Convars.SetBool`
  * :ref:`Convars.SetFloat`
  * :ref:`Convars.SetInt`
  * :ref:`Convars.SetStr`
 .. _Global.AngleDiff:
float AngleDiff(float ang1, float ang2)
`````````````````

Returns the number of degrees difference between two yaw angles


::
    local ang = AngleDiff(45, 80)
print(ang)
+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float | ang1 | No Description Set |
|  float | ang2 | No Description Set |
+-----------+--------------+--------------+
Returns:
float - No Description Set


 .. _Global.AppendToLogFile:
void AppendToLogFile(string , string )
`````````````````

Appends a ''string'' to a log file on the server


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.ApplyDamage:
float ApplyDamage(handle DamageTable)
`````````````````

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
+-----------+--------------+--------------+
|  handle | DamageTable | a table containing Unit Victim, Unit attacker, float damage, and DAMAGE_TYPE type |
+-----------+--------------+--------------+
Returns:
float - damage done after reductions


 .. _Global.AxisAngleToQuaternion:
Quaternion AxisAngleToQuaternion(Vector , float )
`````````````````

(''vector'',''float'') constructs a quaternion representing a rotation by angle around the specified ''vector'' axis


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+
Returns:
Quaternion - No Description Set


 .. _Global.CancelEntityIOEvents:
void CancelEntityIOEvents(ehandle )
`````````````````

Create all I/O events for a particular entity


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  ehandle |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.CreateEffect:
bool CreateEffect(handle )
`````````````````

Pass ''table'' - Inputs: entity, effect


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _Global.CreateHeroForPlayer:
handle CreateHeroForPlayer(string , handle )
`````````````````

Creates a DOTA hero by its dota_npc_units.txt name and sets it as the given player's controlled hero


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _Global.CreateItem:
handle CreateItem(string item_name, handle owner, handle owner)
`````````````````

Creates an item with classname <i>item_name</i> that <i>owner</i> can use.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string | item_name | No Description Set |
|  handle | owner | No Description Set |
|  handle | owner | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _Global.CreateItemOnPositionSync:
handle CreateItemOnPositionSync(Vector , handle )
`````````````````

Create a physical item at a given location


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _Global.CreateTrigger:
handle CreateTrigger(Vector , Vector , Vector )
`````````````````

CreateTrigger( vecMin, vecMax ) : Creates and returns an AABB trigger


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector |  | No Description Set |
|  Vector |  | No Description Set |
|  Vector |  | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _Global.CreateTriggerRadiusApproximate:
handle CreateTriggerRadiusApproximate(Vector , float )
`````````````````

CreateTriggerRadiusApproximate( vecOrigin, flRadius ) : Creates and returns an AABB trigger thats bigger than the radius provided


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _Global.CreateUnitByName:
handle CreateUnitByName(string , Vector , bool , handle , handle , int )
`````````````````

Creates a DOTA unit by its dota_npc_units.txt name ( szUnitName, vLocation, bFindClearSpace, hNPCOwner, hUnitOwner, iTeamNumber )


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
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
int CreateUnitByNameAsync(string , Vector , bool , handle , handle , int , handle )
`````````````````

Creates a DOTA unit by its dota_npc_units.txt name ( szUnitName, vLocation, bFindClearSpace, hNPCOwner, hUnitOwner, iTeamNumber, hCallback )


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
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
float cvar_getf(string )
`````````````````

Gets the value of the given cvar, as a ''float''.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+
Returns:
float - No Description Set


 .. _Global.cvar_setf:
bool cvar_setf(string , float )
`````````````````

Sets the value of the given cvar, as a ''float''.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _Global.DebugBreak:
void DebugBreak()
`````````````````

Breaks in the debugger




 .. _Global.DebugDrawBox:
void DebugDrawBox(Vector , Vector , Vector , int , int , int , int , float )
`````````````````

Draw a debug overlay box (origin, mins, maxs, forward, r, g, b, a, duration )


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
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
void DebugDrawBoxDirection(Vector , Vector , Vector , Vector , Vector , float , float )
`````````````````

Draw a debug forward box (cent, min, max, forward, vRgb, a, duration)


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector |  | No Description Set |
|  Vector |  | No Description Set |
|  Vector |  | No Description Set |
|  Vector |  | No Description Set |
|  Vector |  | No Description Set |
|  float |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.DebugDrawCircle:
void DebugDrawCircle(Vector , Vector , float , float , bool , float )
`````````````````

Draw a debug circle (center, vRgb, a, rad, ztest, duration)


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector |  | No Description Set |
|  Vector |  | No Description Set |
|  float |  | No Description Set |
|  float |  | No Description Set |
|  bool |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.DebugDrawClear:
void DebugDrawClear()
`````````````````

Try to clear all the debug overlay info




 .. _Global.DebugDrawLine:
void DebugDrawLine(Vector , Vector , int , int , int , bool , float )
`````````````````

Draw a debug overlay line (origin, target, r, g, b, ztest, duration)


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector |  | No Description Set |
|  Vector |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  bool |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.DebugDrawLine_vCol:
void DebugDrawLine_vCol(Vector , Vector , Vector , bool , float )
`````````````````

Draw a debug line using color vec (start, end, vRgb, a, ztest, duration)


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector |  | No Description Set |
|  Vector |  | No Description Set |
|  Vector |  | No Description Set |
|  bool |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.DebugDrawScreenTextLine:
void DebugDrawScreenTextLine(float , float , int , string , int , int , int , int , float )
`````````````````

Draw text with a line offset (x, y, lineOffset, text, r, g, b, a, duration)


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
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
void DebugDrawSphere(Vector , Vector , float , float , bool , float )
`````````````````

Draw a debug sphere (center, vRgb, a, rad, ztest, duration)


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector |  | No Description Set |
|  Vector |  | No Description Set |
|  float |  | No Description Set |
|  float |  | No Description Set |
|  bool |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.DebugDrawText:
void DebugDrawText(Vector , string , bool , float )
`````````````````

Draw text in 3d (origin, text, bViewCheck, duration)


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector |  | No Description Set |
|  string |  | No Description Set |
|  bool |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.DebugScreenTextPretty:
void DebugScreenTextPretty(float , float , int , string , int , int , int , int , float , string , int , bool )
`````````````````

Draw pretty debug text (x, y, lineOffset, text, r, g, b, a, duration, font, size, bBold)


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
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
void DoEntFire(string , string , string , float , handle , handle )
`````````````````

EntFire: Generate an entity i/o event ( szTarget, szAction, szValue, flDelay, hActivator, hCaller )


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  string |  | No Description Set |
|  string |  | No Description Set |
|  float |  | No Description Set |
|  handle |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.DoEntFireByInstanceHandle:
void DoEntFireByInstanceHandle(handle , string , string , float , handle , handle )
`````````````````

EntFireByHandle:Generate and entity i/o event


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
|  string |  | No Description Set |
|  string |  | No Description Set |
|  float |  | No Description Set |
|  handle |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.DoIncludeScript:
bool DoIncludeScript(string , handle )
`````````````````

Execute a script (internal)


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _Global.DoScriptAssert:
void DoScriptAssert(bool , string )
`````````````````

ScriptAssert:Asserts the passed in value. Prints out a message and brings up the assert dialog.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.DoUniqueString:
string DoUniqueString(string )
`````````````````

UniqueString:Generate a string guaranteed to be unique across the life of the script VM, with an optional root string. Useful for adding data to table's when not sure what keys are already in use in that table.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+
Returns:
string - No Description Set


 .. _Global.EmitGlobalSound:
void EmitGlobalSound(string )
`````````````````

Play named sound for all players


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.EmitSoundOn:
void EmitSoundOn(string , handle )
`````````````````

Play named sound on Entity


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.EmitSoundOnClient:
void EmitSoundOnClient(string , handle )
`````````````````

Play named sound only on the client for the passed in player


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.EntIndexToHScript:
handle EntIndexToHScript(int )
`````````````````

Turn an entity index integer to an HScript representing that entity's script instance.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _Global.ExecuteOrderFromTable:
void ExecuteOrderFromTable(handle )
`````````````````

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
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.ExponentialDecay:
float ExponentialDecay(float , float , float )
`````````````````

Smooth curve decreasing slower as it approaches zero


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
|  float |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+
Returns:
float - No Description Set


 .. _Global.FileToString:
string FileToString(string )
`````````````````

Reads a ''string'' from a file to send to script


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+
Returns:
string - No Description Set


 .. _Global.FindClearSpaceForUnit:
void FindClearSpaceForUnit(handle , Vector , bool )
`````````````````

Place a unit somewhere not already occupied.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
|  Vector |  | No Description Set |
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.FindUnitsInRadius:
table FindUnitsInRadius(int , Vector , handle , float , int , int , int , int , bool )
`````````````````

Finds the units in a given radius with the given flags. ( iTeamNumber, vPosition, hCacheUnit, flRadius, iTeamFilter, iTypeFilter, iFlagFilter, iOrder, bCanGrowCache )


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
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
void FireEntityIOInputNameOnly(ehandle , string )
`````````````````

Fire Entity's Action Input w/no data


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  ehandle |  | No Description Set |
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.FireEntityIOInputString:
void FireEntityIOInputString(ehandle , string , string )
`````````````````

Fire Entity's Action Input with passed String - you own the memory


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  ehandle |  | No Description Set |
|  string |  | No Description Set |
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.FireEntityIOInputVec:
void FireEntityIOInputVec(ehandle , string , Vector )
`````````````````

Fire Entity's Action Input with passed ''Vector'' ( hEntity, szActionName, vector )


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  ehandle |  | No Description Set |
|  string |  | No Description Set |
|  Vector |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.FireGameEvent:
void FireGameEvent(string eventName, handle parameterTable)
`````````````````

Fire a pre-defined event, which can be found either in custom_events.txt or in dota's resource/*.res


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string | eventName | No Description Set |
|  handle | parameterTable | No Description Set |
+-----------+--------------+--------------+


 .. _Global.FireGameEventLocal:
void FireGameEventLocal(string , handle )
`````````````````

Fire a game event without broadcasting to the client.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.FrameTime:
float FrameTime()
`````````````````

Get the time spent on the server in the last frame


Returns:
float - No Description Set


 .. _Global.GetFrameCount:
int GetFrameCount()
`````````````````

Returns the engines current frame count


Returns:
int - No Description Set


 .. _Global.GetFrostyBoostAmount:
float GetFrostyBoostAmount(int , int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
float - No Description Set


 .. _Global.GetFrostyPointsForRound:
int GetFrostyPointsForRound(int , int , int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _Global.GetGoldFrostyBoostAmount:
float GetGoldFrostyBoostAmount(int , int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
float - No Description Set


 .. _Global.GetGoldFrostyPointsForRound:
int GetGoldFrostyPointsForRound(int , int , int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _Global.GetGroundPosition:
Vector GetGroundPosition(Vector , handle )
`````````````````

Returns the supplied position moved to the ground. Second parameter is an NPC for measuring movement collision hull offset.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+
Returns:
Vector - No Description Set


 .. _Global.GetListenServerHost:
handle GetListenServerHost()
`````````````````

Get the local player on a listen server.


Returns:
handle - No Description Set


 .. _Global.GetMapName:
string GetMapName()
`````````````````

Get the name of the map.


Returns:
string - No Description Set


 .. _Global.GetMaxOutputDelay:
float GetMaxOutputDelay(ehandle , string )
`````````````````

Get the longest delay for all events attached to an output


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  ehandle |  | No Description Set |
|  string |  | No Description Set |
+-----------+--------------+--------------+
Returns:
float - No Description Set


 .. _Global.GetPhysAngularVelocity:
Vector GetPhysAngularVelocity(handle )
`````````````````

Get Angular Velocity for VPHYS or normal object


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+
Returns:
Vector - No Description Set


 .. _Global.GetPhysVelocity:
Vector GetPhysVelocity(handle )
`````````````````

Get Velocity for VPHYS or normal object


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+
Returns:
Vector - No Description Set


 .. _Global.GetSystemDate:
string GetSystemDate()
`````````````````

Get the current real world date


Returns:
string - No Description Set


 .. _Global.GetSystemTime:
string GetSystemTime()
`````````````````

Get the current real world time


Returns:
string - No Description Set


 .. _Global.GetWorldMaxX:
float GetWorldMaxX()
`````````````````

Gets the world's maximum X position.


Returns:
float - No Description Set


 .. _Global.GetWorldMaxY:
float GetWorldMaxY()
`````````````````

Gets the world's maximum Y position.


Returns:
float - No Description Set


 .. _Global.GetWorldMinX:
float GetWorldMinX()
`````````````````

Gets the world's minimum X position.


Returns:
float - No Description Set


 .. _Global.GetWorldMinY:
float GetWorldMinY()
`````````````````

Gets the world's minimum Y position.


Returns:
float - No Description Set


 .. _Global.InitLogFile:
void InitLogFile(string , string )
`````````````````

If the given file doesn't exist, creates it with the given contents; does nothing if it exists


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.IsDedicatedServer:
bool IsDedicatedServer()
`````````````````

Returns true if this server is a dedicated server.


Returns:
bool - No Description Set


 .. _Global.IsMarkedForDeletion:
bool IsMarkedForDeletion(handle )
`````````````````

Returns true if the entity is valid and marked for deletion.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _Global.IsValidEntity:
bool IsValidEntity(handle )
`````````````````

Checks to see if the given hScript is a valid entity


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _Global.ListenToGameEvent:
int ListenToGameEvent(string EventName, handle functionNameToCall, handle context)
`````````````````

Register as a listener for a game event from script.

{{tip|In addition to listening for [[Dota 2 Workshop Tools/Scripting/Built-In Engine Events|standard engine events]], you can also create your own events by placing them in /scripts/custom_events.txt.}}


::
    ListenToGameEvent('entity_killed', Dynamic_Wrap(MyCustomGameMode, 'OnEntityKilled'), self)


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string | EventName | No Description Set |
|  handle | functionNameToCall | No Description Set |
|  handle | context | No Description Set |
+-----------+--------------+--------------+
Returns:
int - a handle for the event/function pair


 .. _Global.LoadKeyValues:
table LoadKeyValues(string )
`````````````````

Creates a ''table'' from the specified keyvalues text file


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+
Returns:
table - No Description Set


 .. _Global.LoadKeyValuesFromString:
table LoadKeyValuesFromString(string )
`````````````````

Creates a ''table'' from the specified keyvalues ''string''


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+
Returns:
table - No Description Set


 .. _Global.MakeStringToken:
int MakeStringToken(string )
`````````````````

Checks to see if the given hScript is a valid entity


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _Global.Msg:
void Msg(string )
`````````````````

Print a message


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.PauseGame:
void PauseGame(bool )
`````````````````

Pause or unpause the game.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.PlayerInstanceFromIndex:
handle PlayerInstanceFromIndex(int )
`````````````````

Get a script instance of a player by index.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _Global.PrecacheEntityFromTable:
void PrecacheEntityFromTable(string , handle , handle )
`````````````````

Precache an entity from KeyValues in ''table''


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  handle |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.PrecacheEntityListFromTable:
void PrecacheEntityListFromTable(handle , handle )
`````````````````

Precache a list of entity KeyValues table's


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.PrecacheItemByNameAsync:
void PrecacheItemByNameAsync(string , handle )
`````````````````

Asynchronously precaches a DOTA item by its dota_npc_items.txt name, provides a callback when it's finished.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.PrecacheItemByNameSync:
void PrecacheItemByNameSync(string , handle )
`````````````````

Precaches a DOTA item by its dota_npc_items.txt name


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.PrecacheModel:
void PrecacheModel(string , handle )
`````````````````

( modelName, context ) - Manually precache a single model


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.PrecacheResource:
void PrecacheResource(string , string , handle )
`````````````````

Manually precache a single resource


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  string |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.PrecacheUnitByNameAsync:
void PrecacheUnitByNameAsync(string , handle )
`````````````````

Asynchronously precaches a DOTA unit by its dota_npc_units.txt name, provides a callback when it's finished.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.PrecacheUnitByNameSync:
void PrecacheUnitByNameSync(string , handle )
`````````````````

Precaches a DOTA unit by its dota_npc_units.txt name


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.PrintLinkedConsoleMessage:
void PrintLinkedConsoleMessage(string , string )
`````````````````

Print a console message with a linked console command


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.RandomFloat:
float RandomFloat(float , float )
`````````````````

Get a random ''float'' within a range


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+
Returns:
float - No Description Set


 .. _Global.RandomInt:
int RandomInt(int , int )
`````````````````

Get a random ''int'' within a range


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _Global.RandomVector:
Vector RandomVector(float )
`````````````````

Get a random 2D ''vector''. Argument (''float'') is the minimum length of the returned vector.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+
Returns:
Vector - No Description Set


 .. _Global.RegisterSpawnGroupFilterProxy:
void RegisterSpawnGroupFilterProxy(string )
`````````````````

Create a C proxy for a script-based spawn group filter


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.ReloadMOTD:
void ReloadMOTD()
`````````````````

Reloads the MotD file




 .. _Global.RemoveSpawnGroupFilterProxy:
void RemoveSpawnGroupFilterProxy(string )
`````````````````

Remove the C proxy for a script-based spawn group filter


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.RollPercentage:
bool RollPercentage(int )
`````````````````

Rolls a number from 1 to 100 and returns true if the roll is less than or equal to the number specified


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _Global.RotateOrientation:
QAngle RotateOrientation(QAngle , QAngle )
`````````````````

Rotate a ''QAngle'' by another ''QAngle''.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  QAngle |  | No Description Set |
|  QAngle |  | No Description Set |
+-----------+--------------+--------------+
Returns:
QAngle - No Description Set


 .. _Global.RotatePosition:
Vector RotatePosition(Vector , QAngle , Vector )
`````````````````

Rotate a ''Vector'' around a point.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector |  | No Description Set |
|  QAngle |  | No Description Set |
|  Vector |  | No Description Set |
+-----------+--------------+--------------+
Returns:
Vector - No Description Set


 .. _Global.RotateQuaternionByAxisAngle:
Quaternion RotateQuaternionByAxisAngle(Quaternion , Vector , float )
`````````````````

Rotates a quaternion by the specified angle around the specified ''vector'' axis


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Quaternion |  | No Description Set |
|  Vector |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+
Returns:
Quaternion - No Description Set


 .. _Global.RotationDelta:
QAngle RotationDelta(QAngle , QAngle )
`````````````````

Find the delta between two ''QAngle''s.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  QAngle |  | No Description Set |
|  QAngle |  | No Description Set |
+-----------+--------------+--------------+
Returns:
QAngle - No Description Set


 .. _Global.rr_AddDecisionRule:
bool rr_AddDecisionRule(handle )
`````````````````

Add a rule to the decision database.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _Global.rr_CommitAIResponse:
bool rr_CommitAIResponse(handle , handle )
`````````````````

Commit the result of QueryBestResponse back to the given entity to play. Call with params (entity, airesponse)


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _Global.rr_GetResponseTargets:
handle rr_GetResponseTargets()
`````````````````

Retrieve a ''table'' of all available expresser targets, in the form { name : ''handle'', name: ''handle'' }.


Returns:
handle - No Description Set


 .. _Global.rr_QueryBestResponse:
bool rr_QueryBestResponse(handle , handle , handle )
`````````````````

Params: ( hEnt, hQuery, hResult ) // Static : tests 'query' against entity's response system and returns the best response found (or ''nil'' if none found).


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
|  handle |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _Global.Say:
void Say(handle entity, string message, bool teamOnly)
`````````````````

Have Entity say ''string'', and teamOnly or not


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle | entity | No Description Set |
|  string | message | No Description Set |
|  bool | teamOnly | No Description Set |
+-----------+--------------+--------------+


 .. _Global.ScreenShake:
void ScreenShake(Vector , float , float , float , float , int , bool )
`````````````````

Start a screenshake with the following parameters. vecCenter, flAmplitude, flFrequency, flDuration, flRadius, eCommand( SHAKE_START = 0, SHAKE_STOP = 1 ), bAirShake


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector |  | No Description Set |
|  float |  | No Description Set |
|  float |  | No Description Set |
|  float |  | No Description Set |
|  float |  | No Description Set |
|  int |  | No Description Set |
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.SendFrostivusTimeElapsedToGC:
void SendFrostivusTimeElapsedToGC()
`````````````````

No Description Set




 .. _Global.SendFrostyPointsMessageToGC:
void SendFrostyPointsMessageToGC(handle )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.SendToConsole:
void SendToConsole(string )
`````````````````

Send a ''string'' to the console as a client command


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.SendToServerConsole:
void SendToServerConsole(string )
`````````````````

Send a ''string'' to the console as a server command


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.SetOpvarFloatAll:
void SetOpvarFloatAll(string , string , string , float )
`````````````````

Sets an opvar value for all players


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  string |  | No Description Set |
|  string |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.SetOpvarFloatPlayer:
void SetOpvarFloatPlayer(string , string , string , float , handle )
`````````````````

Sets an opvar value for a single player ( szStackName, szOperatorName, szOpvarName, flOpvarValue, hEnt )


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  string |  | No Description Set |
|  string |  | No Description Set |
|  float |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.SetQuestName:
void SetQuestName(string )
`````````````````

Set the current quest name.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.SetQuestPhase:
void SetQuestPhase(int )
`````````````````

Set the current quest phase.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.SetRenderingEnabled:
void SetRenderingEnabled(ehandle , bool )
`````````````````

Set rendering on/off for an ''ehandle''


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  ehandle |  | No Description Set |
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.ShowGenericPopup:
void ShowGenericPopup(string title, string content, string unknown, string unknown, int containerType)
`````````````````




+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string | title | No Description Set |
|  string | content | No Description Set |
|  string | unknown | No Description Set |
|  string | unknown | No Description Set |
|  int | containerType | No Description Set |
+-----------+--------------+--------------+


 .. _Global.ShowGenericPopupToPlayer:
void ShowGenericPopupToPlayer(handle , string , string , string , string , int )
`````````````````

Show a generic popup dialog to a specific player.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
|  string |  | No Description Set |
|  string |  | No Description Set |
|  string |  | No Description Set |
|  string |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.ShowMessage:
void ShowMessage(string )
`````````````````

Print a hud message on all clients


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.SpawnEntityFromTableSynchronous:
handle SpawnEntityFromTableSynchronous(string , handle )
`````````````````

Synchronously spawns a single entity from a ''table''


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _Global.SpawnEntityGroupFromTable:
bool SpawnEntityGroupFromTable(handle groupSpawnTables, bool bAsync, handle hCallback)
`````````````````

Hierarchically spawn an entity group from a set of spawn tables.


::
    --some code here
+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle | groupSpawnTables | No Description Set |
|  bool | bAsync | true if running asynchronously |
|  handle | hCallback | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _Global.SpawnEntityListFromTableAsynchronous:
int SpawnEntityListFromTableAsynchronous(handle , handle )
`````````````````

Asynchronously spawn an entity group from a list of spawn table's. A callback will be triggered when the spawning is complete


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _Global.SpawnEntityListFromTableSynchronous:
handle SpawnEntityListFromTableSynchronous(handle )
`````````````````

Synchronously spawn an entity group from a list of spawn table's.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _Global.SplineQuaternions:
Quaternion SplineQuaternions(Quaternion , Quaternion , float )
`````````````````

(quaternion,quaternion,''float'') very basic interpolation of v0 to v1 over t on [0,1]


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Quaternion |  | No Description Set |
|  Quaternion |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+
Returns:
Quaternion - No Description Set


 .. _Global.SplineVectors:
Vector SplineVectors(Vector , Vector , float )
`````````````````

(''vector'',''vector'',''float'') very basic interpolation of v0 to v1 over t on [0,1]


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector |  | No Description Set |
|  Vector |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+
Returns:
Vector - No Description Set


 .. _Global.StartSoundEvent:
void StartSoundEvent(string , handle )
`````````````````

Start a sound event


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.StopEffect:
void StopEffect(handle , string )
`````````````````

(hEntity, szEffectName)


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.StopListeningToAllGameEvents:
void StopListeningToAllGameEvents(handle )
`````````````````

Stop listening to all game events within a specific context.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.StopListeningToGameEvent:
bool StopListeningToGameEvent(int )
`````````````````

Stop listening to a particular game event.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _Global.StopSoundEvent:
void StopSoundEvent(string , handle )
`````````````````

Stops a sound event


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.StopSoundOn:
void StopSoundOn(string soundName, handle playingEntity)
`````````````````

Stop named sound on Entity


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string | soundName | No Description Set |
|  handle | playingEntity | No Description Set |
+-----------+--------------+--------------+


 .. _Global.StringToFile:
bool StringToFile(string , string )
`````````````````

Store a ''string'' to a file for later reading


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  string |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _Global.Time:
float Time()
`````````````````

Get the current server time


Returns:
float - No Description Set


 .. _Global.TraceCollideable:
bool TraceCollideable(handle )
`````````````````

Pass ''table'' - Inputs: start, end, ent, (optional mins, maxs) -- outputs: pos, fraction, hit, startsolid, normal


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _Global.TraceHull:
bool TraceHull(handle )
`````````````````

Pass ''table'' - Inputs: start, end, min, max, mask, ignore  -- outputs: pos, fraction, hit, enthit, startsolid


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _Global.TraceLine:
bool TraceLine(handle )
`````````````````

Pass ''table'' - Inputs: startpos, endpos, mask, ignore  -- outputs: pos, fraction, hit, enthit, startsolid


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _Global.UnloadSpawnGroup:
void UnloadSpawnGroup(string )
`````````````````

Unload a spawn group by name


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.UnloadSpawnGroupByHandle:
void UnloadSpawnGroupByHandle(int )
`````````````````

Unload a spawn group by ''handle''


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.UpdateEventPoints:
void UpdateEventPoints(handle )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.UTIL_Remove:
void UTIL_Remove(handle )
`````````````````

Removes the specified entity


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.UTIL_RemoveImmediate:
void UTIL_RemoveImmediate(handle )
`````````````````

Immediately removes the specified entity


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _Global.VectorToAngles:
QAngle VectorToAngles(Vector )
`````````````````

Get Qangles (with no roll) for a ''Vector''.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector |  | No Description Set |
+-----------+--------------+--------------+
Returns:
QAngle - No Description Set


 .. _Global.Warning:
void Warning(string )
`````````````````

Print a warning


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseEntity.ApplyAbsVelocityImpulse:
void ApplyAbsVelocityImpulse(Vector )
`````````````````

Apply a Velocity Impulse


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector |  | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseEntity.ApplyLocalAngularVelocityImpulse:
void ApplyLocalAngularVelocityImpulse(Vector )
`````````````````

Apply an Ang Velocity Impulse


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector |  | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseEntity.EmitSound:
void EmitSound(string soundName)
`````````````````

 


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string | soundName | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseEntity.EmitSoundParams:
void EmitSoundParams(string soundName, int pitch, float volume, float soundTime)
`````````````````

Plays/modifies a sound from this entity. changes sound if Pitch and/or Volume or SoundTime is > 0.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string | soundName | No Description Set |
|  int | pitch | No Description Set |
|  float | volume | No Description Set |
|  float | soundTime | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseEntity.EyeAngles:
QAngle EyeAngles()
`````````````````

Get the qangles that this entity is looking at.


Returns:
QAngle - No Description Set


 .. _CBaseEntity.EyePosition:
Vector EyePosition()
`````````````````

Get ''vector'' to eye position - absolute coords


Returns:
Vector - No Description Set


 .. _CBaseEntity.FirstMoveChild:
handle FirstMoveChild()
`````````````````

No Description Set


Returns:
handle - No Description Set


 .. _CBaseEntity.GatherCriteria:
void GatherCriteria(handle )
`````````````````

Returns a ''table'' containing the criteria that would be used for response queries on this entity. This is the same as the ''table'' that is passed to response rule script function callbacks.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseEntity.GetAbsOrigin:
Vector GetAbsOrigin()
`````````````````

No Description Set


Returns:
Vector - No Description Set


 .. _CBaseEntity.GetAngles:
QAngle GetAngles()
`````````````````

No Description Set


Returns:
QAngle - No Description Set


 .. _CBaseEntity.GetAnglesAsVector:
Vector GetAnglesAsVector()
`````````````````

Get entity pitch, yaw, roll as a ''vector''


Returns:
Vector - No Description Set


 .. _CBaseEntity.GetAngularVelocity:
Vector GetAngularVelocity()
`````````````````

Get the local angular velocity - returns a ''vector'' of pitch,yaw,roll


Returns:
Vector - No Description Set


 .. _CBaseEntity.GetBaseVelocity:
Vector GetBaseVelocity()
`````````````````

Get Base velocity


Returns:
Vector - No Description Set


 .. _CBaseEntity.GetBoundingMaxs:
Vector GetBoundingMaxs()
`````````````````

Get a ''vector'' containing max bounds, centered on object


Returns:
Vector - No Description Set


 .. _CBaseEntity.GetBoundingMins:
Vector GetBoundingMins()
`````````````````

Get a ''vector'' containing min bounds, centered on object


Returns:
Vector - No Description Set


 .. _CBaseEntity.GetBounds:
table GetBounds()
`````````````````

Get a ''table'' containing the 'Mins' & 'Maxs' ''vector'' bounds, centered on object


Returns:
table - No Description Set


 .. _CBaseEntity.GetCenter:
Vector GetCenter()
`````````````````

Get ''vector'' to center of object - absolute coords


Returns:
Vector - No Description Set


 .. _CBaseEntity.GetChildren:
handle GetChildren()
`````````````````

Get the entities parented to this entity.


Returns:
handle - No Description Set


 .. _CBaseEntity.GetContext:
table GetContext(string )
`````````````````

GetContext( name ): looks up a context and returns it if available. May return ''string'', ''float'', or ''nil'' (if the context isn't found)


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+
Returns:
table - No Description Set


 .. _CBaseEntity.GetForwardVector:
Vector GetForwardVector()
`````````````````

Get the forward ''vector'' of the entity


Returns:
Vector - No Description Set


 .. _CBaseEntity.GetHealth:
int GetHealth()
`````````````````

No Description Set


Returns:
int - No Description Set


 .. _CBaseEntity.GetLocalAngularVelocity:
QAngle GetLocalAngularVelocity()
`````````````````

Maybe local angvel


Returns:
QAngle - No Description Set


 .. _CBaseEntity.GetLocalVelocity:
Vector GetLocalVelocity()
`````````````````

Get Entity relative velocity


Returns:
Vector - No Description Set


 .. _CBaseEntity.GetMaxHealth:
int GetMaxHealth()
`````````````````

No Description Set


Returns:
int - No Description Set


 .. _CBaseEntity.GetModelName:
string GetModelName()
`````````````````

Returns the name of the model


Returns:
string - No Description Set


 .. _CBaseEntity.GetMoveParent:
handle GetMoveParent()
`````````````````

If in hierarchy, retrieves the entity's parent


Returns:
handle - No Description Set


 .. _CBaseEntity.GetOrigin:
Vector GetOrigin()
`````````````````

No Description Set


Returns:
Vector - No Description Set


 .. _CBaseEntity.GetOwner:
handle GetOwner()
`````````````````

Gets this entity's owner


Returns:
handle - No Description Set


 .. _CBaseEntity.GetOwnerEntity:
handle GetOwnerEntity()
`````````````````

Get the owner entity, if there is one


Returns:
handle - No Description Set


 .. _CBaseEntity.GetRightVector:
Vector GetRightVector()
`````````````````

Get the right ''vector'' of the entity


Returns:
Vector - No Description Set


 .. _CBaseEntity.GetRootMoveParent:
handle GetRootMoveParent()
`````````````````

If in hierarchy, walks up the hierarchy to find the root parent


Returns:
handle - No Description Set


 .. _CBaseEntity.GetSoundDuration:
float GetSoundDuration(string soundName, string actormodelname)
`````````````````

Returns ''float'' duration of the sound. Takes soundname and optional actormodelname.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string | soundName | No Description Set |
|  string | actormodelname | No Description Set |
+-----------+--------------+--------------+
Returns:
float - No Description Set


 .. _CBaseEntity.GetTeam:
int GetTeam()
`````````````````

No Description Set


Returns:
int - No Description Set


 .. _CBaseEntity.GetUpVector:
Vector GetUpVector()
`````````````````

Get the up ''vector'' of the entity


Returns:
Vector - No Description Set


 .. _CBaseEntity.GetVelocity:
Vector GetVelocity()
`````````````````

No Description Set


Returns:
Vector - No Description Set


 .. _CBaseEntity.IsAlive:
bool IsAlive()
`````````````````

No Description Set.


Returns:
bool - No Description Set


 .. _CBaseEntity.IsPlayer:
bool IsPlayer()
`````````````````

Is this a player entity?


Returns:
bool - No Description Set


 .. _CBaseEntity.Kill:
void Kill()
`````````````````

No Description Set




 .. _CBaseEntity.NextMovePeer:
handle NextMovePeer()
`````````````````

No Description Set


Returns:
handle - No Description Set


 .. _CBaseEntity.OverrideFriction:
void OverrideFriction(float , float )
`````````````````

Takes duration, value for a temporary override


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseEntity.PrecacheScriptSound:
void PrecacheScriptSound(string )
`````````````````

Precache a sound for later playing.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseEntity.SetAbsOrigin:
void SetAbsOrigin(Vector origin)
`````````````````

SetAbsOrigin


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector | origin | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseEntity.SetAngles:
void SetAngles(float pitch, float yaw, float roll)
`````````````````

Set entity pitch, yaw, roll


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float | pitch | No Description Set |
|  float | yaw | No Description Set |
|  float | roll | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseEntity.SetAngularVelocity:
void SetAngularVelocity(float pitch, float yaw, float roll)
`````````````````

Set the local angular velocity - takes ''float'' pitch,yaw,roll velocities


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float | pitch | No Description Set |
|  float | yaw | No Description Set |
|  float | roll | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseEntity.SetContext:
void SetContext(string , string , float )
`````````````````

SetContext( name , value, duration ): store any key/value pair in this entity's dialog contexts. Value must be a ''string''. Will last for duration (set 0 to mean 'forever').


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  string |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseEntity.SetContextNum:
void SetContextNum(string , float , float )
`````````````````

SetContext( name , value, duration ): store any key/value pair in this entity's dialog contexts. Value must be a number (''int'' or ''float''). Will last for duration (set 0 to mean 'forever').


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  float |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseEntity.SetContextThink:
void SetContextThink(string , handle , float )
`````````````````

Set a think function on this entity.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  handle |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseEntity.SetForwardVector:
void SetForwardVector(Vector forwardVec)
`````````````````

Set the orientation of the entity to have this forward ''forwardVec''


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector | forwardVec | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseEntity.SetFriction:
void SetFriction(float )
`````````````````

Set PLAYER friction, ignored for objects


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseEntity.SetGravity:
void SetGravity(float )
`````````````````

Set PLAYER gravity, ignored for objects


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseEntity.SetHealth:
void SetHealth(int hp)
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int | hp | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseEntity.SetMaxHealth:
void SetMaxHealth(int maxHP)
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int | maxHP | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseEntity.SetModel:
void SetModel(string modelName)
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string | modelName | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseEntity.SetOrigin:
void SetOrigin(Vector origin)
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector | origin | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseEntity.SetOwner:
void SetOwner(handle owningEntity)
`````````````````

Sets this entity's owner


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle | owningEntity | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseEntity.SetParent:
void SetParent(handle , string )
`````````````````

Set the parent for this entity.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseEntity.SetRenderColor:
void SetRenderColor(int , int , int )
`````````````````

SetRenderColor( r, g, b ): Sets the render color of the entity.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseEntity.SetSize:
void SetSize(Vector , Vector )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector |  | No Description Set |
|  Vector |  | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseEntity.SetTeam:
void SetTeam(int team)
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int | team | DOTA_TEAM |
+-----------+--------------+--------------+


 .. _CBaseEntity.SetVelocity:
void SetVelocity(Vector )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector |  | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseEntity.StopSound:
void StopSound(string soundName)
`````````````````

Stops a named sound playing from this entity.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string | soundName | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseEntity.Trigger:
void Trigger()
`````````````````

Fires off this entity's OnTrigger responses




 .. _CEntities.CreateByClassname:
handle CreateByClassname(string className)
`````````````````

Creates an entity by classname


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string | className | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _CEntities.FindAllByClassname:
table FindAllByClassname(string )
`````````````````

Finds all entities by class name. Returns an array containing all the found entities.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+
Returns:
table - No Description Set


 .. _CEntities.FindAllByClassnameWithin:
table FindAllByClassnameWithin(string , Vector , float )
`````````````````

Find entities by class name within a radius.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  Vector |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+
Returns:
table - No Description Set


 .. _CEntities.FindAllByModel:
table FindAllByModel(string modelName)
`````````````````

Find entities by model name.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string | modelName | No Description Set |
+-----------+--------------+--------------+
Returns:
table - No Description Set


 .. _CEntities.FindAllByName:
table FindAllByName(string name)
`````````````````

Find all entities by name. Returns an array containing all the found entities in it.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string | name | No Description Set |
+-----------+--------------+--------------+
Returns:
table - No Description Set


 .. _CEntities.FindAllByNameWithin:
table FindAllByNameWithin(string name, Vector origin, float maxRadius)
`````````````````

Find entities by name within a radius.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string | name | No Description Set |
|  Vector | origin | No Description Set |
|  float | maxRadius | No Description Set |
+-----------+--------------+--------------+
Returns:
table - No Description Set


 .. _CEntities.FindAllByTarget:
table FindAllByTarget(string targetName)
`````````````````

Find entities by targetname.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string | targetName | No Description Set |
+-----------+--------------+--------------+
Returns:
table - No Description Set


 .. _CEntities.FindAllInSphere:
table FindAllInSphere(Vector origin, float maxRadius)
`````````````````

Find entities within a radius.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector | origin | No Description Set |
|  float | maxRadius | No Description Set |
+-----------+--------------+--------------+
Returns:
table - No Description Set


 .. _CEntities.FindByClassname:
handle FindByClassname(handle startFrom, string className)
`````````````````

Find entities by class name. Pass ''nil'' to start an iteration, or reference to a previously found entity to continue a search


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle | startFrom | No Description Set |
|  string | className | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _CEntities.FindByClassnameNearest:
handle FindByClassnameNearest(string className, Vector origin, float maxRadius)
`````````````````

Find entities by class name nearest to a point.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string | className | No Description Set |
|  Vector | origin | No Description Set |
|  float | maxRadius | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _CEntities.FindByClassnameWithin:
handle FindByClassnameWithin(handle startFrom, string className, Vector origin, float maxRadius)
`````````````````

Find entities by class name within a radius. Pass ''nil'' to start an iteration, or reference to a previously found entity to continue a search


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle | startFrom | No Description Set |
|  string | className | No Description Set |
|  Vector | origin | No Description Set |
|  float | maxRadius | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _CEntities.FindByModel:
handle FindByModel(handle startFrom, string modelName)
`````````````````

Find entities by model name. Pass ''nil'' to start an iteration, or reference to a previously found entity to continue a search


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle | startFrom | No Description Set |
|  string | modelName | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _CEntities.FindByModelWithin:
handle FindByModelWithin(handle startFrom, string modelName, Vector origin, float maxRadius)
`````````````````

Find entities by model name within a radius. Pass ''nil'' to start an iteration, or reference to a previously found entity to continue a search


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle | startFrom | No Description Set |
|  string | modelName | No Description Set |
|  Vector | origin | No Description Set |
|  float | maxRadius | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _CEntities.FindByName:
handle FindByName(handle lastEnt, string searchString)
`````````````````

Find entities by name. Pass ''nil'' to start an iteration, or reference to a previously found entity to continue a search


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle | lastEnt | No Description Set |
|  string | searchString | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _CEntities.FindByNameNearest:
handle FindByNameNearest(string name, Vector origin, float maxRadius)
`````````````````

Find entities by name nearest to a point.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string | name | No Description Set |
|  Vector | origin | No Description Set |
|  float | maxRadius | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _CEntities.FindByNameWithin:
handle FindByNameWithin(handle startFrom, string name, Vector origin, float maxRadius)
`````````````````

Find entities by name within a radius. Pass ''nil'' to start an iteration, or reference to a previously found entity to continue a search


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle | startFrom | No Description Set |
|  string | name | No Description Set |
|  Vector | origin | No Description Set |
|  float | maxRadius | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _CEntities.FindByTarget:
handle FindByTarget(handle startFrom, string targetName)
`````````````````

Find entities by targetname. Pass ''nil'' to start an iteration, or reference to a previously found entity to continue a search


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle | startFrom | No Description Set |
|  string | targetName | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _CEntities.FindInSphere:
handle FindInSphere(handle startFrom, Vector origin, float maxRadius)
`````````````````

Find entities within a radius. Pass ''nil'' to start an iteration, or reference to a previously found entity to continue a search


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle | startFrom | No Description Set |
|  Vector | origin | No Description Set |
|  float | maxRadius | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _CEntities.First:
handle First()
`````````````````

Begin an iteration over the list of entities


Returns:
handle - No Description Set


 .. _CEntities.Next:
handle Next(handle startFrom)
`````````````````

Continue an iteration over the list of entities, providing reference to a previously found entity


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle | startFrom | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _CEntityInstance.ConnectOutput:
void ConnectOutput(string , string )
`````````````````

Adds an I/O connection that will call the named function on this entity when the specified output fires.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _CEntityInstance.Destroy:
void Destroy()
`````````````````

No Description Set




 .. _CEntityInstance.DisconnectOutput:
void DisconnectOutput(string , string )
`````````````````

Removes a connected script function from an I/O event on this entity.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _CEntityInstance.DisconnectRedirectedOutput:
void DisconnectRedirectedOutput(string , string , handle )
`````````````````

Removes a connected script function from an I/O event on the passed entity.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  string |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CEntityInstance.entindex:
int entindex()
`````````````````

No Description Set


Returns:
int - No Description Set


 .. _CEntityInstance.FireOutput:
void FireOutput(string , handle , handle , table , float )
`````````````````

Fire an entity output


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  handle |  | No Description Set |
|  handle |  | No Description Set |
|  table |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CEntityInstance.GetClassname:
string GetClassname()
`````````````````

No Description Set


Returns:
string - No Description Set


 .. _CEntityInstance.GetDebugName:
string GetDebugName()
`````````````````

Get the entity name w/help if not defined (i.e. classname/etc)


Returns:
string - No Description Set


 .. _CEntityInstance.GetEntityHandle:
ehandle GetEntityHandle()
`````````````````

Get the entity as an EHANDLE


Returns:
ehandle - No Description Set


 .. _CEntityInstance.GetEntityIndex:
int GetEntityIndex()
`````````````````

No Description Set


Returns:
int - No Description Set


 .. _CEntityInstance.GetIntAttr:
int GetIntAttr(string )
`````````````````

Get Integer Attribute


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CEntityInstance.GetName:
string GetName()
`````````````````

No Description Set


Returns:
string - No Description Set


 .. _CEntityInstance.GetOrCreatePrivateScriptScope:
handle GetOrCreatePrivateScriptScope()
`````````````````

Retrieve, creating if necessary, the private per-instance script-side data associated with an entity


Returns:
handle - No Description Set


 .. _CEntityInstance.GetOrCreatePublicScriptScope:
handle GetOrCreatePublicScriptScope()
`````````````````

Retrieve, creating if necessary, the public script-side data associated with an entity


Returns:
handle - No Description Set


 .. _CEntityInstance.GetPrivateScriptScope:
handle GetPrivateScriptScope()
`````````````````

Retrieve the private per-instance script-side data associated with an entity


Returns:
handle - No Description Set


 .. _CEntityInstance.GetPublicScriptScope:
handle GetPublicScriptScope()
`````````````````

Retrieve the public script-side data associated with an entity


Returns:
handle - No Description Set


 .. _CEntityInstance.RedirectOutput:
void RedirectOutput(string , string , handle )
`````````````````

Adds an I/O connection that will call the named function on the passed entity when the specified output fires.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  string |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CEntityInstance.RemoveSelf:
void RemoveSelf()
`````````````````

Delete this entity




 .. _CEntityInstance.SetIntAttr:
void SetIntAttr(string , int )
`````````````````

Set Integer Attribute


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseAbility.CastAbility:
void CastAbility()
`````````````````

No Description Set




 .. _CDOTABaseAbility.ContinueCasting:
bool ContinueCasting()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTABaseAbility.CreateVisibilityNode:
void CreateVisibilityNode(Vector , float , float )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector |  | No Description Set |
|  float |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseAbility.DecrementModifierRefCount:
void DecrementModifierRefCount()
`````````````````

No Description Set




 .. _CDOTABaseAbility.EndChannel:
void EndChannel(bool )
`````````````````

Param: ''bool'' bInterrupted


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseAbility.EndCooldown:
void EndCooldown()
`````````````````

Clear the cooldown remaining on this ability.




 .. _CDOTABaseAbility.GetAbilityDamage:
int GetAbilityDamage()
`````````````````

No Description Set


Returns:
int - No Description Set


 .. _CDOTABaseAbility.GetAbilityDamageType:
int GetAbilityDamageType()
`````````````````

No Description Set


Returns:
int - No Description Set


 .. _CDOTABaseAbility.GetAbilityIndex:
int GetAbilityIndex()
`````````````````

No Description Set


Returns:
int - No Description Set


 .. _CDOTABaseAbility.GetAbilityName:
string GetAbilityName()
`````````````````

No Description Set


Returns:
string - No Description Set


 .. _CDOTABaseAbility.GetAbilityTargetFlags:
int GetAbilityTargetFlags()
`````````````````

No Description Set


Returns:
int - No Description Set


 .. _CDOTABaseAbility.GetAbilityTargetTeam:
int GetAbilityTargetTeam()
`````````````````

No Description Set


Returns:
int - No Description Set


 .. _CDOTABaseAbility.GetAbilityTargetType:
int GetAbilityTargetType()
`````````````````

No Description Set


Returns:
int - No Description Set


 .. _CDOTABaseAbility.GetAbilityType:
int GetAbilityType()
`````````````````

No Description Set


Returns:
int - No Description Set


 .. _CDOTABaseAbility.GetAnimationIgnoresModelScale:
bool GetAnimationIgnoresModelScale()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTABaseAbility.GetAssociatedPrimaryAbilities:
string GetAssociatedPrimaryAbilities()
`````````````````

No Description Set


Returns:
string - No Description Set


 .. _CDOTABaseAbility.GetAssociatedSecondaryAbilities:
string GetAssociatedSecondaryAbilities()
`````````````````

No Description Set


Returns:
string - No Description Set


 .. _CDOTABaseAbility.GetAutoCastState:
bool GetAutoCastState()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTABaseAbility.GetBackswingTime:
float GetBackswingTime()
`````````````````

No Description Set


Returns:
float - No Description Set


 .. _CDOTABaseAbility.GetBehavior:
int GetBehavior()
`````````````````

No Description Set


Returns:
int - No Description Set


 .. _CDOTABaseAbility.GetCaster:
handle GetCaster()
`````````````````

No Description Set


Returns:
handle - No Description Set


 .. _CDOTABaseAbility.GetCastPoint:
float GetCastPoint()
`````````````````

No Description Set


Returns:
float - No Description Set


 .. _CDOTABaseAbility.GetCastRange:
int GetCastRange()
`````````````````

No Description Set


Returns:
int - No Description Set


 .. _CDOTABaseAbility.GetChannelledManaCostPerSecond:
int GetChannelledManaCostPerSecond(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTABaseAbility.GetChannelStartTime:
float GetChannelStartTime()
`````````````````

No Description Set


Returns:
float - No Description Set


 .. _CDOTABaseAbility.GetChannelTime:
float GetChannelTime()
`````````````````

No Description Set


Returns:
float - No Description Set


 .. _CDOTABaseAbility.GetCloneSource:
handle GetCloneSource()
`````````````````

No Description Set


Returns:
handle - No Description Set


 .. _CDOTABaseAbility.GetConceptRecipientType:
int GetConceptRecipientType()
`````````````````

No Description Set


Returns:
int - No Description Set


 .. _CDOTABaseAbility.GetCooldown:
float GetCooldown(int )
`````````````````

Get the cooldown duration for this ability at a given level, not the amount of cooldown actually left.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
float - No Description Set


 .. _CDOTABaseAbility.GetCooldownTime:
float GetCooldownTime()
`````````````````

No Description Set


Returns:
float - No Description Set


 .. _CDOTABaseAbility.GetCooldownTimeRemaining:
float GetCooldownTimeRemaining()
`````````````````

No Description Set


Returns:
float - No Description Set


 .. _CDOTABaseAbility.GetCursorPosition:
Vector GetCursorPosition()
`````````````````

No Description Set


Returns:
Vector - No Description Set


 .. _CDOTABaseAbility.GetCursorTarget:
handle GetCursorTarget()
`````````````````

No Description Set


Returns:
handle - No Description Set


 .. _CDOTABaseAbility.GetCursorTargetingNothing:
bool GetCursorTargetingNothing()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTABaseAbility.GetDuration:
float GetDuration()
`````````````````

No Description Set


Returns:
float - No Description Set


 .. _CDOTABaseAbility.GetGoldCost:
int GetGoldCost(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTABaseAbility.GetGoldCostForUpgrade:
int GetGoldCostForUpgrade(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTABaseAbility.GetHeroLevelRequiredToUpgrade:
int GetHeroLevelRequiredToUpgrade()
`````````````````

No Description Set


Returns:
int - No Description Set


 .. _CDOTABaseAbility.GetIntrinsicModifierName:
string GetIntrinsicModifierName()
`````````````````

No Description Set


Returns:
string - No Description Set


 .. _CDOTABaseAbility.GetLevel:
int GetLevel()
`````````````````

Get the current level of the ability


Returns:
int - No Description Set


 .. _CDOTABaseAbility.GetLevelSpecialValueFor:
table GetLevelSpecialValueFor(string , int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
table - No Description Set


 .. _CDOTABaseAbility.GetManaCost:
int GetManaCost(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTABaseAbility.GetMaxLevel:
int GetMaxLevel()
`````````````````

No Description Set


Returns:
int - No Description Set


 .. _CDOTABaseAbility.GetModifierValue:
float GetModifierValue()
`````````````````

No Description Set


Returns:
float - No Description Set


 .. _CDOTABaseAbility.GetModifierValueBonus:
float GetModifierValueBonus()
`````````````````

No Description Set


Returns:
float - No Description Set


 .. _CDOTABaseAbility.GetPlaybackRateOverride:
float GetPlaybackRateOverride()
`````````````````

No Description Set


Returns:
float - No Description Set


 .. _CDOTABaseAbility.GetSharedCooldownName:
string GetSharedCooldownName()
`````````````````

No Description Set


Returns:
string - No Description Set


 .. _CDOTABaseAbility.GetSpecialValueFor:
table GetSpecialValueFor(string )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+
Returns:
table - No Description Set


 .. _CDOTABaseAbility.GetStolenActivityModifier:
string GetStolenActivityModifier()
`````````````````

No Description Set


Returns:
string - No Description Set


 .. _CDOTABaseAbility.GetToggleState:
bool GetToggleState()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTABaseAbility.HeroXPChange:
bool HeroXPChange(float )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _CDOTABaseAbility.IncrementModifierRefCount:
void IncrementModifierRefCount()
`````````````````

No Description Set




 .. _CDOTABaseAbility.IsActivated:
bool IsActivated()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTABaseAbility.IsAttributeBonus:
bool IsAttributeBonus()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTABaseAbility.IsChanneling:
bool IsChanneling()
`````````````````

Returns whether the ability is currently channeling.


Returns:
bool - No Description Set


 .. _CDOTABaseAbility.IsCooldownReady:
bool IsCooldownReady()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTABaseAbility.IsCosmetic:
bool IsCosmetic()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTABaseAbility.IsFullyCastable:
bool IsFullyCastable()
`````````````````

Returns whether the ability can be cast.


Returns:
bool - No Description Set


 .. _CDOTABaseAbility.IsHidden:
bool IsHidden()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTABaseAbility.IsHiddenWhenStolen:
bool IsHiddenWhenStolen()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTABaseAbility.IsInAbilityPhase:
bool IsInAbilityPhase()
`````````````````

Returns whether the ability is currently casting.


Returns:
bool - No Description Set


 .. _CDOTABaseAbility.IsItem:
bool IsItem()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTABaseAbility.IsOwnersGoldEnough:
bool IsOwnersGoldEnough(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _CDOTABaseAbility.IsOwnersGoldEnoughForUpgrade:
bool IsOwnersGoldEnoughForUpgrade()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTABaseAbility.IsOwnersManaEnough:
bool IsOwnersManaEnough()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTABaseAbility.IsPassive:
bool IsPassive()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTABaseAbility.IsSharedWithTeammates:
bool IsSharedWithTeammates()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTABaseAbility.IsStealable:
bool IsStealable()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTABaseAbility.IsStolen:
bool IsStolen()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTABaseAbility.IsToggle:
bool IsToggle()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTABaseAbility.IsTrained:
bool IsTrained()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTABaseAbility.MarkAbilityButtonDirty:
void MarkAbilityButtonDirty()
`````````````````

Mark the ability button for this ability as needing a refresh




 .. _CDOTABaseAbility.NumModifiersUsingAbility:
int NumModifiersUsingAbility()
`````````````````

No Description Set


Returns:
int - No Description Set


 .. _CDOTABaseAbility.OnAbilityPhaseInterrupted:
void OnAbilityPhaseInterrupted()
`````````````````

No Description Set




 .. _CDOTABaseAbility.OnAbilityPhaseStart:
bool OnAbilityPhaseStart()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTABaseAbility.OnAbilityPinged:
void OnAbilityPinged()
`````````````````

No Description Set




 .. _CDOTABaseAbility.OnChannelFinish:
void OnChannelFinish(bool )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseAbility.OnChannelThink:
void OnChannelThink(float )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseAbility.OnHeroCalculateStatBonus:
void OnHeroCalculateStatBonus()
`````````````````

No Description Set




 .. _CDOTABaseAbility.OnHeroLevelUp:
void OnHeroLevelUp()
`````````````````

No Description Set




 .. _CDOTABaseAbility.OnInventoryContentsChanged:
void OnInventoryContentsChanged()
`````````````````

No Description Set




 .. _CDOTABaseAbility.OnOwnerDied:
void OnOwnerDied()
`````````````````

No Description Set




 .. _CDOTABaseAbility.OnOwnerSpawned:
void OnOwnerSpawned()
`````````````````

No Description Set




 .. _CDOTABaseAbility.OnSpellStart:
void OnSpellStart()
`````````````````

No Description Set




 .. _CDOTABaseAbility.OnToggle:
void OnToggle()
`````````````````

No Description Set




 .. _CDOTABaseAbility.OnUpgrade:
void OnUpgrade()
`````````````````

No Description Set




 .. _CDOTABaseAbility.PayGoldCost:
void PayGoldCost()
`````````````````

No Description Set




 .. _CDOTABaseAbility.PayGoldCostForUpgrade:
void PayGoldCostForUpgrade()
`````````````````

No Description Set




 .. _CDOTABaseAbility.PayManaCost:
void PayManaCost()
`````````````````

No Description Set




 .. _CDOTABaseAbility.PlaysDefaultAnimWhenStolen:
bool PlaysDefaultAnimWhenStolen()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTABaseAbility.ProcsMagicStick:
bool ProcsMagicStick()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTABaseAbility.RefCountsModifiers:
bool RefCountsModifiers()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTABaseAbility.RefundManaCost:
void RefundManaCost()
`````````````````

No Description Set




 .. _CDOTABaseAbility.ResetToggleOnRespawn:
bool ResetToggleOnRespawn()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTABaseAbility.SetAbilityIndex:
void SetAbilityIndex(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseAbility.SetActivated:
void SetActivated(bool )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseAbility.SetChanneling:
void SetChanneling(bool )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseAbility.SetHidden:
void SetHidden(bool )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseAbility.SetInAbilityPhase:
void SetInAbilityPhase(bool )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseAbility.SetLevel:
void SetLevel(int )
`````````````````

Sets the level of this ability.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseAbility.SetOverrideCastPoint:
void SetOverrideCastPoint(float )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseAbility.SetRefCountsModifiers:
void SetRefCountsModifiers(bool )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseAbility.SetStolen:
void SetStolen(bool )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseAbility.ShouldUseResources:
bool ShouldUseResources()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTABaseAbility.SpeakAbilityConcept:
void SpeakAbilityConcept(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseAbility.SpeakTrigger:
bool SpeakTrigger()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTABaseAbility.StartCooldown:
void StartCooldown(float )
`````````````````

param: flCooldown


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseAbility.ToggleAbility:
void ToggleAbility()
`````````````````

No Description Set




 .. _CDOTABaseAbility.ToggleAutoCast:
void ToggleAutoCast()
`````````````````

No Description Set




 .. _CDOTABaseAbility.UpgradeAbility:
void UpgradeAbility()
`````````````````

No Description Set




 .. _CDOTABaseAbility.UseResources:
void UseResources(bool , bool , bool )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
|  bool |  | No Description Set |
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_Ability_Animation_Attack.SetPlaybackRate:
void SetPlaybackRate(float )
`````````````````

Override playbackrate


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_Ability_Animation_TailSpin.SetPlaybackRate:
void SetPlaybackRate(float )
`````````````````

Override playbackrate


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_Ability_Nian_Leap.SetPlaybackRate:
void SetPlaybackRate(float )
`````````````````

Override playbackrate


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_Ability_Nian_Dive.SetPlaybackRate:
void SetPlaybackRate(float )
`````````````````

Override playbackrate


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_Ability_Nian_Roar.GetCastCount:
int GetCastCount()
`````````````````

Number of times Nian has used the roar


Returns:
int - No Description Set


 .. _CDOTA_Item.GetContainer:
handle GetContainer()
`````````````````

Get the container for this item.


Returns:
handle - No Description Set


 .. _CDOTA_Item.GetCost:
int GetCost()
`````````````````

No Description Set


Returns:
int - No Description Set


 .. _CDOTA_Item.GetCurrentCharges:
int GetCurrentCharges()
`````````````````

Get the number of charges this item currently has.


Returns:
int - No Description Set


 .. _CDOTA_Item.GetInitialCharges:
int GetInitialCharges()
`````````````````

Get the initial number of charges this item has.


Returns:
int - No Description Set


 .. _CDOTA_Item.GetPurchaser:
handle GetPurchaser()
`````````````````

Get the purchaser for this item.


Returns:
handle - No Description Set


 .. _CDOTA_Item.GetPurchaseTime:
float GetPurchaseTime()
`````````````````

Get the purchase time of this item


Returns:
float - No Description Set


 .. _CDOTA_Item.GetShareability:
int GetShareability()
`````````````````

No Description Set


Returns:
int - No Description Set


 .. _CDOTA_Item.IsPermanent:
bool IsPermanent()
`````````````````

Is this a permanent item?


Returns:
bool - No Description Set


 .. _CDOTA_Item.LaunchLoot:
void LaunchLoot(bool , float , float , Vector )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
|  float |  | No Description Set |
|  float |  | No Description Set |
|  Vector |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_Item.SetCurrentCharges:
void SetCurrentCharges(int )
`````````````````

Set the number of charges on this item


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_Item.SetPurchaser:
void SetPurchaser(handle )
`````````````````

Set the purchaser of record for this item.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_Item.SetPurchaseTime:
void SetPurchaseTime(float )
`````````````````

Set the purchase time of this item


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_Item.SetStacksWithOtherOwners:
void SetStacksWithOtherOwners(bool )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_Item.StacksWithOtherOwners:
bool StacksWithOtherOwners()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_Item.Think:
void Think()
`````````````````

Think this item




 .. _CDOTA_Item_Physical.GetContainedItem:
handle GetContainedItem()
`````````````````

Returned the contained item.


Returns:
handle - No Description Set


 .. _CDOTA_Item_Physical.GetCreationTime:
float GetCreationTime()
`````````````````

Returns the game time when this item was created in the world


Returns:
float - No Description Set


 .. _CDOTA_Item_Physical.SetContainedItem:
void SetContainedItem(handle )
`````````````````

Set the contained item.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_Item_DataDriven.ApplyDataDrivenModifier:
void ApplyDataDrivenModifier(handle source, handle target, string modifier_name, handle modifierArgs)
`````````````````




+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle | source | No Description Set |
|  handle | target | No Description Set |
|  string | modifier_name | No Description Set |
|  handle | modifierArgs | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_Unit_Nian.GetHorn:
handle GetHorn()
`````````````````

Is the Nian horn?


Returns:
handle - No Description Set


 .. _CDOTA_Unit_Nian.GetTail:
handle GetTail()
`````````````````

Is the Nian's tail broken?


Returns:
handle - No Description Set


 .. _CDOTA_Unit_Nian.IsHornAlive:
bool IsHornAlive()
`````````````````

Is the Nian's horn broken?


Returns:
bool - No Description Set


 .. _CDOTA_Unit_Nian.IsTailAlive:
bool IsTailAlive()
`````````````````

Is the Nian's tail broken?


Returns:
bool - No Description Set


 .. _CBasePlayer.IsNoclipping:
bool IsNoclipping()
`````````````````

Returns true if the player is in noclip mode.


Returns:
bool - No Description Set


 .. _CDOTAPlayer.GetAssignedHero:
handle GetAssignedHero()
`````````````````

Get the player's hero.


Returns:
handle - No Description Set


 .. _CDOTAPlayer.GetControlledRPGUnit:
handle GetControlledRPGUnit()
`````````````````

Get the RPG unit this player controls.


Returns:
handle - No Description Set


 .. _CDOTAPlayer.GetPlayerID:
int GetPlayerID()
`````````````````

Get the player's official PlayerID; notably is -1 when the player isn't yet on a team.


Returns:
int - No Description Set


 .. _CDOTAPlayer.MakeRandomHeroSelection:
void MakeRandomHeroSelection()
`````````````````

Randoms this player's hero.




 .. _CDOTAPlayer.SetKillCamUnit:
void SetKillCamUnit(handle )
`````````````````

Set the kill cam unit for this hero.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTAPlayer.SetMusicStatus:
void SetMusicStatus(int nMusicStatus, float flIntensity)
`````````````````

Set the music status for this player, note this will only really apply if dota_music_battle_enable is off.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int | nMusicStatus | Status flag of the Music |
|  float | flIntensity | Intensity of the music |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.AddAegisPickup:
void AddAegisPickup(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.AddClaimedFarm:
void AddClaimedFarm(int , float )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.AddGoldSpentOnSupport:
void AddGoldSpentOnSupport(int , int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.AddRunePickup:
void AddRunePickup(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.AreUnitsSharedWithPlayerID:
bool AreUnitsSharedWithPlayerID(int , int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _CDOTA_PlayerResource.ClearKillsMatrix:
void ClearKillsMatrix(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.ClearLastHitMultikill:
void ClearLastHitMultikill(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.ClearLastHitStreak:
void ClearLastHitStreak(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.ClearRawPlayerDamageMatrix:
void ClearRawPlayerDamageMatrix(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.ClearStreak:
void ClearStreak(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.GetAegisPickups:
int GetAegisPickups(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetAssists:
int GetAssists(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetBroadcasterChannel:
<> GetBroadcasterChannel(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
<> - No Description Set


 .. _CDOTA_PlayerResource.GetBroadcasterChannelSlot:
<> GetBroadcasterChannelSlot(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
<> - No Description Set


 .. _CDOTA_PlayerResource.GetClaimedDenies:
int GetClaimedDenies(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetClaimedFarm:
float GetClaimedFarm(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
float - No Description Set


 .. _CDOTA_PlayerResource.GetClaimedMisses:
int GetClaimedMisses(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetConnectionState:
<> GetConnectionState(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
<> - No Description Set


 .. _CDOTA_PlayerResource.GetCreepDamageTaken:
int GetCreepDamageTaken(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetCustomBuybackCooldown:
float GetCustomBuybackCooldown(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
float - No Description Set


 .. _CDOTA_PlayerResource.GetCustomBuybackCost:
int GetCustomBuybackCost(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetDamageDoneToHero:
int GetDamageDoneToHero(int , int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetDeaths:
int GetDeaths(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetDenies:
int GetDenies(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetEventPointsForPlayerID:
int GetEventPointsForPlayerID(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetEventPremiumPointsGranted:
int GetEventPremiumPointsGranted(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetEventRankGranted:
int GetEventRankGranted(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetGold:
int GetGold(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetGoldBagsCollected:
int GetGoldBagsCollected(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetGoldLostToDeath:
int GetGoldLostToDeath(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetGoldPerMin:
float GetGoldPerMin(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
float - No Description Set


 .. _CDOTA_PlayerResource.GetGoldSpentOnBuybacks:
int GetGoldSpentOnBuybacks(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetGoldSpentOnConsumables:
int GetGoldSpentOnConsumables(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetGoldSpentOnItems:
int GetGoldSpentOnItems(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetGoldSpentOnSupport:
int GetGoldSpentOnSupport(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetHealing:
float GetHealing(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
float - No Description Set


 .. _CDOTA_PlayerResource.GetHeroDamageTaken:
int GetHeroDamageTaken(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetKills:
int GetKills(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetKillsDoneToHero:
int GetKillsDoneToHero(int , int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetLastHitMultikill:
int GetLastHitMultikill(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetLastHits:
int GetLastHits(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetLastHitStreak:
int GetLastHitStreak(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetLevel:
int GetLevel(int playerID)
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int | playerID | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetMisses:
int GetMisses(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetNearbyCreepDeaths:
int GetNearbyCreepDeaths(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetNthCourierForTeam:
handle GetNthCourierForTeam(int , int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _CDOTA_PlayerResource.GetNthPlayerIDOnTeam:
int GetNthPlayerIDOnTeam(int , int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetNumConsumablesPurchased:
int GetNumConsumablesPurchased(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetNumCouriersForTeam:
int GetNumCouriersForTeam(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetNumItemsPurchased:
int GetNumItemsPurchased(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetPlayer:
handle GetPlayer(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _CDOTA_PlayerResource.GetPlayerLoadedCompletely:
bool GetPlayerLoadedCompletely(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _CDOTA_PlayerResource.GetPlayerName:
string GetPlayerName(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
string - No Description Set


 .. _CDOTA_PlayerResource.GetPlayerReservedState:
bool GetPlayerReservedState(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _CDOTA_PlayerResource.GetRawPlayerDamage:
int GetRawPlayerDamage(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetReliableGold:
int GetReliableGold(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetRespawnSeconds:
int GetRespawnSeconds(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetRoshanKills:
int GetRoshanKills(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetRunePickups:
int GetRunePickups(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetSelectedHeroEntity:
handle GetSelectedHeroEntity(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _CDOTA_PlayerResource.GetSelectedHeroID:
int GetSelectedHeroID(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetSelectedHeroName:
string GetSelectedHeroName(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
string - No Description Set


 .. _CDOTA_PlayerResource.GetSteamAccountID:
<> GetSteamAccountID(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
<> - No Description Set


 .. _CDOTA_PlayerResource.GetStreak:
int GetStreak(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetStuns:
float GetStuns(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
float - No Description Set


 .. _CDOTA_PlayerResource.GetTeam:
int GetTeam(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetTeamKills:
int GetTeamKills(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetTimeOfLastConsumablePurchase:
float GetTimeOfLastConsumablePurchase(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
float - No Description Set


 .. _CDOTA_PlayerResource.GetTimeOfLastDeath:
float GetTimeOfLastDeath(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
float - No Description Set


 .. _CDOTA_PlayerResource.GetTimeOfLastItemPurchase:
float GetTimeOfLastItemPurchase(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
float - No Description Set


 .. _CDOTA_PlayerResource.GetTotalEarnedGold:
int GetTotalEarnedGold(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetTotalEarnedXP:
int GetTotalEarnedXP(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetTotalGoldSpent:
int GetTotalGoldSpent(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetTowerDamageTaken:
int GetTowerDamageTaken(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetTowerKills:
int GetTowerKills(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetUnitShareMaskForPlayer:
int GetUnitShareMaskForPlayer(int , int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetUnreliableGold:
int GetUnreliableGold(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.GetXPPerMin:
float GetXPPerMin(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
float - No Description Set


 .. _CDOTA_PlayerResource.HasRandomed:
bool HasRandomed(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _CDOTA_PlayerResource.HasRepicked:
bool HasRepicked(int playerID)
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int | playerID | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _CDOTA_PlayerResource.HasSelectedHero:
bool HasSelectedHero(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _CDOTA_PlayerResource.HaveAllPlayersJoined:
bool HaveAllPlayersJoined()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_PlayerResource.HeroLevelUp:
void HeroLevelUp(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.IncrementAssists:
void IncrementAssists(int playerID)
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int | playerID | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.IncrementClaimedDenies:
void IncrementClaimedDenies(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.IncrementClaimedMisses:
void IncrementClaimedMisses(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.IncrementDeaths:
void IncrementDeaths(int playerID)
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int | playerID | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.IncrementDenies:
void IncrementDenies(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.IncrementGoldBagsCollected:
void IncrementGoldBagsCollected(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.IncrementKills:
void IncrementKills(int playerID, int kills)
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int | playerID | No Description Set |
|  int | kills | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.IncrementLastHitMultikill:
void IncrementLastHitMultikill(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.IncrementLastHits:
void IncrementLastHits(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.IncrementLastHitStreak:
void IncrementLastHitStreak(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.IncrementMisses:
void IncrementMisses(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.IncrementNearbyCreepDeaths:
void IncrementNearbyCreepDeaths(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.IncrementStreak:
void IncrementStreak(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.IncrementTotalEarnedXP:
void IncrementTotalEarnedXP(int , int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.IsBroadcaster:
bool IsBroadcaster(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _CDOTA_PlayerResource.IsDisableHelpSetForPlayerID:
bool IsDisableHelpSetForPlayerID(int , int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _CDOTA_PlayerResource.IsFakeClient:
bool IsFakeClient(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _CDOTA_PlayerResource.IsHeroSelected:
bool IsHeroSelected(string )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _CDOTA_PlayerResource.IsHeroSharedWithPlayerID:
bool IsHeroSharedWithPlayerID(int , int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _CDOTA_PlayerResource.IsValidPlayer:
bool IsValidPlayer(int playerID)
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int | playerID | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _CDOTA_PlayerResource.IsValidPlayerID:
bool IsValidPlayerID(int playerID)
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int | playerID | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _CDOTA_PlayerResource.IsValidTeamPlayer:
bool IsValidTeamPlayer(int playerID)
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int | playerID | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _CDOTA_PlayerResource.IsValidTeamPlayerID:
bool IsValidTeamPlayerID(int playerID)
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int | playerID | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _CDOTA_PlayerResource.ModifyGold:
int ModifyGold(int playerID, int goldAmmt, bool reliable, int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int | playerID | No Description Set |
|  int | goldAmmt | No Description Set |
|  bool | reliable | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_PlayerResource.ReplaceHeroWith:
handle ReplaceHeroWith(int , string , int , int )
`````````````````

(playerID, heroClassName, gold, XP) - replaces the player's hero with a new one of the specified class, gold and XP


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
|  string |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _CDOTA_PlayerResource.ResetBuybackCostTime:
void ResetBuybackCostTime(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.ResetTotalEarnedGold:
void ResetTotalEarnedGold(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.SetBuybackCooldownTime:
void SetBuybackCooldownTime(int , float )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.SetBuybackGoldLimitTime:
void SetBuybackGoldLimitTime(int , float )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.SetCameraTarget:
void SetCameraTarget(int , handle )
`````````````````

(playerID, entity) - force the given player's camera to follow the given entity


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.SetCustomBuybackCooldown:
void SetCustomBuybackCooldown(int , float )
`````````````````

Set the buyback cooldown for this player.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.SetCustomBuybackCost:
void SetCustomBuybackCost(int , int )
`````````````````

Set the buyback cost for this player.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.SetGold:
void SetGold(int , int , bool )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
|  int |  | No Description Set |
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.SetHasRandomed:
void SetHasRandomed(int playerID)
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int | playerID | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.SetHasRepicked:
void SetHasRepicked(int playerID)
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int | playerID | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.SetLastBuybackTime:
void SetLastBuybackTime(int , int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.SetPlayerReservedState:
void SetPlayerReservedState(int , bool )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.SetUnitShareMaskForPlayer:
void SetUnitShareMaskForPlayer(int , int , int , bool )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.SpendGold:
void SpendGold(int , int , int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.UpdateTeamSlot:
void UpdateTeamSlot(int , int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_PlayerResource.WhoSelectedHero:
int WhoSelectedHero(string )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_BaseNPC.AddAbility:
void AddAbility(string )
`````````````````

Add an ability to this unit by name.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.AddItem:
void AddItem(handle )
`````````````````

Add an item to this unit's inventory.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.AddNewModifier:
void AddNewModifier(handle caster, handle optionalSourceAbility, string modifierName, handle modifierData)
`````````````````




+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle | caster | No Description Set |
|  handle | optionalSourceAbility | No Description Set |
|  string | modifierName | No Description Set |
|  handle | modifierData | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.AddNoDraw:
void AddNoDraw()
`````````````````

Adds the no draw flag.




 .. _CDOTA_BaseNPC.AlertNearbyUnits:
void AlertNearbyUnits(handle , handle )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.AngerNearbyUnits:
void AngerNearbyUnits()
`````````````````

No Description Set




 .. _CDOTA_BaseNPC.AttackNoEarlierThan:
void AttackNoEarlierThan(float )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.AttackReady:
bool AttackReady()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.BoundingRadius2D:
float BoundingRadius2D()
`````````````````

No Description Set


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.CastAbilityImmediately:
void CastAbilityImmediately(handle , int )
`````````````````

Cast an ability immediately.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.CastAbilityNoTarget:
void CastAbilityNoTarget(handle ability, int playerIndex)
`````````````````

Cast an ability with no target. ( hAbility, iPlayerIndex )


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle | ability | No Description Set |
|  int | playerIndex | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.CastAbilityOnPosition:
void CastAbilityOnPosition(Vector , handle , int )
`````````````````

Cast an ability on a position.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector |  | No Description Set |
|  handle |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.CastAbilityOnTarget:
void CastAbilityOnTarget(handle target, handle ability, int playerIndex)
`````````````````

Cast an ability on a target entity.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle | target | No Description Set |
|  handle | ability | No Description Set |
|  int | playerIndex | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.CastAbilityToggle:
void CastAbilityToggle(handle , int )
`````````````````

Toggle an ability. ( hAbility, iPlayerIndex )


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.DisassembleItem:
void DisassembleItem(handle )
`````````````````

Disassemble the passed item in this unit's inventory.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.DropItemAtPosition:
void DropItemAtPosition(Vector , handle )
`````````````````

Drop an item at a given point.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.DropItemAtPositionImmediate:
void DropItemAtPositionImmediate(handle , Vector )
`````````````````

Immediately drop a carried item at a given position.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
|  Vector |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.EjectItemFromStash:
void EjectItemFromStash(handle )
`````````````````

Drops the selected item out of this unit's stash.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.FindAbilityByName:
handle FindAbilityByName(string )
`````````````````

Retrieve an ability by name from the unit.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _CDOTA_BaseNPC.ForceKill:
void ForceKill(bool )
`````````````````

Kill this unit immediately.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.GetAbilityByIndex:
handle GetAbilityByIndex(int )
`````````````````

Retrieve an ability by index from the unit.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _CDOTA_BaseNPC.GetAbilityCount:
int GetAbilityCount()
`````````````````

No Description Set


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC.GetAcquisitionRange:
float GetAcquisitionRange()
`````````````````

Gets the range at which this unit will auto-acquire.


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetAdditionalBattleMusicWeight:
float GetAdditionalBattleMusicWeight()
`````````````````

Combat involving this creature will have this weight added to the music calcuations


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetAttackAnimationPoint:
float GetAttackAnimationPoint()
`````````````````

No Description Set


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetAttackDamage:
int GetAttackDamage()
`````````````````

Returns a random integer between the minimum and maximum base damage of the unit.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC.GetAttackRange:
float GetAttackRange()
`````````````````

Gets this unit's attack range after all modifiers.


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetAttackRangeBuffer:
float GetAttackRangeBuffer()
`````````````````

Gets the attack range buffer.


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetAttackSpeed:
float GetAttackSpeed()
`````````````````

No Description Set


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetAttacksPerSecond:
float GetAttacksPerSecond()
`````````````````

No Description Set


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetAttackTarget:
handle GetAttackTarget()
`````````````````

No Description Set


Returns:
handle - No Description Set


 .. _CDOTA_BaseNPC.GetAverageTrueAttackDamage:
int GetAverageTrueAttackDamage()
`````````````````

Returns the average value of the minimum and maximum damage values.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC.GetBaseAttackRange:
int GetBaseAttackRange()
`````````````````

Gets this unit's attack range before modifiers.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC.GetBaseAttackTime:
float GetBaseAttackTime()
`````````````````

No Description Set


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetBaseDamageMax:
int GetBaseDamageMax()
`````````````````

Gets the minimum base damage.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC.GetBaseDamageMin:
int GetBaseDamageMin()
`````````````````

Gets the minimum base damage.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC.GetBaseDayTimeVisionRange:
int GetBaseDayTimeVisionRange()
`````````````````

Returns the vision range before modifiers.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC.GetBaseHealthRegen:
float GetBaseHealthRegen()
`````````````````

No Description Set


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetBaseMagicalResistanceValue:
float GetBaseMagicalResistanceValue()
`````````````````

Returns base magical armor value.


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetBaseMaxHealth:
float GetBaseMaxHealth()
`````````````````

Gets the base max health value.


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetBaseMoveSpeed:
float GetBaseMoveSpeed()
`````````````````

No Description Set


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetBaseNightTimeVisionRange:
int GetBaseNightTimeVisionRange()
`````````````````

Returns the vision range before modifiers.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC.GetCastPoint:
float GetCastPoint(bool )
`````````````````

Parameter: bAttack


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+
Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetCollisionPadding:
float GetCollisionPadding()
`````````````````

Returns the size of the collision padding around the hull.


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetConstantBasedManaRegen:
float GetConstantBasedManaRegen()
`````````````````

This Mana regen is derived from constant bonuses like Basilius.


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetCreationTime:
float GetCreationTime()
`````````````````

No Description Set


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetCurrentActiveAbility:
handle GetCurrentActiveAbility()
`````````````````

Get the ability this unit is currently casting.


Returns:
handle - No Description Set


 .. _CDOTA_BaseNPC.GetCurrentVisionRange:
int GetCurrentVisionRange()
`````````````````

Gets the current vision range.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC.GetCursorCastTarget:
handle GetCursorCastTarget()
`````````````````

No Description Set


Returns:
handle - No Description Set


 .. _CDOTA_BaseNPC.GetCursorPosition:
Vector GetCursorPosition()
`````````````````

No Description Set


Returns:
Vector - No Description Set


 .. _CDOTA_BaseNPC.GetCursorTargetingNothing:
bool GetCursorTargetingNothing()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.GetDayTimeVisionRange:
int GetDayTimeVisionRange()
`````````````````

Returns the vision range after modifiers.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC.GetDeathXP:
int GetDeathXP()
`````````````````

Get the XP bounty on this unit


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC.GetForceAttackTarget:
handle GetForceAttackTarget()
`````````````````

No Description Set


Returns:
handle - No Description Set


 .. _CDOTA_BaseNPC.GetGoldBounty:
int GetGoldBounty()
`````````````````

Get the gold bounty on this unit


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC.GetHasteFactor:
float GetHasteFactor()
`````````````````

No Description Set


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetHealth:
int GetHealth()
`````````````````

Get the health of this unit.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC.GetHealthDeficit:
int GetHealthDeficit()
`````````````````

Returns integer amount of health missing from max.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC.GetHealthPercent:
int GetHealthPercent()
`````````````````

Get the current health percent of the unit.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC.GetHealthRegen:
float GetHealthRegen()
`````````````````

No Description Set


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetHullRadius:
float GetHullRadius()
`````````````````

Get the collision hull radius of this NPC


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetIdealSpeed:
float GetIdealSpeed()
`````````````````

Returns speed after all modifiers.


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetIncreasedAttackSpeed:
float GetIncreasedAttackSpeed()
`````````````````

No Description Set


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetInitialGoalEntity:
handle GetInitialGoalEntity()
`````````````````

Returns the initial waypoint goal for this NPC


Returns:
handle - No Description Set


 .. _CDOTA_BaseNPC.GetItemInSlot:
handle GetItemInSlot(int )
`````````````````

Returns nth item in inventory slot (index is zero based)


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _CDOTA_BaseNPC.GetLastIdleChangeTime:
float GetLastIdleChangeTime()
`````````````````

Get the last game time that this unit switched to/from idle state.


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetLevel:
int GetLevel()
`````````````````

Returns the level of this unit.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC.GetMagicalArmorValue:
float GetMagicalArmorValue()
`````````````````

Returns current magical armor value.


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetMainControllingPlayer:
int GetMainControllingPlayer()
`````````````````

Returns the player ID of the controlling player.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC.GetMana:
float GetMana()
`````````````````

Get the mana on this unit.


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetManaPercent:
int GetManaPercent()
`````````````````

Get the percent of mana remaining.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC.GetManaRegen:
float GetManaRegen()
`````````````````

No Description Set


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetMaxHealth:
int GetMaxHealth()
`````````````````

Get the maximum health of this unit.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC.GetMaxMana:
float GetMaxMana()
`````````````````

Get the maximum mana of this unit.


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetModelRadius:
float GetModelRadius()
`````````````````

No Description Set


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetModifierCount:
int GetModifierCount()
`````````````````

How many modifiers does this unit have?


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC.GetModifierNameByIndex:
string GetModifierNameByIndex(int )
`````````````````

Get a modifier name by index.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
string - No Description Set


 .. _CDOTA_BaseNPC.GetMoveSpeedModifier:
float GetMoveSpeedModifier(float )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+
Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetMustReachEachGoalEntity:
bool GetMustReachEachGoalEntity()
`````````````````

Get whether this NPC is required to reach each goal entity, rather than being allowed to 'unkink' their path


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.GetNightTimeVisionRange:
int GetNightTimeVisionRange()
`````````````````

Returns the vision range after modifiers.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC.GetOpposingTeamNumber:
int GetOpposingTeamNumber()
`````````````````

No Description Set


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC.GetPaddedCollisionRadius:
float GetPaddedCollisionRadius()
`````````````````

Get the collision hull radius (including padding) of this NPC


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetPercentageBasedManaRegen:
float GetPercentageBasedManaRegen()
`````````````````

This Mana regen is derived from % bonuses (from items like Void Stone).


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetPhysicalArmorBaseValue:
float GetPhysicalArmorBaseValue()
`````````````````

Returns base physical armor value.


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetPhysicalArmorValue:
float GetPhysicalArmorValue()
`````````````````

Returns current physical armor value.


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetPlayerOwner:
handle GetPlayerOwner()
`````````````````

Returns the player that owns this unit


Returns:
handle - No Description Set


 .. _CDOTA_BaseNPC.GetPlayerOwnerID:
int GetPlayerOwnerID()
`````````````````

Get the owner player ID for this unit.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC.GetProjectileSpeed:
int GetProjectileSpeed()
`````````````````

No Description Set


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC.GetRangeToUnit:
float GetRangeToUnit(handle )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+
Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetSecondsPerAttack:
float GetSecondsPerAttack()
`````````````````

No Description Set


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetStatsBasedManaRegen:
float GetStatsBasedManaRegen()
`````````````````

Returns mana regen rate per intelligence.


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.GetTeamNumber:
int GetTeamNumber()
`````````````````

Get the team number of this unit.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC.GetTotalPurchasedUpgradeGoldCost:
int GetTotalPurchasedUpgradeGoldCost()
`````````````````

Get how much gold has been spent on ability upgrades.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC.GetUnitLabel:
string GetUnitLabel()
`````````````````

No Description Set


Returns:
string - No Description Set


 .. _CDOTA_BaseNPC.GetUnitName:
string GetUnitName()
`````````````````

No Description Set


Returns:
string - No Description Set


 .. _CDOTA_BaseNPC.GiveMana:
void GiveMana(float )
`````````````````

Give mana to this unit, this can be used for mana gained by abilities or item usage.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.HasAbility:
bool HasAbility(string )
`````````````````

See whether this unit has an ability by name.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.HasAttackCapability:
bool HasAttackCapability()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.HasFlyingVision:
bool HasFlyingVision()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.HasFlyMovementCapability:
bool HasFlyMovementCapability()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.HasGroundMovementCapability:
bool HasGroundMovementCapability()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.HasInventory:
bool HasInventory()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.HasItemInInventory:
bool HasItemInInventory(string )
`````````````````

See whether this unit has an item by name.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.HasModifier:
bool HasModifier(string )
`````````````````

Sees if this unit has a given modifier


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.HasMovementCapability:
bool HasMovementCapability()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.HasScepter:
bool HasScepter()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.Heal:
void Heal(float , handle )
`````````````````

Heal this unit.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.Hold:
void Hold()
`````````````````

Hold position.




 .. _CDOTA_BaseNPC.Interrupt:
void Interrupt()
`````````````````

No Description Set




 .. _CDOTA_BaseNPC.InterruptChannel:
void InterruptChannel()
`````````````````

No Description Set




 .. _CDOTA_BaseNPC.InterruptMotionControllers:
void InterruptMotionControllers(bool )
`````````````````

Parameter boolean determines finding clear space.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.IsAlive:
bool IsAlive()
`````````````````

Is this unit alive?


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsAncient:
bool IsAncient()
`````````````````

Is this creature an Ancient?


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsAttackImmune:
bool IsAttackImmune()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsAttacking:
bool IsAttacking()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsAttackingEntity:
bool IsAttackingEntity(handle )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsBlind:
bool IsBlind()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsBlockDisabled:
bool IsBlockDisabled()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsCommandRestricted:
bool IsCommandRestricted()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsControllableByAnyPlayer:
bool IsControllableByAnyPlayer()
`````````````````

Is this unit controlled by any non-bot player?


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsCreature:
bool IsCreature()
`````````````````

Is this a Creature type NPC


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsDeniable:
bool IsDeniable()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsDisarmed:
bool IsDisarmed()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsDominated:
bool IsDominated()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsEvadeDisabled:
bool IsEvadeDisabled()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsFrozen:
bool IsFrozen()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsHardDisarmed:
bool IsHardDisarmed()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsHero:
bool IsHero()
`````````````````

Is this a hero or hero illusion?


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsHexed:
bool IsHexed()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsIdle:
bool IsIdle()
`````````````````

Is this creature currently idle?


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsIllusion:
bool IsIllusion()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsInvisible:
bool IsInvisible()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsInvulnerable:
bool IsInvulnerable()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsLowAttackPriority:
bool IsLowAttackPriority()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsMagicImmune:
bool IsMagicImmune()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsMechanical:
bool IsMechanical()
`````````````````

Is the unit mechanical?


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsMovementImpaired:
bool IsMovementImpaired()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsMuted:
bool IsMuted()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsNeutralUnitType:
bool IsNeutralUnitType()
`````````````````

Is this a neutral?


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsNightmared:
bool IsNightmared()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsOpposingTeam:
bool IsOpposingTeam(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsOutOfGame:
bool IsOutOfGame()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsOwnedByAnyPlayer:
bool IsOwnedByAnyPlayer()
`````````````````

Is this unit owned by any non-bot player?


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsPhantom:
bool IsPhantom()
`````````````````

Is this a phantom unit?


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsPhantomBlocker:
bool IsPhantomBlocker()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsPhased:
bool IsPhased()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsPositionInRange:
bool IsPositionInRange(Vector , float )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsRangedAttacker:
bool IsRangedAttacker()
`````````````````

Is this unit a ranged attacker?


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsRealHero:
bool IsRealHero()
`````````````````

Returns true if the hero is a true Hero, not a creep or an Illusion of a hero


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsRooted:
bool IsRooted()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsSilenced:
bool IsSilenced()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsSoftDisarmed:
bool IsSoftDisarmed()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsSpeciallyDeniable:
bool IsSpeciallyDeniable()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsStunned:
bool IsStunned()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsSummoned:
bool IsSummoned()
`````````````````

Is this unit summoned?


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsTower:
bool IsTower()
`````````````````

Is this a tower?


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsUnableToMiss:
bool IsUnableToMiss()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.IsUnselectable:
bool IsUnselectable()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.Kill:
void Kill(handle , handle )
`````````````````

Kills this NPC, with the params Ability and Attacker


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.MakeIllusion:
void MakeIllusion()
`````````````````

No Description Set




 .. _CDOTA_BaseNPC.MakePhantomBlocker:
void MakePhantomBlocker()
`````````````````

No Description Set




 .. _CDOTA_BaseNPC.MakeVisibleDueToAttack:
void MakeVisibleDueToAttack(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.MakeVisibleToTeam:
void MakeVisibleToTeam(int , float )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.ModifyHealth:
void ModifyHealth(int , handle , bool , int )
`````````````````

Sets the health to a specific value, with optional flags or inflictors.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
|  handle |  | No Description Set |
|  bool |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.MoveToNPC:
void MoveToNPC(handle )
`````````````````

Move to follow a unit.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.MoveToNPCToGiveItem:
void MoveToNPCToGiveItem(handle , handle )
`````````````````

Give an item to another unit.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.MoveToPosition:
void MoveToPosition(Vector )
`````````````````

Issue a Move-To command


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.MoveToPositionAggressive:
void MoveToPositionAggressive(Vector )
`````````````````

Issue an Attack-Move-To command


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.MoveToTargetToAttack:
void MoveToTargetToAttack(handle )
`````````````````

Move to a target to attack.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.NoHealthBar:
bool NoHealthBar()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.NoTeamMoveTo:
bool NoTeamMoveTo()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.NoTeamSelect:
bool NoTeamSelect()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.NotOnMinimap:
bool NotOnMinimap()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.NotOnMinimapForEnemies:
bool NotOnMinimapForEnemies()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.NoUnitCollision:
bool NoUnitCollision()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.PassivesDisabled:
bool PassivesDisabled()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.PerformAttack:
void PerformAttack(handle , bool , bool , bool , bool )
`````````````````

Performs an attack on a target. Params: Target, bUseCastAttackOrb, bProcessProcs, bSkipCooldown, bIgnoreInvis


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
|  bool |  | No Description Set |
|  bool |  | No Description Set |
|  bool |  | No Description Set |
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.PickupDroppedItem:
void PickupDroppedItem(handle )
`````````````````

Pick up a dropped item.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.PickupRune:
void PickupRune(handle )
`````````````````

Pick up a rune.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.ProvidesVision:
bool ProvidesVision()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.ReduceMana:
void ReduceMana(float )
`````````````````

Remove mana from this unit, this can be used for involuntary mana loss, not for mana that is spent.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.RemoveAbility:
void RemoveAbility(string )
`````````````````

Remove an ability from this unit by name.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.RemoveItem:
void RemoveItem(handle )
`````````````````

Removes the passed item from this unit's inventory.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.RemoveModifierByName:
void RemoveModifierByName(string )
`````````````````

Removes a modifier


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.RemoveModifierByNameAndCaster:
void RemoveModifierByNameAndCaster(string , handle )
`````````````````

Removes a modifier that was cast by the given caster


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.RemoveNoDraw:
void RemoveNoDraw()
`````````````````

Remove the no draw flag.




 .. _CDOTA_BaseNPC.RespawnUnit:
void RespawnUnit()
`````````````````

Respawns the target unit if it can be respawned.




 .. _CDOTA_BaseNPC.SellItem:
void SellItem(handle )
`````````````````

Sells the passed item in this unit's inventory.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetAdditionalBattleMusicWeight:
void SetAdditionalBattleMusicWeight(float )
`````````````````

Combat involving this creature will have this weight added to the music calcuations


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetAttackCapability:
void SetAttackCapability(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetAttacking:
void SetAttacking(handle )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetBaseAttackTime:
void SetBaseAttackTime(float )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetBaseDamageMax:
void SetBaseDamageMax(int )
`````````````````

Sets the minimum base damage.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetBaseDamageMin:
void SetBaseDamageMin(int )
`````````````````

Sets the minimum base damage.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetBaseHealthRegen:
void SetBaseHealthRegen(float )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetBaseMagicalResistanceValue:
void SetBaseMagicalResistanceValue(float )
`````````````````

Sets base magical armor value.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetBaseManaRegen:
void SetBaseManaRegen(float )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetBaseMaxHealth:
void SetBaseMaxHealth(float )
`````````````````

Set a new base max health value.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetBaseMoveSpeed:
void SetBaseMoveSpeed(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetControllableByPlayer:
void SetControllableByPlayer(int , bool )
`````````````````

Set this unit controllable by the player with the passed ID.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetCursorCastTarget:
void SetCursorCastTarget(handle )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetCursorPosition:
void SetCursorPosition(Vector )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetCursorTargetingNothing:
void SetCursorTargetingNothing(bool )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetDayTimeVisionRange:
void SetDayTimeVisionRange(int )
`````````````````

Set the base vision range.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetDeathXP:
void SetDeathXP(int )
`````````````````

Set the XP bounty on this unit


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetForceAttackTarget:
void SetForceAttackTarget(handle )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetHasInventory:
void SetHasInventory(bool )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetHullRadius:
void SetHullRadius(float )
`````````````````

Set the collision hull radius of this NPC


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetIdleAcquire:
void SetIdleAcquire(bool )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetInitialGoalEntity:
void SetInitialGoalEntity(handle )
`````````````````

Sets the initial waypoint goal for this NPC


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetMana:
void SetMana(float )
`````````````````

Set the mana on this unit.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetMaximumGoldBounty:
void SetMaximumGoldBounty(int )
`````````````````

Set the maximum gold bounty for this unit.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetMinimumGoldBounty:
void SetMinimumGoldBounty(int )
`````````````````

Set the minimum gold bounty for this unit.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetMoveCapability:
void SetMoveCapability(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetMustReachEachGoalEntity:
void SetMustReachEachGoalEntity(bool )
`````````````````

Set whether this NPC is required to reach each goal entity, rather than being allowed to 'unkink' their path


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetNeverMoveToClearSpace:
void SetNeverMoveToClearSpace(bool )
`````````````````

If set to true, we will never attempt to move this unit to clear space, even when it unphases.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetNightTimeVisionRange:
void SetNightTimeVisionRange(int )
`````````````````

Set the base vision range.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetOriginalModel:
void SetOriginalModel(string originalModel)
`````````````````

Sets the original model of this entity, which it will tend to fall back to anytime its state changes


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string | originalModel | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetPhysicalArmorBaseValue:
void SetPhysicalArmorBaseValue(float )
`````````````````

Sets base physical armor value.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetRangedProjectileName:
void SetRangedProjectileName(string )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetStolenScepter:
void SetStolenScepter(bool )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.SetUnitName:
void SetUnitName(string )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.ShouldIdleAcquire:
bool ShouldIdleAcquire()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.SpendMana:
void SpendMana(float , handle )
`````````````````

Spend mana from this unit, this can be used for spending mana from abilities or item usage.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.Stop:
void Stop()
`````````````````

Stop the current order.




 .. _CDOTA_BaseNPC.SwapAbilities:
void SwapAbilities(string , string , bool , bool )
`````````````````

Swaps the slots of the two passed abilities and sets them enabled/disabled: const char* AbilityName1, const char* AbilityName2, ''bool'' bEnable1, ''bool'' bEnable2. The boolean controls which ability is active. The ability order is never swapped when swapping abilities, only the boolean statements are flipped.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  string |  | No Description Set |
|  bool |  | No Description Set |
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC.TimeUntilNextAttack:
float TimeUntilNextAttack()
`````````````````

No Description Set


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC.TriggerModifierDodge:
bool TriggerModifierDodge()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.TriggerSpellAbsorb:
bool TriggerSpellAbsorb(handle )
`````````````````

Query whether the passed ability will trigger spell absorb on this unit.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC.UnitCanRespawn:
bool UnitCanRespawn()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC_Hero.AddExperience:
bool AddExperience(float amount, bool applyBotDifficultyScaling)
`````````````````

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
+-----------+--------------+--------------+
|  float | amount | No Description Set |
|  bool | applyBotDifficultyScaling | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC_Hero.Buyback:
void Buyback()
`````````````````

Spend the gold and buyback with this hero.




 .. _CDOTA_BaseNPC_Hero.CalculateStatBonus:
void CalculateStatBonus()
`````````````````

Recalculate all stats after the hero gains stats.




 .. _CDOTA_BaseNPC_Hero.CanEarnGold:
bool CanEarnGold()
`````````````````

Returns boolean value result of buyback gold limit time less than game time.


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC_Hero.ClearLastHitMultikill:
void ClearLastHitMultikill()
`````````````````

Value is stored in PlayerResource.




 .. _CDOTA_BaseNPC_Hero.ClearLastHitStreak:
void ClearLastHitStreak()
`````````````````

Value is stored in PlayerResource.




 .. _CDOTA_BaseNPC_Hero.ClearStreak:
void ClearStreak()
`````````````````

Value is stored in PlayerResource.




 .. _CDOTA_BaseNPC_Hero.GetAbilityPoints:
int GetAbilityPoints()
`````````````````

Gets the current unspent ability point's.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetAgility:
float GetAgility()
`````````````````

No Description Set


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetAgilityGain:
float GetAgilityGain()
`````````````````

No Description Set


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetAssists:
int GetAssists()
`````````````````

Value is stored in PlayerResource.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetAttacker:
int GetAttacker(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetBaseAgility:
float GetBaseAgility()
`````````````````

No Description Set


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetBaseDamageMax:
int GetBaseDamageMax()
`````````````````

Hero damage is also affected by attributes.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetBaseDamageMin:
int GetBaseDamageMin()
`````````````````

Hero damage is also affected by attributes.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetBaseIntellect:
float GetBaseIntellect()
`````````````````

No Description Set


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetBaseStrength:
float GetBaseStrength()
`````````````````

No Description Set


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetBonusDamageFromPrimaryStat:
int GetBonusDamageFromPrimaryStat()
`````````````````

No Description Set


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetBuybackCooldownTime:
float GetBuybackCooldownTime()
`````````````````

Return ''float'' value for the amount of time left on cooldown for this hero's buyback.


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetBuybackCost:
int GetBuybackCost()
`````````````````

Return integer value for the gold cost of a buyback.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetBuybackGoldLimitTime:
float GetBuybackGoldLimitTime()
`````````````````

Returns the amount of time gold gain is limited after buying back.


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetCurrentXP:
int GetCurrentXP()
`````````````````

Returns the amount of XP


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetDeathGoldCost:
int GetDeathGoldCost()
`````````````````

No Description Set


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetDeaths:
int GetDeaths()
`````````````````

Value is stored in PlayerResource.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetDenies:
int GetDenies()
`````````````````

Value is stored in PlayerResource.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetGold:
int GetGold()
`````````````````

Returns gold amount for the player owning this hero


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetGoldBounty:
int GetGoldBounty()
`````````````````

No Description Set


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetHealthRegen:
float GetHealthRegen()
`````````````````

Hero health regen is affected by attributes.


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetIncreasedAttackSpeed:
float GetIncreasedAttackSpeed()
`````````````````

Hero attack speed is also affected by agility.


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetIntellect:
float GetIntellect()
`````````````````

No Description Set


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetIntellectGain:
float GetIntellectGain()
`````````````````

No Description Set


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetKills:
int GetKills()
`````````````````

Value is stored in PlayerResource.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetLastHits:
int GetLastHits()
`````````````````

Value is stored in PlayerResource.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetManaRegen:
float GetManaRegen()
`````````````````

Hero mana regen is affected by attributes.


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetMostRecentDamageTime:
float GetMostRecentDamageTime()
`````````````````

No Description Set


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetMultipleKillCount:
int GetMultipleKillCount()
`````````````````

No Description Set


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetNumAttackers:
int GetNumAttackers()
`````````````````

No Description Set


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetPhysicalArmorValue:
float GetPhysicalArmorValue()
`````````````````

Hero armor is affected by attributes.


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetPlayerID:
int GetPlayerID()
`````````````````

Returns player ID of the player owning this hero


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetPrimaryAttribute:
int GetPrimaryAttribute()
`````````````````

0 = strength, 1 = agility, 2 = intelligence.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetPrimaryStatValue:
float GetPrimaryStatValue()
`````````````````

No Description Set


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetRespawnTime:
float GetRespawnTime()
`````````````````

No Description Set


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetStatsBasedManaRegen:
float GetStatsBasedManaRegen()
`````````````````

Returns only the regen based on Intelligence.


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetStreak:
int GetStreak()
`````````````````

Value is stored in PlayerResource.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetStrength:
float GetStrength()
`````````````````

No Description Set


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetStrengthGain:
float GetStrengthGain()
`````````````````

No Description Set


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC_Hero.GetTimeUntilRespawn:
float GetTimeUntilRespawn()
`````````````````

No Description Set


Returns:
float - No Description Set


 .. _CDOTA_BaseNPC_Hero.HasAnyAvailableInventorySpace:
bool HasAnyAvailableInventorySpace()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC_Hero.HasFlyingVision:
bool HasFlyingVision()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC_Hero.HasOwnerAbandoned:
bool HasOwnerAbandoned()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC_Hero.HasRoomForItem:
int HasRoomForItem(string , bool , bool )
`````````````````

Args: const char* pItemName, ''bool'' bIncludeStashCombines, ''bool'' bAllowSelling


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  bool |  | No Description Set |
|  bool |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_BaseNPC_Hero.HeroLevelUp:
void HeroLevelUp(bool )
`````````````````

Levels up the hero, true or false to play effects.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Hero.IncrementAssists:
void IncrementAssists()
`````````````````

Value is stored in PlayerResource.




 .. _CDOTA_BaseNPC_Hero.IncrementDeaths:
void IncrementDeaths()
`````````````````

Value is stored in PlayerResource.




 .. _CDOTA_BaseNPC_Hero.IncrementDenies:
void IncrementDenies()
`````````````````

Value is stored in PlayerResource.




 .. _CDOTA_BaseNPC_Hero.IncrementKills:
void IncrementKills(int kills)
`````````````````

Passed ID is for the victim, killer ID is ID of the current hero. Value is stored in PlayerResource.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int | kills | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Hero.IncrementLastHitMultikill:
void IncrementLastHitMultikill()
`````````````````

Value is stored in PlayerResource.




 .. _CDOTA_BaseNPC_Hero.IncrementLastHits:
void IncrementLastHits()
`````````````````

Value is stored in PlayerResource.




 .. _CDOTA_BaseNPC_Hero.IncrementLastHitStreak:
void IncrementLastHitStreak()
`````````````````

Value is stored in PlayerResource.




 .. _CDOTA_BaseNPC_Hero.IncrementNearbyCreepDeaths:
void IncrementNearbyCreepDeaths()
`````````````````

Value is stored in PlayerResource.




 .. _CDOTA_BaseNPC_Hero.IncrementStreak:
void IncrementStreak()
`````````````````

Value is stored in PlayerResource.




 .. _CDOTA_BaseNPC_Hero.IsBuybackDisabledByReapersScythe:
bool IsBuybackDisabledByReapersScythe()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC_Hero.IsReincarnating:
bool IsReincarnating()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC_Hero.KilledHero:
void KilledHero(handle , handle )
`````````````````

Args: Hero, Inflictor


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Hero.ModifyAgility:
void ModifyAgility(float )
`````````````````

Adds passed value to base attribute value, then calls CalculateStatBonus.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Hero.ModifyGold:
int ModifyGold(int goldAmmt, bool reliable, int reason)
`````````````````

Gives this hero some gold. Args: ''int'' nGoldChange, ''bool'' bReliable, ''int'' reason


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int | goldAmmt | No Description Set |
|  bool | reliable | No Description Set |
|  int | reason | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CDOTA_BaseNPC_Hero.ModifyIntellect:
void ModifyIntellect(float )
`````````````````

Adds passed value to base attribute value, then calls CalculateStatBonus.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Hero.ModifyStrength:
void ModifyStrength(float )
`````````````````

Adds passed value to base attribute value, then calls CalculateStatBonus.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Hero.PerformTaunt:
void PerformTaunt()
`````````````````

No Description Set




 .. _CDOTA_BaseNPC_Hero.RecordLastHit:
void RecordLastHit()
`````````````````

No Description Set




 .. _CDOTA_BaseNPC_Hero.RespawnHero:
void RespawnHero(bool buyback, bool unknown1, bool unknown2)
`````````````````




+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool | buyback | No Description Set |
|  bool | unknown1 | No Description Set |
|  bool | unknown2 | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Hero.SetAbilityPoints:
void SetAbilityPoints(int )
`````````````````

Sets the current unspent ability point's.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Hero.SetBaseAgility:
void SetBaseAgility(float )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Hero.SetBaseIntellect:
void SetBaseIntellect(float )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Hero.SetBaseStrength:
void SetBaseStrength(float )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Hero.SetBuybackCooldownTime:
void SetBuybackCooldownTime(float )
`````````````````

Sets the buyback cooldown time.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Hero.SetBuyBackDisabledByReapersScythe:
void SetBuyBackDisabledByReapersScythe(bool )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Hero.SetBuybackGoldLimitTime:
void SetBuybackGoldLimitTime(float )
`````````````````

Set the amount of time gold gain is limited after buying back.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Hero.SetCustomDeathXP:
void SetCustomDeathXP(int )
`````````````````

Sets a custom experience value for this hero. {{tip|GameRules boolean must be set for this to work!}}


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Hero.SetGold:
void SetGold(int , bool )
`````````````````

Sets the gold amount for the player owning this hero


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Hero.SetPlayerID:
void SetPlayerID(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Hero.SetRespawnPosition:
void SetRespawnPosition(Vector )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Hero.SetTimeUntilRespawn:
void SetTimeUntilRespawn(float )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Hero.ShouldDoFlyHeightVisual:
bool ShouldDoFlyHeightVisual()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC_Hero.SpendGold:
void SpendGold(int , int )
`````````````````

Args: ''int'' nGold, ''int'' nReason


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Hero.UnitCanRespawn:
bool UnitCanRespawn()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC_Hero.UpgradeAbility:
void UpgradeAbility(handle )
`````````````````

This upgrades the passed ability if it exists and the hero has enough ability point's.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Hero.WillReincarnate:
bool WillReincarnate()
`````````````````

No Description Set


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC_Creature.AddItemDrop:
void AddItemDrop(handle )
`````````````````

Add the specified item drop to this creature


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Creature.CreatureLevelUp:
void CreatureLevelUp(int )
`````````````````

Level the creature up by the specified number of levels


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Creature.IsChampion:
bool IsChampion()
`````````````````

Is this unit a champion?


Returns:
bool - No Description Set


 .. _CDOTA_BaseNPC_Creature.SetArmorGain:
void SetArmorGain(float )
`````````````````

Set the armor gained per level on this creature.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Creature.SetAttackTimeGain:
void SetAttackTimeGain(float )
`````````````````

Set the attack time gained per level on this creature.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Creature.SetBountyGain:
void SetBountyGain(int )
`````````````````

Set the bounty gold gained per level on this creature.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Creature.SetChampion:
void SetChampion(bool )
`````````````````

Flag this unit as a champion creature.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Creature.SetDamageGain:
void SetDamageGain(int )
`````````````````

Set the damage gained per level on this creature.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Creature.SetDisableResistanceGain:
void SetDisableResistanceGain(float )
`````````````````

Set the disable resistance gained per level on this creature.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Creature.SetHPGain:
void SetHPGain(int )
`````````````````

Set the hit point's gained per level on this creature.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Creature.SetHPRegenGain:
void SetHPRegenGain(float )
`````````````````

Set the hit point's regen gained per level on this creature.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Creature.SetMagicResistanceGain:
void SetMagicResistanceGain(float )
`````````````````

Set the magic resistance gained per level on this creature.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Creature.SetManaGain:
void SetManaGain(int )
`````````````````

Set the mana point's gained per level on this creature.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Creature.SetManaRegenGain:
void SetManaRegenGain(float )
`````````````````

Set the mana point's regen gained per level on this creature.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Creature.SetMoveSpeedGain:
void SetMoveSpeedGain(int )
`````````````````

Set the move speed gained per level on this creature.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Creature.SetXPGain:
void SetXPGain(int )
`````````````````

Set the xp reward gained per level on this creature.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTA_BaseNPC_Building.GetInvulnCount:
int GetInvulnCount()
`````````````````

Get the invulnerability count for a building.


Returns:
int - No Description Set


 .. _CDOTA_BaseNPC_Building.SetInvulnCount:
void SetInvulnCount(int )
`````````````````

Set the invulnerability counter of this building.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CRPG_Unit.ActionState:
handle ActionState()
`````````````````

return the ActionState object for this unit.


Returns:
handle - No Description Set


 .. _CRPG_Unit.ClearMovementTarget:
void ClearMovementTarget()
`````````````````

Clear any movement target entity/position.




 .. _CRPG_Unit.FindSensedEnemies:
table FindSensedEnemies()
`````````````````

returns list of all enemy units within this unit's sight cone or sensing sphere


Returns:
table - No Description Set


 .. _CRPG_Unit.GetMaxSpeed:
float GetMaxSpeed()
`````````````````

returns unit's max speed


Returns:
float - No Description Set


 .. _CRPG_Unit.GetMaxStamina:
float GetMaxStamina()
`````````````````

returns maximum stamina amount.


Returns:
float - No Description Set


 .. _CRPG_Unit.GetMovementTargetEntity:
handle GetMovementTargetEntity()
`````````````````

Returs the movement target entity, if set.


Returns:
handle - No Description Set


 .. _CRPG_Unit.GetSensingSphereRange:
float GetSensingSphereRange()
`````````````````

returns range of unit's 360 degree sensing sphere


Returns:
float - No Description Set


 .. _CRPG_Unit.GetSightConeAngle:
float GetSightConeAngle()
`````````````````

returns angle in which the unit can see things up to sight range


Returns:
float - No Description Set


 .. _CRPG_Unit.GetSightConeRange:
float GetSightConeRange()
`````````````````

returns range of unit's sight cone


Returns:
float - No Description Set


 .. _CRPG_Unit.GetStamina:
float GetStamina()
`````````````````

returns current stamina amount.


Returns:
float - No Description Set


 .. _CRPG_Unit.GetTurnRate:
float GetTurnRate()
`````````````````

returns unit's turn rate in degrees per second


Returns:
float - No Description Set


 .. _CRPG_Unit.GetUnitName:
string GetUnitName()
`````````````````

get the unit name for this unit.


Returns:
string - No Description Set


 .. _CRPG_Unit.GrantItem:
void GrantItem(string , bool )
`````````````````

( sItemName ) - grant an item to the unit by name.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CRPG_Unit.IsBlocking:
bool IsBlocking()
`````````````````

is this unit blocking?


Returns:
bool - No Description Set


 .. _CRPG_Unit.IsFacing:
bool IsFacing(Vector , float )
`````````````````

( vecTargetPosition, flAngleTolerance ) - returns true if the unit is within flAngleTolerance degrees of the target position


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _CRPG_Unit.SetBlocking:
void SetBlocking(bool )
`````````````````

( bShouldBlock ) - Set the blocking state of this unit.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CRPG_Unit.SetMaxSpeed:
void SetMaxSpeed(float )
`````````````````

( flMaxSpeed ) - sets unit's max speed


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CRPG_Unit.SetMovementTargetEntity:
void SetMovementTargetEntity(handle , float )
`````````````````

( hTargetEntity, flTargetRange ) - Try to move this unit to the given range from the target entity.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CRPG_Unit.SetMovementTargetPosition:
void SetMovementTargetPosition(Vector , float )
`````````````````

( vecTargetPosition, flTargetRange ) - Try to move this unit to the given range from the target point.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CRPG_Unit.SetSensingSphereRange:
void SetSensingSphereRange(float )
`````````````````

( flSightRange ) - set range of unit's 360 degree sensing sphere


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CRPG_Unit.SetSightConeAngle:
void SetSightConeAngle(float )
`````````````````

( flAngleDegrees ) - sets angle in which the unit can see things up to sight range


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CRPG_Unit.SetSightConeRange:
void SetSightConeRange(float )
`````````````````

( fRange ) - set range of unit's sight cone


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CRPG_Unit.SetTurnRate:
void SetTurnRate(float )
`````````````````

( flTurnRate ) - sets unit's turn rate in degrees per second


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseGameMode.ClientLoadGridNav:
void ClientLoadGridNav()
`````````````````

Tell clients that they need to load gridnav information. Used for things like allowing clients to identify valid locations to place buildings.




 .. _CDOTABaseGameMode.SetAlwaysShowPlayerInventory:
void SetAlwaysShowPlayerInventory(bool )
`````````````````

Show the player hero's inventory in the HUD, regardless of what unit is selected.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseGameMode.SetBotThinkingEnabled:
void SetBotThinkingEnabled(bool )
`````````````````

Enables/Disables bot thinking. Requires a very Dota PvP-like map with 3 lanes, a shop, etc.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseGameMode.SetBuybackEnabled:
void SetBuybackEnabled(bool )
`````````````````

Enables or disables buyback completely


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseGameMode.SetCameraDistanceOverride:
void SetCameraDistanceOverride(float )
`````````````````

Set a different camera distance; dota default is 1134.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseGameMode.SetCustomBuybackCooldownEnabled:
void SetCustomBuybackCooldownEnabled(bool )
`````````````````

Turns on capability to define custom buyback cooldowns.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseGameMode.SetCustomBuybackCostEnabled:
void SetCustomBuybackCostEnabled(bool )
`````````````````

Turns on capability to define custom buyback costs.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseGameMode.SetCustomHeroMaxLevel:
void SetCustomHeroMaxLevel(int maxLevel)
`````````````````

Allows definition of the max level heroes can achieve (default is 25).


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int | maxLevel | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseGameMode.SetCustomXPRequiredToReachNextLevel:
void SetCustomXPRequiredToReachNextLevel(handle )
`````````````````

Allows definition of a ''table'' of hero XP values.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseGameMode.SetFogOfWarDisabled:
void SetFogOfWarDisabled(bool )
`````````````````

Turn the fog of war on or off.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseGameMode.SetGoldSoundDisabled:
void SetGoldSoundDisabled(bool )
`````````````````

Turn the sound when gold is acquired off/on. Takes a ''bool''.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseGameMode.SetOverrideSelectionEntity:
void SetOverrideSelectionEntity(handle unit)
`````````````````

Set an override for the default selection entity, instead of each player's hero.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle | unit | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseGameMode.SetRecommendedItemsDisabled:
void SetRecommendedItemsDisabled(bool )
`````````````````

Turn the panel for showing recommended items at the shop off/on. Takes a ''bool''.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseGameMode.SetRemoveIllusionsOnDeath:
void SetRemoveIllusionsOnDeath(bool )
`````````````````

Make it so illusions are immediately removed upon death, rather than sticking around for a few seconds.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseGameMode.SetTopBarTeamValue:
void SetTopBarTeamValue(int , int )
`````````````````

Set the team values on the top game bar.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseGameMode.SetTopBarTeamValuesOverride:
void SetTopBarTeamValuesOverride(bool )
`````````````````

Override the values of the team values on the top game bar.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseGameMode.SetTopBarTeamValuesVisible:
void SetTopBarTeamValuesVisible(bool )
`````````````````

Turning on/off the team values on the top game bar.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseGameMode.SetTowerBackdoorProtectionEnabled:
void SetTowerBackdoorProtectionEnabled(bool )
`````````````````

Enables/Disables tower backdoor protection


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTABaseGameMode.SetUseCustomHeroLevels:
void SetUseCustomHeroLevels(bool )
`````````````````

Turn on custom-defined XP values for hero level ups. The ''table'' should be defined before switching this on.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDotaQuest.AddSubquest:
void AddSubquest(handle )
`````````````````

Add a subquest to this quest


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDotaQuest.CompleteQuest:
void CompleteQuest()
`````````````````

Mark this quest complete




 .. _CDotaQuest.GetSubquest:
handle GetSubquest(int )
`````````````````

Finds a subquest from this quest by index


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _CDotaQuest.GetSubquestByName:
handle GetSubquestByName(string )
`````````````````

Finds a subquest from this quest by name


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _CDotaQuest.RemoveSubquest:
void RemoveSubquest(handle )
`````````````````

Remove a subquest from this quest


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDotaQuest.SetTextReplaceString:
void SetTextReplaceString(string )
`````````````````

Set the text replace ''string'' for this quest


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDotaQuest.SetTextReplaceValue:
void SetTextReplaceValue(int , int )
`````````````````

Set a quest value


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDotaSubquestBase.CompleteSubquest:
void CompleteSubquest()
`````````````````

Mark this subquest complete




 .. _CDotaSubquestBase.SetTextReplaceString:
void SetTextReplaceString(string )
`````````````````

Set the text replace ''string'' for this subquest


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDotaSubquestBase.SetTextReplaceValue:
void SetTextReplaceValue(int , int )
`````````````````

Set a subquest value


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CPhysicsComponent.ExpensiveInstantRayCast:
bool ExpensiveInstantRayCast(Vector , Vector , handle )
`````````````````

Do an instant (i.e. blocking) Ray Cast. Will do a handle/queue version later. Don't plan to use this for real!


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector |  | No Description Set |
|  Vector |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _CPointTemplate.DeleteCreatedSpawnGroups:
void DeleteCreatedSpawnGroups()
`````````````````

DeleteCreatedSpawnGroups() : Deletes any spawn groups that this point_template has spawned. Note: The point_template will not be deleted by this.




 .. _CPointTemplate.ForceSpawn:
void ForceSpawn()
`````````````````

ForceSpawn() : Spawns all of the entities the point_template is pointing at.




 .. _CPointTemplate.GetSpawnedEntities:
handle GetSpawnedEntities()
`````````````````

GetSpawnedEntities() : Get the list of the most recent spawned entities


Returns:
handle - No Description Set


 .. _CPointTemplate.SetSpawnCallback:
void SetSpawnCallback(handle , handle )
`````````````````

SetSpawnCallback( hCallbackFunc, hCallbackScope, hCallbackData ) : Set a callback for when the template spawns entities. The spawned entities will be passed in as an array.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CBodyComponent.AddImpulseAtPosition:
void AddImpulseAtPosition(Vector , Vector )
`````````````````

Apply an impulse at a worldspace position to the physics


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector |  | No Description Set |
|  Vector |  | No Description Set |
+-----------+--------------+--------------+


 .. _CBodyComponent.AddVelocity:
void AddVelocity(Vector , Vector )
`````````````````

Add linear and angular velocity to the physics object


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector |  | No Description Set |
|  Vector |  | No Description Set |
+-----------+--------------+--------------+


 .. _CBodyComponent.DetachFromParent:
void DetachFromParent()
`````````````````

Detach from its parent




 .. _CBodyComponent.GetSequence:
<> GetSequence()
`````````````````

Returns the active sequence


Returns:
<> - No Description Set


 .. _CBodyComponent.IsAttachedToParent:
bool IsAttachedToParent()
`````````````````

Is attached to parent


Returns:
bool - No Description Set


 .. _CBodyComponent.LookupSequence:
<> LookupSequence(string )
`````````````````

Returns a sequence id given a name


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+
Returns:
<> - No Description Set


 .. _CBodyComponent.SequenceDuration:
float SequenceDuration(string )
`````````````````

Returns the duration in seconds of the specified sequence


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+
Returns:
float - No Description Set


 .. _CBodyComponent.SetAngularVelocity:
void SetAngularVelocity(Vector )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector |  | No Description Set |
+-----------+--------------+--------------+


 .. _CBodyComponent.SetAnimation:
void SetAnimation(string )
`````````````````

Pass ''string'' for the animation to play on this model


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _CBodyComponent.SetBodyGroup:
void SetBodyGroup(string )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _CBodyComponent.SetMaterialGroup:
void SetMaterialGroup(utlstringtoken )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  utlstringtoken |  | No Description Set |
+-----------+--------------+--------------+


 .. _CBodyComponent.SetVelocity:
void SetVelocity(Vector velocity)
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector | velocity | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseAnimating.GetAttachmentAngles:
Vector GetAttachmentAngles(int )
`````````````````

Get the attachement id's angles as a p,y,r ''vector''


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
Vector - No Description Set


 .. _CBaseAnimating.GetAttachmentOrigin:
Vector GetAttachmentOrigin(int )
`````````````````

Get the attachement id's origin ''vector''


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
Vector - No Description Set


 .. _CBaseAnimating.IsSequenceFinished:
bool IsSequenceFinished()
`````````````````

Ask whether the main sequence is done playing


Returns:
bool - No Description Set


 .. _CBaseAnimating.ScriptLookupAttachment:
int ScriptLookupAttachment(string )
`````````````````

Get the named attachment id


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CBaseAnimating.SetBodygroup:
void SetBodygroup(int , int )
`````````````````

Sets a bodygroup


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseAnimating.SetModelScale:
void SetModelScale(float scale)
`````````````````

Sets the model's scale to <i>scale</i>, <br/>so if a unit had its model scale at 1, and you use <i>SetModelScale(<b>10.0</b>)</i>, it would set the scale to <b>10.0</b>.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float | scale | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseAnimating.SetPoseParameter:
float SetPoseParameter(string , float )
`````````````````

Set the specified pose parameter to the specified value


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+
Returns:
float - No Description Set


 .. _CBaseCombatCharacter.GetEquippedWeapons:
table GetEquippedWeapons()
`````````````````

GetEquippedWeapons() : Returns an array of all the equipped weapons


Returns:
table - No Description Set


 .. _CBaseCombatCharacter.GetWeaponCount:
int GetWeaponCount()
`````````````````

GetWeaponCount() : Gets the number of weapons currently equipped


Returns:
int - No Description Set


 .. _ProjectileManager.CreateLinearProjectile:
int CreateLinearProjectile(handle )
`````````````````

Creates a linear projectile and returns the projectile ID


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _ProjectileManager.CreateTrackingProjectile:
void CreateTrackingProjectile(handle )
`````````````````

Creates a tracking projectile


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _ProjectileManager.DestroyLinearProjectile:
void DestroyLinearProjectile(int )
`````````````````

Destroys the linear projectile matching the argument ID


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _ProjectileManager.ProjectileDodge:
void ProjectileDodge(handle )
`````````````````

Makes the specified unit dodge projectiles


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CBaseTrigger.Disable:
void Disable()
`````````````````

Disable the trigger




 .. _CBaseTrigger.Enable:
void Enable()
`````````````````

Enable the trigger




 .. _CBaseTrigger.IsTouching:
bool IsTouching(handle )
`````````````````

Checks whether the passed entity is touching the trigger.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _CEnvEntityMaker.SpawnEntity:
void SpawnEntity()
`````````````````

Create an entity at the location of the maker




 .. _CEnvEntityMaker.SpawnEntityAtEntityOrigin:
void SpawnEntityAtEntityOrigin(handle )
`````````````````

Create an entity at the location of a specified entity instance


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CEnvEntityMaker.SpawnEntityAtLocation:
void SpawnEntityAtLocation(Vector , Vector )
`````````````````

Create an entity at a specified location and orientaton, orientation is Euler angle in degrees (pitch, yaw, roll)


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector |  | No Description Set |
|  Vector |  | No Description Set |
+-----------+--------------+--------------+


 .. _CEnvEntityMaker.SpawnEntityAtNamedEntityOrigin:
void SpawnEntityAtNamedEntityOrigin(string )
`````````````````

Create an entity at the location of a named entity


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTAVoteSystem.StartVote:
void StartVote(handle )
`````````````````

Starts a vote, based upon a ''table'' of parameters


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _CMarkupVolumeTagged.HasTag:
bool HasTag(string )
`````````````````

Does this volume have the given tag.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _CScriptPrecacheContext.AddResource:
void AddResource(string )
`````````````````

Precaches a specific resource


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _CScriptPrecacheContext.GetValue:
table GetValue(string )
`````````````````

Reads a spawn key


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+
Returns:
table - No Description Set


 .. _CScriptKeyValues.GetValue:
table GetValue(string )
`````````````````

Reads a spawn key


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+
Returns:
table - No Description Set


 .. _CScriptParticleManager.CreateParticle:
int CreateParticle(string particleName, int particleAttach, handle owningEntity)
`````````````````

Creates a new particle effect


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string | particleName | No Description Set |
|  int | particleAttach | No Description Set |
|  handle | owningEntity | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CScriptParticleManager.CreateParticleForPlayer:
int CreateParticleForPlayer(string particleName, int particleAttach, handle owningEntity, handle owningPlayer)
`````````````````

Creates a new particle effect that only plays for the specified player


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string | particleName | No Description Set |
|  int | particleAttach | No Description Set |
|  handle | owningEntity | No Description Set |
|  handle | owningPlayer | No Description Set |
+-----------+--------------+--------------+
Returns:
int - Particle ID


 .. _CScriptParticleManager.GetParticleReplacement:
string GetParticleReplacement(string , handle )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+
Returns:
string - No Description Set


 .. _CScriptParticleManager.ReleaseParticleIndex:
void ReleaseParticleIndex(int particleId)
`````````````````

Frees the specified particle index


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int | particleId | No Description Set |
+-----------+--------------+--------------+


 .. _CScriptParticleManager.SetParticleAlwaysSimulate:
void SetParticleAlwaysSimulate(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CScriptParticleManager.SetParticleControl:
void SetParticleControl(int particleId, int controlIndex, Vector controlData)
`````````````````

Set the control point data for a control on a particle effect


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int | particleId | No Description Set |
|  int | controlIndex | No Description Set |
|  Vector | controlData | No Description Set |
+-----------+--------------+--------------+


 .. _CScriptParticleManager.SetParticleControlEnt:
void SetParticleControlEnt(int , int , handle , int , string , Vector , bool )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
|  int |  | No Description Set |
|  handle |  | No Description Set |
|  int |  | No Description Set |
|  string |  | No Description Set |
|  Vector |  | No Description Set |
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CScriptHeroList.GetAllHeroes:
table GetAllHeroes()
`````````````````

Returns all the heroes in the world


Returns:
table - No Description Set


 .. _CScriptHeroList.GetHero:
handle GetHero(int heroId)
`````````````````

Get the Nth hero in the Hero List


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int | heroId | A value between 0 and 9 |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _CScriptHeroList.GetHeroCount:
int GetHeroCount()
`````````````````

Returns the number of heroes in the world


Returns:
int - No Description Set


 .. _CNativeOutputs.AddOutput:
void AddOutput(string , string )
`````````````````

Add an output


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  string |  | No Description Set |
+-----------+--------------+--------------+


 .. _CNativeOutputs.Init:
void Init(int )
`````````````````

Initialize with number of outputs


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CEnvProjectedTexture.SetFarRange:
void SetFarRange(float )
`````````````````

Set light maximum range


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CEnvProjectedTexture.SetLinearAttenuation:
void SetLinearAttenuation(float )
`````````````````

Set light linear attenuation value


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CEnvProjectedTexture.SetNearRange:
void SetNearRange(float )
`````````````````

Set light minimum range


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CEnvProjectedTexture.SetQuadraticAttenuation:
void SetQuadraticAttenuation(float )
`````````````````

Set light quadratic attenuation value


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CEnvProjectedTexture.SetVolumetrics:
void SetVolumetrics(bool , float , float , int , float )
`````````````````

Turn on/off light volumetrics: ''bool'' bOn, ''float'' flIntensity, ''float'' flNoise, ''int'' nPlanes, ''float'' flPlaneOffset


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
|  float |  | No Description Set |
|  float |  | No Description Set |
|  int |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CInfoData.QueryColor:
Vector QueryColor(utlstringtoken , Vector )
`````````````````

Query color data for this key


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  utlstringtoken |  | No Description Set |
|  Vector |  | No Description Set |
+-----------+--------------+--------------+
Returns:
Vector - No Description Set


 .. _CInfoData.QueryFloat:
float QueryFloat(utlstringtoken , float )
`````````````````

Query ''float'' data for this key


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  utlstringtoken |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+
Returns:
float - No Description Set


 .. _CInfoData.QueryInt:
int QueryInt(utlstringtoken , int )
`````````````````

Query ''int'' data for this key


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  utlstringtoken |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _CInfoData.QueryNumber:
float QueryNumber(utlstringtoken , float )
`````````````````

Query number data for this key


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  utlstringtoken |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+
Returns:
float - No Description Set


 .. _CInfoData.QueryString:
string QueryString(utlstringtoken , string )
`````````````````

Query ''string'' data for this key


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  utlstringtoken |  | No Description Set |
|  string |  | No Description Set |
+-----------+--------------+--------------+
Returns:
string - No Description Set


 .. _CInfoData.QueryVector:
Vector QueryVector(utlstringtoken , Vector )
`````````````````

Query ''vector'' data for this key


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  utlstringtoken |  | No Description Set |
|  Vector |  | No Description Set |
+-----------+--------------+--------------+
Returns:
Vector - No Description Set


 .. _CPhysicsProp.DisableMotion:
void DisableMotion()
`````````````````

Enable motion for the prop




 .. _CPhysicsProp.EnableMotion:
void EnableMotion()
`````````````````

Enable motion for the prop




 .. _CDOTAGamerules.Defeated:
void Defeated()
`````````````````

Kills the ancient, etc.




 .. _CDOTAGamerules.DidMatchSignoutTimeOut:
bool DidMatchSignoutTimeOut()
`````````````````

true when we have waited some time after end of the game and not received signout


Returns:
bool - No Description Set


 .. _CDOTAGamerules.GetCustomGameDifficulty:
int GetCustomGameDifficulty()
`````````````````

Returns the difficulty level of the custom game mode


Returns:
int - No Description Set


 .. _CDOTAGamerules.GetDifficulty:
int GetDifficulty()
`````````````````

Returns difficulty level of the custom game mode


Returns:
int - No Description Set


 .. _CDOTAGamerules.GetDroppedItem:
handle GetDroppedItem(int dropIndex)
`````````````````

Gets the Xth dropped item


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int | dropIndex | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _CDOTAGamerules.GetGameModeEntity:
handle GetGameModeEntity()
`````````````````

Get the game mode entity


Returns:
handle - No Description Set


 .. _CDOTAGamerules.GetGameTime:
float GetGameTime()
`````````````````

Returns the number of seconds elapsed since map start. This time doesn't count up when the game is paused


Returns:
float - No Description Set


 .. _CDOTAGamerules.GetMatchSignoutComplete:
bool GetMatchSignoutComplete()
`````````````````

Have we received the post match signout message that includes reward information


Returns:
bool - No Description Set


 .. _CDOTAGamerules.GetNianFightStartTime:
float GetNianFightStartTime()
`````````````````

Gets the start time for the Nian fight


Returns:
float - No Description Set


 .. _CDOTAGamerules.GetNianTotalDamageTaken:
int GetNianTotalDamageTaken()
`````````````````

For New Bloom, get total damage taken by the Nian / Year Beast


Returns:
int - No Description Set


 .. _CDOTAGamerules.GetTimeOfDay:
float GetTimeOfDay()
`````````````````

Get the time of day


Returns:
float - No Description Set


 .. _CDOTAGamerules.IsDaytime:
bool IsDaytime()
`````````````````

Is it day time.


Returns:
bool - No Description Set


 .. _CDOTAGamerules.MakeTeamLose:
void MakeTeamLose(int team)
`````````````````

Makes ths specified team lose


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int | team | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTAGamerules.NumDroppedItems:
int NumDroppedItems()
`````````````````

Returns the number of items currently dropped on the ground


Returns:
int - No Description Set


 .. _CDOTAGamerules.Playtesting_UpdateAddOnKeyValues:
void Playtesting_UpdateAddOnKeyValues()
`````````````````

Updates custom hero, unit and ability KeyValues in memory with the latest values from disk




 .. _CDOTAGamerules.ResetDefeated:
void ResetDefeated()
`````````````````

Restart after killing the ancient, etc.




 .. _CDOTAGamerules.ResetToHeroSelection:
void ResetToHeroSelection()
`````````````````

Restart the game at hero selection




 .. _CDOTAGamerules.SendCustomMessage:
void SendCustomMessage(string message, int teamID, int unknown(1?))
`````````````````

Displays a line of text in the left textbox (where usually deaths/denies/buysbacks are announced). This function takes restricted HTML as input! (&lt;br&gt;,&lt;u&gt;,&lt;font&gt;)


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string | message | No Description Set |
|  int | teamID | No Description Set |
|  int | unknown(1?) | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTAGamerules.SetCreepMinimapIconScale:
void SetCreepMinimapIconScale(float scale)
`````````````````

Scale the creep icons on the minimap.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float | scale | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTAGamerules.SetCustomGameDifficulty:
void SetCustomGameDifficulty(int )
`````````````````

Set the difficulty level of the custom game mode


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTAGamerules.SetFirstBloodActive:
void SetFirstBloodActive(bool )
`````````````````

Sets whether First Blood has been triggered.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTAGamerules.SetGameWinner:
void SetGameWinner(int team)
`````````````````

Makes ths specified team win


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int | team | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTAGamerules.SetGoldPerTick:
void SetGoldPerTick(int )
`````````````````

Set the auto gold increase per timed interval.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTAGamerules.SetGoldTickTime:
void SetGoldTickTime(float )
`````````````````

Set the time ''int''erval between auto gold increases.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTAGamerules.SetHeroMinimapIconSize:
void SetHeroMinimapIconSize(int iconSize)
`````````````````

(nMinimapHeroIconSize) - Set the hero minimap icon size.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int | iconSize | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTAGamerules.SetHeroRespawnEnabled:
void SetHeroRespawnEnabled(bool canRespawn)
`````````````````

Control if the normal DOTA hero respawn rules apply.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool | canRespawn | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTAGamerules.SetHeroSelectionTime:
void SetHeroSelectionTime(float time)
`````````````````

Sets the amount of time players have to pick their hero.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float | time | Time In Seconds |
+-----------+--------------+--------------+


 .. _CDOTAGamerules.SetNianFightStartTime:
void SetNianFightStartTime(float )
`````````````````

Sets the start time for the Nian fight


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTAGamerules.SetOverlayHealthBarUnit:
void SetOverlayHealthBarUnit(handle unit, int style)
`````````````````

Show this unit's health on the overlay health bar


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle | unit | No Description Set |
|  int | style | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTAGamerules.SetPostGameTime:
void SetPostGameTime(float time)
`````````````````

Sets the amount of time players have between the game ending and the server disconnecting them.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float | time | Time in Seconds |
+-----------+--------------+--------------+


 .. _CDOTAGamerules.SetPreGameTime:
void SetPreGameTime(float time)
`````````````````

Sets the amount of time players have between picking their hero and game start.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float | time | Time In Seconds |
+-----------+--------------+--------------+


 .. _CDOTAGamerules.SetRuneMinimapIconScale:
void SetRuneMinimapIconScale(float scale)
`````````````````

Scale the rune icons on the minimap.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float | scale | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTAGamerules.SetRuneSpawnTime:
void SetRuneSpawnTime(float time)
`````````````````

Sets the amount of time between rune spawns.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float | time | Time in seconds |
+-----------+--------------+--------------+


 .. _CDOTAGamerules.SetSafeToLeave:
void SetSafeToLeave(bool safeToLeave)
`````````````````

Mark this game as safe to leave.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool | safeToLeave | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTAGamerules.SetSameHeroSelectionEnabled:
void SetSameHeroSelectionEnabled(bool enabled)
`````````````````

When true, players can repeatedly pick the same hero.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool | enabled | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTAGamerules.SetTimeOfDay:
void SetTimeOfDay(float time)
`````````````````

Set the time of day.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float | time | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTAGamerules.SetTreeRegrowTime:
void SetTreeRegrowTime(float time)
`````````````````

Sets the tree regrow time in seconds.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float | time | Time in Seconds |
+-----------+--------------+--------------+


 .. _CDOTAGamerules.SetUseBaseGoldBountyOnHeroes:
void SetUseBaseGoldBountyOnHeroes(bool )
`````````````````

Heroes will use the basic NPC functionality for determining their bounty, rather than DOTA specific formulas.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTAGamerules.SetUseCustomHeroXPValues:
void SetUseCustomHeroXPValues(bool )
`````````````````

Allows heroes in the map to give a specific amount of XP (this value must be set).


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTAGamerules.SetUseUniversalShopMode:
void SetUseUniversalShopMode(bool enabled)
`````````````````

When true, all items are available at as long as any shop is in range, including Secret Shop items


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool | enabled | No Description Set |
+-----------+--------------+--------------+


 .. _CDOTAGamerules.State_Get:
<> State_Get()
`````````````````

Get the current Gamerules state


Returns:
<> - No Description Set


 .. _CToneMapControllerComponent.GetBloomScale:
float GetBloomScale()
`````````````````

Gets bloomscale for this tonemap controller


Returns:
float - No Description Set


 .. _CToneMapControllerComponent.GetMaxExposure:
float GetMaxExposure()
`````````````````

Gets max exposure for this tonemap controller


Returns:
float - No Description Set


 .. _CToneMapControllerComponent.GetMinExposure:
float GetMinExposure()
`````````````````

Gets min exposure for this tonemap controller


Returns:
float - No Description Set


 .. _CToneMapControllerComponent.SetBloomScale:
void SetBloomScale(float )
`````````````````

Sets bloom scale for this tonemap controller


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CToneMapControllerComponent.SetMaxExposure:
void SetMaxExposure(float )
`````````````````

Sets max exposure for this tonemap controller


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CToneMapControllerComponent.SetMinExposure:
void SetMinExposure(float )
`````````````````

Sets min exposure for this tonemap controller


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDebugOverlayScriptHelper.Axis:
void Axis(Vector , Quaternion , float , bool , float )
`````````````````

Draws an axis. Specify origin + orientation in world space.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector |  | No Description Set |
|  Quaternion |  | No Description Set |
|  float |  | No Description Set |
|  bool |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDebugOverlayScriptHelper.Box:
void Box(Vector , Vector , int , int , int , int , bool , float )
`````````````````

Draws a world-space axis-aligned box. Specify bounds in world space.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
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
void BoxAngles(Vector , Vector , Vector , Quaternion , int , int , int , int , bool , float )
`````````````````

Draws an oriented box at the origin. Specify bounds in local space.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
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
void Capsule(Vector , Quaternion , float , float , int , int , int , int , bool , float )
`````````````````

Draws a capsule. Specify base in world space.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
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
void Circle(Vector , Quaternion , float , int , int , int , int , bool , float )
`````````````````

Draws a circle. Specify center in world space.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
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
void CircleScreenOriented(Vector , float , int , int , int , int , bool , float )
`````````````````

Draws a circle oriented to the screen. Specify center in world space.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
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
void Cone(Vector , Vector , float , float , int , int , int , int , bool , float )
`````````````````

Draws a wireframe cone. Specify endpoint and direction in world space.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
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
void Cross(Vector , float , int , int , int , int , bool , float )
`````````````````

Draws a screen-aligned cross. Specify origin in world space.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
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
void Cross3D(Vector , float , int , int , int , int , bool , float )
`````````````````

Draws a world-aligned cross. Specify origin in world space.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
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
void Cross3DOriented(Vector , Quaternion , float , int , int , int , int , bool , float )
`````````````````

Draws an oriented cross. Specify origin in world space.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
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
void DrawTickMarkedLine(Vector , Vector , float , int , int , int , int , int , bool , float )
`````````````````

Draws a dashed line. Specify endpoint's in world space.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
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
void EntityAttachments(ehandle , float )
`````````````````

Draws the attachments of the entity


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  ehandle |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDebugOverlayScriptHelper.EntityAxis:
void EntityAxis(ehandle , float , bool , float )
`````````````````

Draws the axis of the entity origin


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  ehandle |  | No Description Set |
|  float |  | No Description Set |
|  bool |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDebugOverlayScriptHelper.EntityBounds:
void EntityBounds(ehandle , int , int , int , int , bool , float )
`````````````````

Draws bounds of an entity


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  ehandle |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  bool |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDebugOverlayScriptHelper.EntitySkeleton:
void EntitySkeleton(ehandle , float )
`````````````````

Draws the skeleton of the entity


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  ehandle |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDebugOverlayScriptHelper.EntityText:
void EntityText(ehandle , int , string , int , int , int , int , float )
`````````````````

Draws text on an entity


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
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
void FilledRect2D(Vector2D , Vector2D , int , int , int , int , float )
`````````````````

Draws a screen-space filled 2D rectangle. Coordinates are in pixels.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector2D |  | No Description Set |
|  Vector2D |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDebugOverlayScriptHelper.HorzArrow:
void HorzArrow(Vector , Vector , float , int , int , int , int , bool , float )
`````````````````

Draws a horizontal arrow. Specify endpoint's in world space.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
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
void Line(Vector , Vector , int , int , int , int , bool , float )
`````````````````

Draws a line between two point's


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
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
void Line2D(Vector2D , Vector2D , int , int , int , int , float )
`````````````````

Draws a line between two point's in screenspace


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector2D |  | No Description Set |
|  Vector2D |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  int |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDebugOverlayScriptHelper.PopDebugOverlayScope:
void PopDebugOverlayScope()
`````````````````

Pops the identifier used to group overlays. Overlays marked with this identifier can be deleted in a big batch.




 .. _CDebugOverlayScriptHelper.PushAndClearDebugOverlayScope:
void PushAndClearDebugOverlayScope(utlstringtoken )
`````````````````

Pushes an identifier used to group overlays. Deletes all existing overlays using this overlay id.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  utlstringtoken |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDebugOverlayScriptHelper.PushDebugOverlayScope:
void PushDebugOverlayScope(utlstringtoken )
`````````````````

Pushes an identifier used to group overlays. Overlays marked with this identifier can be deleted in a big batch.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  utlstringtoken |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDebugOverlayScriptHelper.RemoveAllInScope:
void RemoveAllInScope(utlstringtoken )
`````````````````

Removes all overlays marked with a specific identifier, regardless of their lifetime.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  utlstringtoken |  | No Description Set |
+-----------+--------------+--------------+


 .. _CDebugOverlayScriptHelper.SolidCone:
void SolidCone(Vector , Vector , float , float , int , int , int , int , bool , float )
`````````````````

Draws a solid cone. Specify endpoint and direction in world space.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
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
void Sphere(Vector , float , int , int , int , int , bool , float )
`````````````````

Draws a wireframe sphere. Specify center in world space.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
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
void SweptBox(Vector , Vector , Vector , Vector , Quaternion , int , int , int , int , float )
`````````````````

Draws a swept box. Specify endpoint's in world space and the bounds in local space.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
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
void Text(Vector , int , string , float , int , int , int , int , float )
`````````````````

Draws 2D text. Specify origin in world space.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
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
void Texture(string , Vector2D , Vector2D , int , int , int , int , Vector2D , Vector2D , float )
`````````````````

Draws a screen-space texture. Coordinates are in pixels.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
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
void Triangle(Vector , Vector , Vector , int , int , int , int , bool , float )
`````````````````

Draws a filled triangle. Specify vertices in world space.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
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
void UnitTestCycleOverlayRenderType()
`````````````````

Toggles the overlay render type, for unit tests




 .. _CDebugOverlayScriptHelper.VectorText3D:
void VectorText3D(Vector , Quaternion , string , int , int , int , int , bool , float )
`````````````````

Draws 3D text. Specify origin + orientation in world space.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
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
void VertArrow(Vector , Vector , float , int , int , int , int , bool , float )
`````````````````

Draws a vertical arrow. Specify endpoint's in world space.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
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
void YawArrow(Vector , float , float , float , int , int , int , int , bool , float )
`````````````````

Draws a arrow associated with a specific yaw. Specify endpoint's in world space.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
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
handle GetCurrentScene()
`````````````````

Returns the instance of the oldest active scene entity '''(if any).


Returns:
handle - No Description Set


 .. _CBaseFlex.GetSceneByIndex:
handle GetSceneByIndex(int )
`````````````````

Returns the instance of the scene entity at the specified index.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _CSceneEntity.AddBroadcastTeamTarget:
void AddBroadcastTeamTarget(int )
`````````````````

Adds a team (by index) to the broadcast list


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CSceneEntity.Cancel:
void Cancel()
`````````````````

Cancel scene playback




 .. _CSceneEntity.EstimateLength:
float EstimateLength()
`````````````````

Returns length of this scene in seconds.


Returns:
float - No Description Set


 .. _CSceneEntity.FindCamera:
handle FindCamera()
`````````````````

Get the camera


Returns:
handle - No Description Set


 .. _CSceneEntity.FindNamedEntity:
handle FindNamedEntity(string )
`````````````````

given an entity reference, such as !target, get actual entity from scene object


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+
Returns:
handle - No Description Set


 .. _CSceneEntity.IsPaused:
bool IsPaused()
`````````````````

If this scene is currently paused.


Returns:
bool - No Description Set


 .. _CSceneEntity.IsPlayingBack:
bool IsPlayingBack()
`````````````````

If this scene is currently playing.


Returns:
bool - No Description Set


 .. _CSceneEntity.LoadSceneFromString:
bool LoadSceneFromString(string , string )
`````````````````

given a dummy scene name and a vcd ''string'', load the scene


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  string |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _CSceneEntity.RemoveBroadcastTeamTarget:
void RemoveBroadcastTeamTarget(int )
`````````````````

Removes a team (by index) from the broadcast list


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _CSceneEntity.Start:
void Start(handle )
`````````````````

Start scene playback, takes activatorEntity as param


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


 .. _GridNav.GridPosToWorldCenterX:
float GridPosToWorldCenterX(int )
`````````````````

Get the X position of the center of a given X index


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
float - No Description Set


 .. _GridNav.GridPosToWorldCenterY:
float GridPosToWorldCenterY(int )
`````````````````

Get the Y position of the center of a given Y index


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+
Returns:
float - No Description Set


 .. _GridNav.IsBlocked:
bool IsBlocked(Vector )
`````````````````

Checks whether the given position is blocked


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _GridNav.IsNearbyTree:
bool IsNearbyTree(Vector position, float radius, bool )
`````````````````

 


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector | position | No Description Set |
|  float | radius | No Description Set |
|  bool |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _GridNav.IsTraversable:
bool IsTraversable(Vector )
`````````````````

Checks whether the given position is traversable


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector |  | No Description Set |
+-----------+--------------+--------------+
Returns:
bool - No Description Set


 .. _GridNav.RegrowAllTrees:
void RegrowAllTrees()
`````````````````

 




 .. _GridNav.WorldToGridPosX:
int WorldToGridPosX(float )
`````````````````

Get the X index of a given world X position


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _GridNav.WorldToGridPosY:
int WorldToGridPosY(float )
`````````````````

Get the Y index of a given world Y position


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+
Returns:
int - No Description Set


 .. _Convars.GetBool:
table GetBool(string variableName)
`````````````````

GetBool(name) : returns the convar as a boolean flag.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string | variableName | No Description Set |
+-----------+--------------+--------------+
Returns:
table - No Description Set


 .. _Convars.GetCommandClient:
handle GetCommandClient()
`````````````````

GetCommandClient() : returns the player who issued this console command.


Returns:
handle - No Description Set


 .. _Convars.GetDOTACommandClient:
handle GetDOTACommandClient()
`````````````````

GetDOTACommandClient() : returns the DOTA player who issued this console command.


Returns:
handle - No Description Set


 .. _Convars.GetFloat:
table GetFloat(string name)
`````````````````

GetFloat(name) : returns the convar as a ''float''. May return ''nil'' if no such convar.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string | name | No Description Set |
+-----------+--------------+--------------+
Returns:
table - No Description Set


 .. _Convars.GetInt:
table GetInt(string )
`````````````````

GetInt(name) : returns the convar as an ''int''. May return ''nil'' if no such convar.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+
Returns:
table - No Description Set


 .. _Convars.GetStr:
table GetStr(string variableName)
`````````````````

GetStr(name) : returns the convar as a ''string''. May return ''nil'' if no such convar.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string | variableName | No Description Set |
+-----------+--------------+--------------+
Returns:
table - No Description Set


 .. _Convars.RegisterCommand:
void RegisterCommand(string variableName, handle function, string helpText, int flags)
`````````````````

RegisterCommand(name, fn, helpString, flags) : register a console command.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string | variableName | No Description Set |
|  handle | function | A lua function to call when this concommand is run |
|  string | helpText | No Description Set |
|  int | flags | FCVAR flags |
+-----------+--------------+--------------+


 .. _Convars.RegisterConvar:
void RegisterConvar(string name, string defaultValue, string helpText, int flags)
`````````````````

RegisterConvar(name, defaultValue, helpString, flags): register a new console variable.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string | name | No Description Set |
|  string | defaultValue | No Description Set |
|  string | helpText | No Description Set |
|  int | flags | FCVAR flags |
+-----------+--------------+--------------+


 .. _Convars.SetBool:
void SetBool(string variableName, bool value)
`````````````````

SetBool(name, val) : sets the value of the convar to the ''bool''.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string | variableName | No Description Set |
|  bool | value | No Description Set |
+-----------+--------------+--------------+


 .. _Convars.SetFloat:
void SetFloat(string variableName, float value)
`````````````````

SetFloat(name, val) : sets the value of the convar to the ''float''.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string | variableName | No Description Set |
|  float | value | No Description Set |
+-----------+--------------+--------------+


 .. _Convars.SetInt:
void SetInt(string , int )
`````````````````

SetInt(name, val) : sets the value of the convar to the ''int''.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+


 .. _Convars.SetStr:
void SetStr(string , string )
`````````````````

SetStr(name, val) : sets the value of the convar to the ''string''.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  string |  | No Description Set |
+-----------+--------------+--------------+


