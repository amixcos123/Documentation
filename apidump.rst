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


void AppendToLogFile(string , string )
`````````````````

Appends a ''string'' to a log file on the server


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  string |  | No Description Set |
+-----------+--------------+--------------+


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


void CancelEntityIOEvents(ehandle )
`````````````````

Create all I/O events for a particular entity


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  ehandle |  | No Description Set |
+-----------+--------------+--------------+


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


void DebugBreak()
`````````````````

Breaks in the debugger




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


void DebugDrawClear()
`````````````````

Try to clear all the debug overlay info




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


void DoScriptAssert(bool , string )
`````````````````

ScriptAssert:Asserts the passed in value. Prints out a message and brings up the assert dialog.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
|  string |  | No Description Set |
+-----------+--------------+--------------+


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


void EmitGlobalSound(string )
`````````````````

Play named sound for all players


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+


void EmitSoundOn(string , handle )
`````````````````

Play named sound on Entity


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


void EmitSoundOnClient(string , handle )
`````````````````

Play named sound only on the client for the passed in player


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


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


void FireEntityIOInputNameOnly(ehandle , string )
`````````````````

Fire Entity's Action Input w/no data


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  ehandle |  | No Description Set |
|  string |  | No Description Set |
+-----------+--------------+--------------+


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


void FireGameEvent(string eventName, handle parameterTable)
`````````````````

Fire a pre-defined event, which can be found either in custom_events.txt or in dota's resource/*.res


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string | eventName | No Description Set |
|  handle | parameterTable | No Description Set |
+-----------+--------------+--------------+


void FireGameEventLocal(string , handle )
`````````````````

Fire a game event without broadcasting to the client.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


float FrameTime()
`````````````````

Get the time spent on the server in the last frame


Returns:
float - No Description Set


int GetFrameCount()
`````````````````

Returns the engines current frame count


Returns:
int - No Description Set


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


handle GetListenServerHost()
`````````````````

Get the local player on a listen server.


Returns:
handle - No Description Set


string GetMapName()
`````````````````

Get the name of the map.


Returns:
string - No Description Set


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


string GetSystemDate()
`````````````````

Get the current real world date


Returns:
string - No Description Set


string GetSystemTime()
`````````````````

Get the current real world time


Returns:
string - No Description Set


float GetWorldMaxX()
`````````````````

Gets the world's maximum X position.


Returns:
float - No Description Set


float GetWorldMaxY()
`````````````````

Gets the world's maximum Y position.


Returns:
float - No Description Set


float GetWorldMinX()
`````````````````

Gets the world's minimum X position.


Returns:
float - No Description Set


float GetWorldMinY()
`````````````````

Gets the world's minimum Y position.


Returns:
float - No Description Set


void InitLogFile(string , string )
`````````````````

If the given file doesn't exist, creates it with the given contents; does nothing if it exists


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  string |  | No Description Set |
+-----------+--------------+--------------+


bool IsDedicatedServer()
`````````````````

Returns true if this server is a dedicated server.


Returns:
bool - No Description Set


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


void Msg(string )
`````````````````

Print a message


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+


void PauseGame(bool )
`````````````````

Pause or unpause the game.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


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


void PrecacheEntityListFromTable(handle , handle )
`````````````````

Precache a list of entity KeyValues table's


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


void PrecacheItemByNameAsync(string , handle )
`````````````````

Asynchronously precaches a DOTA item by its dota_npc_items.txt name, provides a callback when it's finished.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


void PrecacheItemByNameSync(string , handle )
`````````````````

Precaches a DOTA item by its dota_npc_items.txt name


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


void PrecacheModel(string , handle )
`````````````````

( modelName, context ) - Manually precache a single model


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


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


void PrecacheUnitByNameAsync(string , handle )
`````````````````

Asynchronously precaches a DOTA unit by its dota_npc_units.txt name, provides a callback when it's finished.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


void PrecacheUnitByNameSync(string , handle )
`````````````````

Precaches a DOTA unit by its dota_npc_units.txt name


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


void PrintLinkedConsoleMessage(string , string )
`````````````````

Print a console message with a linked console command


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  string |  | No Description Set |
+-----------+--------------+--------------+


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


void RegisterSpawnGroupFilterProxy(string )
`````````````````

Create a C proxy for a script-based spawn group filter


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+


void ReloadMOTD()
`````````````````

Reloads the MotD file




void RemoveSpawnGroupFilterProxy(string )
`````````````````

Remove the C proxy for a script-based spawn group filter


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+


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


handle rr_GetResponseTargets()
`````````````````

Retrieve a ''table'' of all available expresser targets, in the form { name : ''handle'', name: ''handle'' }.


Returns:
handle - No Description Set


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


void SendFrostivusTimeElapsedToGC()
`````````````````

No Description Set




void SendFrostyPointsMessageToGC(handle )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


void SendToConsole(string )
`````````````````

Send a ''string'' to the console as a client command


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+


void SendToServerConsole(string )
`````````````````

Send a ''string'' to the console as a server command


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+


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


void SetQuestName(string )
`````````````````

Set the current quest name.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+


void SetQuestPhase(int )
`````````````````

Set the current quest phase.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


void SetRenderingEnabled(ehandle , bool )
`````````````````

Set rendering on/off for an ''ehandle''


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  ehandle |  | No Description Set |
|  bool |  | No Description Set |
+-----------+--------------+--------------+


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


void ShowMessage(string )
`````````````````

Print a hud message on all clients


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+


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


void StartSoundEvent(string , handle )
`````````````````

Start a sound event


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


void StopEffect(handle , string )
`````````````````

(hEntity, szEffectName)


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
|  string |  | No Description Set |
+-----------+--------------+--------------+


void StopListeningToAllGameEvents(handle )
`````````````````

Stop listening to all game events within a specific context.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


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


void StopSoundEvent(string , handle )
`````````````````

Stops a sound event


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


void StopSoundOn(string soundName, handle playingEntity)
`````````````````

Stop named sound on Entity


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string | soundName | No Description Set |
|  handle | playingEntity | No Description Set |
+-----------+--------------+--------------+


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


float Time()
`````````````````

Get the current server time


Returns:
float - No Description Set


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


void UnloadSpawnGroup(string )
`````````````````

Unload a spawn group by name


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+


void UnloadSpawnGroupByHandle(int )
`````````````````

Unload a spawn group by ''handle''


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


void UpdateEventPoints(handle )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


void UTIL_Remove(handle )
`````````````````

Removes the specified entity


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


void UTIL_RemoveImmediate(handle )
`````````````````

Immediately removes the specified entity


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


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


void Warning(string )
`````````````````

Print a warning


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+


void ApplyAbsVelocityImpulse(Vector )
`````````````````

Apply a Velocity Impulse


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector |  | No Description Set |
+-----------+--------------+--------------+


void ApplyLocalAngularVelocityImpulse(Vector )
`````````````````

Apply an Ang Velocity Impulse


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector |  | No Description Set |
+-----------+--------------+--------------+


void EmitSound(string soundName)
`````````````````

 


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string | soundName | No Description Set |
+-----------+--------------+--------------+


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


QAngle EyeAngles()
`````````````````

Get the qangles that this entity is looking at.


Returns:
QAngle - No Description Set


Vector EyePosition()
`````````````````

Get ''vector'' to eye position - absolute coords


Returns:
Vector - No Description Set


handle FirstMoveChild()
`````````````````

No Description Set


Returns:
handle - No Description Set


void GatherCriteria(handle )
`````````````````

Returns a ''table'' containing the criteria that would be used for response queries on this entity. This is the same as the ''table'' that is passed to response rule script function callbacks.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


Vector GetAbsOrigin()
`````````````````

No Description Set


Returns:
Vector - No Description Set


QAngle GetAngles()
`````````````````

No Description Set


Returns:
QAngle - No Description Set


Vector GetAnglesAsVector()
`````````````````

Get entity pitch, yaw, roll as a ''vector''


Returns:
Vector - No Description Set


Vector GetAngularVelocity()
`````````````````

Get the local angular velocity - returns a ''vector'' of pitch,yaw,roll


Returns:
Vector - No Description Set


Vector GetBaseVelocity()
`````````````````

Get Base velocity


Returns:
Vector - No Description Set


Vector GetBoundingMaxs()
`````````````````

Get a ''vector'' containing max bounds, centered on object


Returns:
Vector - No Description Set


Vector GetBoundingMins()
`````````````````

Get a ''vector'' containing min bounds, centered on object


Returns:
Vector - No Description Set


table GetBounds()
`````````````````

Get a ''table'' containing the 'Mins' & 'Maxs' ''vector'' bounds, centered on object


Returns:
table - No Description Set


Vector GetCenter()
`````````````````

Get ''vector'' to center of object - absolute coords


Returns:
Vector - No Description Set


handle GetChildren()
`````````````````

Get the entities parented to this entity.


Returns:
handle - No Description Set


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


Vector GetForwardVector()
`````````````````

Get the forward ''vector'' of the entity


Returns:
Vector - No Description Set


int GetHealth()
`````````````````

No Description Set


Returns:
int - No Description Set


QAngle GetLocalAngularVelocity()
`````````````````

Maybe local angvel


Returns:
QAngle - No Description Set


Vector GetLocalVelocity()
`````````````````

Get Entity relative velocity


Returns:
Vector - No Description Set


int GetMaxHealth()
`````````````````

No Description Set


Returns:
int - No Description Set


string GetModelName()
`````````````````

Returns the name of the model


Returns:
string - No Description Set


handle GetMoveParent()
`````````````````

If in hierarchy, retrieves the entity's parent


Returns:
handle - No Description Set


Vector GetOrigin()
`````````````````

No Description Set


Returns:
Vector - No Description Set


handle GetOwner()
`````````````````

Gets this entity's owner


Returns:
handle - No Description Set


handle GetOwnerEntity()
`````````````````

Get the owner entity, if there is one


Returns:
handle - No Description Set


Vector GetRightVector()
`````````````````

Get the right ''vector'' of the entity


Returns:
Vector - No Description Set


handle GetRootMoveParent()
`````````````````

If in hierarchy, walks up the hierarchy to find the root parent


Returns:
handle - No Description Set


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


int GetTeam()
`````````````````

No Description Set


Returns:
int - No Description Set


Vector GetUpVector()
`````````````````

Get the up ''vector'' of the entity


Returns:
Vector - No Description Set


Vector GetVelocity()
`````````````````

No Description Set


Returns:
Vector - No Description Set


bool IsAlive()
`````````````````

No Description Set.


Returns:
bool - No Description Set


bool IsPlayer()
`````````````````

Is this a player entity?


Returns:
bool - No Description Set


void Kill()
`````````````````

No Description Set




handle NextMovePeer()
`````````````````

No Description Set


Returns:
handle - No Description Set


void OverrideFriction(float , float )
`````````````````

Takes duration, value for a temporary override


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


void PrecacheScriptSound(string )
`````````````````

Precache a sound for later playing.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+


void SetAbsOrigin(Vector origin)
`````````````````

SetAbsOrigin


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector | origin | No Description Set |
+-----------+--------------+--------------+


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


void SetForwardVector(Vector forwardVec)
`````````````````

Set the orientation of the entity to have this forward ''forwardVec''


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector | forwardVec | No Description Set |
+-----------+--------------+--------------+


void SetFriction(float )
`````````````````

Set PLAYER friction, ignored for objects


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


void SetGravity(float )
`````````````````

Set PLAYER gravity, ignored for objects


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


void SetHealth(int hp)
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int | hp | No Description Set |
+-----------+--------------+--------------+


void SetMaxHealth(int maxHP)
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int | maxHP | No Description Set |
+-----------+--------------+--------------+


void SetModel(string modelName)
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string | modelName | No Description Set |
+-----------+--------------+--------------+


void SetOrigin(Vector origin)
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector | origin | No Description Set |
+-----------+--------------+--------------+


void SetOwner(handle owningEntity)
`````````````````

Sets this entity's owner


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle | owningEntity | No Description Set |
+-----------+--------------+--------------+


void SetParent(handle , string )
`````````````````

Set the parent for this entity.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
|  string |  | No Description Set |
+-----------+--------------+--------------+


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


void SetSize(Vector , Vector )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector |  | No Description Set |
|  Vector |  | No Description Set |
+-----------+--------------+--------------+


void SetTeam(int team)
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int | team | DOTA_TEAM |
+-----------+--------------+--------------+


void SetVelocity(Vector )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector |  | No Description Set |
+-----------+--------------+--------------+


void StopSound(string soundName)
`````````````````

Stops a named sound playing from this entity.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string | soundName | No Description Set |
+-----------+--------------+--------------+


void Trigger()
`````````````````

Fires off this entity's OnTrigger responses




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


handle First()
`````````````````

Begin an iteration over the list of entities


Returns:
handle - No Description Set


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


void ConnectOutput(string , string )
`````````````````

Adds an I/O connection that will call the named function on this entity when the specified output fires.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  string |  | No Description Set |
+-----------+--------------+--------------+


void Destroy()
`````````````````

No Description Set




void DisconnectOutput(string , string )
`````````````````

Removes a connected script function from an I/O event on this entity.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  string |  | No Description Set |
+-----------+--------------+--------------+


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


int entindex()
`````````````````

No Description Set


Returns:
int - No Description Set


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


string GetClassname()
`````````````````

No Description Set


Returns:
string - No Description Set


string GetDebugName()
`````````````````

Get the entity name w/help if not defined (i.e. classname/etc)


Returns:
string - No Description Set


ehandle GetEntityHandle()
`````````````````

Get the entity as an EHANDLE


Returns:
ehandle - No Description Set


int GetEntityIndex()
`````````````````

No Description Set


Returns:
int - No Description Set


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


string GetName()
`````````````````

No Description Set


Returns:
string - No Description Set


handle GetOrCreatePrivateScriptScope()
`````````````````

Retrieve, creating if necessary, the private per-instance script-side data associated with an entity


Returns:
handle - No Description Set


handle GetOrCreatePublicScriptScope()
`````````````````

Retrieve, creating if necessary, the public script-side data associated with an entity


Returns:
handle - No Description Set


handle GetPrivateScriptScope()
`````````````````

Retrieve the private per-instance script-side data associated with an entity


Returns:
handle - No Description Set


handle GetPublicScriptScope()
`````````````````

Retrieve the public script-side data associated with an entity


Returns:
handle - No Description Set


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


void RemoveSelf()
`````````````````

Delete this entity




void SetIntAttr(string , int )
`````````````````

Set Integer Attribute


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+


void CastAbility()
`````````````````

No Description Set




bool ContinueCasting()
`````````````````

No Description Set


Returns:
bool - No Description Set


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


void DecrementModifierRefCount()
`````````````````

No Description Set




void EndChannel(bool )
`````````````````

Param: ''bool'' bInterrupted


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


void EndCooldown()
`````````````````

Clear the cooldown remaining on this ability.




int GetAbilityDamage()
`````````````````

No Description Set


Returns:
int - No Description Set


int GetAbilityDamageType()
`````````````````

No Description Set


Returns:
int - No Description Set


int GetAbilityIndex()
`````````````````

No Description Set


Returns:
int - No Description Set


string GetAbilityName()
`````````````````

No Description Set


Returns:
string - No Description Set


int GetAbilityTargetFlags()
`````````````````

No Description Set


Returns:
int - No Description Set


int GetAbilityTargetTeam()
`````````````````

No Description Set


Returns:
int - No Description Set


int GetAbilityTargetType()
`````````````````

No Description Set


Returns:
int - No Description Set


int GetAbilityType()
`````````````````

No Description Set


Returns:
int - No Description Set


bool GetAnimationIgnoresModelScale()
`````````````````

No Description Set


Returns:
bool - No Description Set


string GetAssociatedPrimaryAbilities()
`````````````````

No Description Set


Returns:
string - No Description Set


string GetAssociatedSecondaryAbilities()
`````````````````

No Description Set


Returns:
string - No Description Set


bool GetAutoCastState()
`````````````````

No Description Set


Returns:
bool - No Description Set


float GetBackswingTime()
`````````````````

No Description Set


Returns:
float - No Description Set


int GetBehavior()
`````````````````

No Description Set


Returns:
int - No Description Set


handle GetCaster()
`````````````````

No Description Set


Returns:
handle - No Description Set


float GetCastPoint()
`````````````````

No Description Set


Returns:
float - No Description Set


int GetCastRange()
`````````````````

No Description Set


Returns:
int - No Description Set


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


float GetChannelStartTime()
`````````````````

No Description Set


Returns:
float - No Description Set


float GetChannelTime()
`````````````````

No Description Set


Returns:
float - No Description Set


handle GetCloneSource()
`````````````````

No Description Set


Returns:
handle - No Description Set


int GetConceptRecipientType()
`````````````````

No Description Set


Returns:
int - No Description Set


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


float GetCooldownTime()
`````````````````

No Description Set


Returns:
float - No Description Set


float GetCooldownTimeRemaining()
`````````````````

No Description Set


Returns:
float - No Description Set


Vector GetCursorPosition()
`````````````````

No Description Set


Returns:
Vector - No Description Set


handle GetCursorTarget()
`````````````````

No Description Set


Returns:
handle - No Description Set


bool GetCursorTargetingNothing()
`````````````````

No Description Set


Returns:
bool - No Description Set


float GetDuration()
`````````````````

No Description Set


Returns:
float - No Description Set


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


int GetHeroLevelRequiredToUpgrade()
`````````````````

No Description Set


Returns:
int - No Description Set


string GetIntrinsicModifierName()
`````````````````

No Description Set


Returns:
string - No Description Set


int GetLevel()
`````````````````

Get the current level of the ability


Returns:
int - No Description Set


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


int GetMaxLevel()
`````````````````

No Description Set


Returns:
int - No Description Set


float GetModifierValue()
`````````````````

No Description Set


Returns:
float - No Description Set


float GetModifierValueBonus()
`````````````````

No Description Set


Returns:
float - No Description Set


float GetPlaybackRateOverride()
`````````````````

No Description Set


Returns:
float - No Description Set


string GetSharedCooldownName()
`````````````````

No Description Set


Returns:
string - No Description Set


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


string GetStolenActivityModifier()
`````````````````

No Description Set


Returns:
string - No Description Set


bool GetToggleState()
`````````````````

No Description Set


Returns:
bool - No Description Set


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


void IncrementModifierRefCount()
`````````````````

No Description Set




bool IsActivated()
`````````````````

No Description Set


Returns:
bool - No Description Set


bool IsAttributeBonus()
`````````````````

No Description Set


Returns:
bool - No Description Set


bool IsChanneling()
`````````````````

Returns whether the ability is currently channeling.


Returns:
bool - No Description Set


bool IsCooldownReady()
`````````````````

No Description Set


Returns:
bool - No Description Set


bool IsCosmetic()
`````````````````

No Description Set


Returns:
bool - No Description Set


bool IsFullyCastable()
`````````````````

Returns whether the ability can be cast.


Returns:
bool - No Description Set


bool IsHidden()
`````````````````

No Description Set


Returns:
bool - No Description Set


bool IsHiddenWhenStolen()
`````````````````

No Description Set


Returns:
bool - No Description Set


bool IsInAbilityPhase()
`````````````````

Returns whether the ability is currently casting.


Returns:
bool - No Description Set


bool IsItem()
`````````````````

No Description Set


Returns:
bool - No Description Set


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


bool IsOwnersGoldEnoughForUpgrade()
`````````````````

No Description Set


Returns:
bool - No Description Set


bool IsOwnersManaEnough()
`````````````````

No Description Set


Returns:
bool - No Description Set


bool IsPassive()
`````````````````

No Description Set


Returns:
bool - No Description Set


bool IsSharedWithTeammates()
`````````````````

No Description Set


Returns:
bool - No Description Set


bool IsStealable()
`````````````````

No Description Set


Returns:
bool - No Description Set


bool IsStolen()
`````````````````

No Description Set


Returns:
bool - No Description Set


bool IsToggle()
`````````````````

No Description Set


Returns:
bool - No Description Set


bool IsTrained()
`````````````````

No Description Set


Returns:
bool - No Description Set


void MarkAbilityButtonDirty()
`````````````````

Mark the ability button for this ability as needing a refresh




int NumModifiersUsingAbility()
`````````````````

No Description Set


Returns:
int - No Description Set


void OnAbilityPhaseInterrupted()
`````````````````

No Description Set




bool OnAbilityPhaseStart()
`````````````````

No Description Set


Returns:
bool - No Description Set


void OnAbilityPinged()
`````````````````

No Description Set




void OnChannelFinish(bool )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


void OnChannelThink(float )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


void OnHeroCalculateStatBonus()
`````````````````

No Description Set




void OnHeroLevelUp()
`````````````````

No Description Set




void OnInventoryContentsChanged()
`````````````````

No Description Set




void OnOwnerDied()
`````````````````

No Description Set




void OnOwnerSpawned()
`````````````````

No Description Set




void OnSpellStart()
`````````````````

No Description Set




void OnToggle()
`````````````````

No Description Set




void OnUpgrade()
`````````````````

No Description Set




void PayGoldCost()
`````````````````

No Description Set




void PayGoldCostForUpgrade()
`````````````````

No Description Set




void PayManaCost()
`````````````````

No Description Set




bool PlaysDefaultAnimWhenStolen()
`````````````````

No Description Set


Returns:
bool - No Description Set


bool ProcsMagicStick()
`````````````````

No Description Set


Returns:
bool - No Description Set


bool RefCountsModifiers()
`````````````````

No Description Set


Returns:
bool - No Description Set


void RefundManaCost()
`````````````````

No Description Set




bool ResetToggleOnRespawn()
`````````````````

No Description Set


Returns:
bool - No Description Set


void SetAbilityIndex(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


void SetActivated(bool )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


void SetChanneling(bool )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


void SetHidden(bool )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


void SetInAbilityPhase(bool )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


void SetLevel(int )
`````````````````

Sets the level of this ability.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


void SetOverrideCastPoint(float )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


void SetRefCountsModifiers(bool )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


void SetStolen(bool )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


bool ShouldUseResources()
`````````````````

No Description Set


Returns:
bool - No Description Set


void SpeakAbilityConcept(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


bool SpeakTrigger()
`````````````````

No Description Set


Returns:
bool - No Description Set


void StartCooldown(float )
`````````````````

param: flCooldown


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


void ToggleAbility()
`````````````````

No Description Set




void ToggleAutoCast()
`````````````````

No Description Set




void UpgradeAbility()
`````````````````

No Description Set




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


void SetPlaybackRate(float )
`````````````````

Override playbackrate


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


void SetPlaybackRate(float )
`````````````````

Override playbackrate


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


void SetPlaybackRate(float )
`````````````````

Override playbackrate


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


void SetPlaybackRate(float )
`````````````````

Override playbackrate


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


int GetCastCount()
`````````````````

Number of times Nian has used the roar


Returns:
int - No Description Set


handle GetContainer()
`````````````````

Get the container for this item.


Returns:
handle - No Description Set


int GetCost()
`````````````````

No Description Set


Returns:
int - No Description Set


int GetCurrentCharges()
`````````````````

Get the number of charges this item currently has.


Returns:
int - No Description Set


int GetInitialCharges()
`````````````````

Get the initial number of charges this item has.


Returns:
int - No Description Set


handle GetPurchaser()
`````````````````

Get the purchaser for this item.


Returns:
handle - No Description Set


float GetPurchaseTime()
`````````````````

Get the purchase time of this item


Returns:
float - No Description Set


int GetShareability()
`````````````````

No Description Set


Returns:
int - No Description Set


bool IsPermanent()
`````````````````

Is this a permanent item?


Returns:
bool - No Description Set


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


void SetCurrentCharges(int )
`````````````````

Set the number of charges on this item


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


void SetPurchaser(handle )
`````````````````

Set the purchaser of record for this item.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


void SetPurchaseTime(float )
`````````````````

Set the purchase time of this item


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


void SetStacksWithOtherOwners(bool )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


bool StacksWithOtherOwners()
`````````````````

No Description Set


Returns:
bool - No Description Set


void Think()
`````````````````

Think this item




handle GetContainedItem()
`````````````````

Returned the contained item.


Returns:
handle - No Description Set


float GetCreationTime()
`````````````````

Returns the game time when this item was created in the world


Returns:
float - No Description Set


void SetContainedItem(handle )
`````````````````

Set the contained item.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


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


handle GetHorn()
`````````````````

Is the Nian horn?


Returns:
handle - No Description Set


handle GetTail()
`````````````````

Is the Nian's tail broken?


Returns:
handle - No Description Set


bool IsHornAlive()
`````````````````

Is the Nian's horn broken?


Returns:
bool - No Description Set


bool IsTailAlive()
`````````````````

Is the Nian's tail broken?


Returns:
bool - No Description Set


bool IsNoclipping()
`````````````````

Returns true if the player is in noclip mode.


Returns:
bool - No Description Set


handle GetAssignedHero()
`````````````````

Get the player's hero.


Returns:
handle - No Description Set


handle GetControlledRPGUnit()
`````````````````

Get the RPG unit this player controls.


Returns:
handle - No Description Set


int GetPlayerID()
`````````````````

Get the player's official PlayerID; notably is -1 when the player isn't yet on a team.


Returns:
int - No Description Set


void MakeRandomHeroSelection()
`````````````````

Randoms this player's hero.




void SetKillCamUnit(handle )
`````````````````

Set the kill cam unit for this hero.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


void SetMusicStatus(int nMusicStatus, float flIntensity)
`````````````````

Set the music status for this player, note this will only really apply if dota_music_battle_enable is off.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int | nMusicStatus | Status flag of the Music |
|  float | flIntensity | Intensity of the music |
+-----------+--------------+--------------+


void AddAegisPickup(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


void AddClaimedFarm(int , float )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


void AddGoldSpentOnSupport(int , int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+


void AddRunePickup(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


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


void ClearKillsMatrix(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


void ClearLastHitMultikill(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


void ClearLastHitStreak(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


void ClearRawPlayerDamageMatrix(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


void ClearStreak(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


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


bool HaveAllPlayersJoined()
`````````````````

No Description Set


Returns:
bool - No Description Set


void HeroLevelUp(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


void IncrementAssists(int playerID)
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int | playerID | No Description Set |
+-----------+--------------+--------------+


void IncrementClaimedDenies(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


void IncrementClaimedMisses(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


void IncrementDeaths(int playerID)
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int | playerID | No Description Set |
+-----------+--------------+--------------+


void IncrementDenies(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


void IncrementGoldBagsCollected(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


void IncrementKills(int playerID, int kills)
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int | playerID | No Description Set |
|  int | kills | No Description Set |
+-----------+--------------+--------------+


void IncrementLastHitMultikill(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


void IncrementLastHits(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


void IncrementLastHitStreak(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


void IncrementMisses(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


void IncrementNearbyCreepDeaths(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


void IncrementStreak(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


void IncrementTotalEarnedXP(int , int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+


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


void ResetBuybackCostTime(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


void ResetTotalEarnedGold(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


void SetBuybackCooldownTime(int , float )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


void SetBuybackGoldLimitTime(int , float )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


void SetCameraTarget(int , handle )
`````````````````

(playerID, entity) - force the given player's camera to follow the given entity


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


void SetCustomBuybackCooldown(int , float )
`````````````````

Set the buyback cooldown for this player.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


void SetCustomBuybackCost(int , int )
`````````````````

Set the buyback cost for this player.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+


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


void SetHasRandomed(int playerID)
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int | playerID | No Description Set |
+-----------+--------------+--------------+


void SetHasRepicked(int playerID)
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int | playerID | No Description Set |
+-----------+--------------+--------------+


void SetLastBuybackTime(int , int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+


void SetPlayerReservedState(int , bool )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
|  bool |  | No Description Set |
+-----------+--------------+--------------+


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


void UpdateTeamSlot(int , int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+


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


void AddAbility(string )
`````````````````

Add an ability to this unit by name.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+


void AddItem(handle )
`````````````````

Add an item to this unit's inventory.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


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


void AddNoDraw()
`````````````````

Adds the no draw flag.




void AlertNearbyUnits(handle , handle )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


void AngerNearbyUnits()
`````````````````

No Description Set




void AttackNoEarlierThan(float )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


bool AttackReady()
`````````````````

No Description Set


Returns:
bool - No Description Set


float BoundingRadius2D()
`````````````````

No Description Set


Returns:
float - No Description Set


void CastAbilityImmediately(handle , int )
`````````````````

Cast an ability immediately.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+


void CastAbilityNoTarget(handle ability, int playerIndex)
`````````````````

Cast an ability with no target. ( hAbility, iPlayerIndex )


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle | ability | No Description Set |
|  int | playerIndex | No Description Set |
+-----------+--------------+--------------+


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


void CastAbilityToggle(handle , int )
`````````````````

Toggle an ability. ( hAbility, iPlayerIndex )


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+


void DisassembleItem(handle )
`````````````````

Disassemble the passed item in this unit's inventory.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


void DropItemAtPosition(Vector , handle )
`````````````````

Drop an item at a given point.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


void DropItemAtPositionImmediate(handle , Vector )
`````````````````

Immediately drop a carried item at a given position.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
|  Vector |  | No Description Set |
+-----------+--------------+--------------+


void EjectItemFromStash(handle )
`````````````````

Drops the selected item out of this unit's stash.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


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


void ForceKill(bool )
`````````````````

Kill this unit immediately.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


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


int GetAbilityCount()
`````````````````

No Description Set


Returns:
int - No Description Set


float GetAcquisitionRange()
`````````````````

Gets the range at which this unit will auto-acquire.


Returns:
float - No Description Set


float GetAdditionalBattleMusicWeight()
`````````````````

Combat involving this creature will have this weight added to the music calcuations


Returns:
float - No Description Set


float GetAttackAnimationPoint()
`````````````````

No Description Set


Returns:
float - No Description Set


int GetAttackDamage()
`````````````````

Returns a random integer between the minimum and maximum base damage of the unit.


Returns:
int - No Description Set


float GetAttackRange()
`````````````````

Gets this unit's attack range after all modifiers.


Returns:
float - No Description Set


float GetAttackRangeBuffer()
`````````````````

Gets the attack range buffer.


Returns:
float - No Description Set


float GetAttackSpeed()
`````````````````

No Description Set


Returns:
float - No Description Set


float GetAttacksPerSecond()
`````````````````

No Description Set


Returns:
float - No Description Set


handle GetAttackTarget()
`````````````````

No Description Set


Returns:
handle - No Description Set


int GetAverageTrueAttackDamage()
`````````````````

Returns the average value of the minimum and maximum damage values.


Returns:
int - No Description Set


int GetBaseAttackRange()
`````````````````

Gets this unit's attack range before modifiers.


Returns:
int - No Description Set


float GetBaseAttackTime()
`````````````````

No Description Set


Returns:
float - No Description Set


int GetBaseDamageMax()
`````````````````

Gets the minimum base damage.


Returns:
int - No Description Set


int GetBaseDamageMin()
`````````````````

Gets the minimum base damage.


Returns:
int - No Description Set


int GetBaseDayTimeVisionRange()
`````````````````

Returns the vision range before modifiers.


Returns:
int - No Description Set


float GetBaseHealthRegen()
`````````````````

No Description Set


Returns:
float - No Description Set


float GetBaseMagicalResistanceValue()
`````````````````

Returns base magical armor value.


Returns:
float - No Description Set


float GetBaseMaxHealth()
`````````````````

Gets the base max health value.


Returns:
float - No Description Set


float GetBaseMoveSpeed()
`````````````````

No Description Set


Returns:
float - No Description Set


int GetBaseNightTimeVisionRange()
`````````````````

Returns the vision range before modifiers.


Returns:
int - No Description Set


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


float GetCollisionPadding()
`````````````````

Returns the size of the collision padding around the hull.


Returns:
float - No Description Set


float GetConstantBasedManaRegen()
`````````````````

This Mana regen is derived from constant bonuses like Basilius.


Returns:
float - No Description Set


float GetCreationTime()
`````````````````

No Description Set


Returns:
float - No Description Set


handle GetCurrentActiveAbility()
`````````````````

Get the ability this unit is currently casting.


Returns:
handle - No Description Set


int GetCurrentVisionRange()
`````````````````

Gets the current vision range.


Returns:
int - No Description Set


handle GetCursorCastTarget()
`````````````````

No Description Set


Returns:
handle - No Description Set


Vector GetCursorPosition()
`````````````````

No Description Set


Returns:
Vector - No Description Set


bool GetCursorTargetingNothing()
`````````````````

No Description Set


Returns:
bool - No Description Set


int GetDayTimeVisionRange()
`````````````````

Returns the vision range after modifiers.


Returns:
int - No Description Set


int GetDeathXP()
`````````````````

Get the XP bounty on this unit


Returns:
int - No Description Set


handle GetForceAttackTarget()
`````````````````

No Description Set


Returns:
handle - No Description Set


int GetGoldBounty()
`````````````````

Get the gold bounty on this unit


Returns:
int - No Description Set


float GetHasteFactor()
`````````````````

No Description Set


Returns:
float - No Description Set


int GetHealth()
`````````````````

Get the health of this unit.


Returns:
int - No Description Set


int GetHealthDeficit()
`````````````````

Returns integer amount of health missing from max.


Returns:
int - No Description Set


int GetHealthPercent()
`````````````````

Get the current health percent of the unit.


Returns:
int - No Description Set


float GetHealthRegen()
`````````````````

No Description Set


Returns:
float - No Description Set


float GetHullRadius()
`````````````````

Get the collision hull radius of this NPC


Returns:
float - No Description Set


float GetIdealSpeed()
`````````````````

Returns speed after all modifiers.


Returns:
float - No Description Set


float GetIncreasedAttackSpeed()
`````````````````

No Description Set


Returns:
float - No Description Set


handle GetInitialGoalEntity()
`````````````````

Returns the initial waypoint goal for this NPC


Returns:
handle - No Description Set


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


float GetLastIdleChangeTime()
`````````````````

Get the last game time that this unit switched to/from idle state.


Returns:
float - No Description Set


int GetLevel()
`````````````````

Returns the level of this unit.


Returns:
int - No Description Set


float GetMagicalArmorValue()
`````````````````

Returns current magical armor value.


Returns:
float - No Description Set


int GetMainControllingPlayer()
`````````````````

Returns the player ID of the controlling player.


Returns:
int - No Description Set


float GetMana()
`````````````````

Get the mana on this unit.


Returns:
float - No Description Set


int GetManaPercent()
`````````````````

Get the percent of mana remaining.


Returns:
int - No Description Set


float GetManaRegen()
`````````````````

No Description Set


Returns:
float - No Description Set


int GetMaxHealth()
`````````````````

Get the maximum health of this unit.


Returns:
int - No Description Set


float GetMaxMana()
`````````````````

Get the maximum mana of this unit.


Returns:
float - No Description Set


float GetModelRadius()
`````````````````

No Description Set


Returns:
float - No Description Set


int GetModifierCount()
`````````````````

How many modifiers does this unit have?


Returns:
int - No Description Set


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


bool GetMustReachEachGoalEntity()
`````````````````

Get whether this NPC is required to reach each goal entity, rather than being allowed to 'unkink' their path


Returns:
bool - No Description Set


int GetNightTimeVisionRange()
`````````````````

Returns the vision range after modifiers.


Returns:
int - No Description Set


int GetOpposingTeamNumber()
`````````````````

No Description Set


Returns:
int - No Description Set


float GetPaddedCollisionRadius()
`````````````````

Get the collision hull radius (including padding) of this NPC


Returns:
float - No Description Set


float GetPercentageBasedManaRegen()
`````````````````

This Mana regen is derived from % bonuses (from items like Void Stone).


Returns:
float - No Description Set


float GetPhysicalArmorBaseValue()
`````````````````

Returns base physical armor value.


Returns:
float - No Description Set


float GetPhysicalArmorValue()
`````````````````

Returns current physical armor value.


Returns:
float - No Description Set


handle GetPlayerOwner()
`````````````````

Returns the player that owns this unit


Returns:
handle - No Description Set


int GetPlayerOwnerID()
`````````````````

Get the owner player ID for this unit.


Returns:
int - No Description Set


int GetProjectileSpeed()
`````````````````

No Description Set


Returns:
int - No Description Set


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


float GetSecondsPerAttack()
`````````````````

No Description Set


Returns:
float - No Description Set


float GetStatsBasedManaRegen()
`````````````````

Returns mana regen rate per intelligence.


Returns:
float - No Description Set


int GetTeamNumber()
`````````````````

Get the team number of this unit.


Returns:
int - No Description Set


int GetTotalPurchasedUpgradeGoldCost()
`````````````````

Get how much gold has been spent on ability upgrades.


Returns:
int - No Description Set


string GetUnitLabel()
`````````````````

No Description Set


Returns:
string - No Description Set


string GetUnitName()
`````````````````

No Description Set


Returns:
string - No Description Set


void GiveMana(float )
`````````````````

Give mana to this unit, this can be used for mana gained by abilities or item usage.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


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


bool HasAttackCapability()
`````````````````

No Description Set


Returns:
bool - No Description Set


bool HasFlyingVision()
`````````````````

No Description Set


Returns:
bool - No Description Set


bool HasFlyMovementCapability()
`````````````````

No Description Set


Returns:
bool - No Description Set


bool HasGroundMovementCapability()
`````````````````

No Description Set


Returns:
bool - No Description Set


bool HasInventory()
`````````````````

No Description Set


Returns:
bool - No Description Set


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


bool HasMovementCapability()
`````````````````

No Description Set


Returns:
bool - No Description Set


bool HasScepter()
`````````````````

No Description Set


Returns:
bool - No Description Set


void Heal(float , handle )
`````````````````

Heal this unit.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


void Hold()
`````````````````

Hold position.




void Interrupt()
`````````````````

No Description Set




void InterruptChannel()
`````````````````

No Description Set




void InterruptMotionControllers(bool )
`````````````````

Parameter boolean determines finding clear space.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


bool IsAlive()
`````````````````

Is this unit alive?


Returns:
bool - No Description Set


bool IsAncient()
`````````````````

Is this creature an Ancient?


Returns:
bool - No Description Set


bool IsAttackImmune()
`````````````````

No Description Set


Returns:
bool - No Description Set


bool IsAttacking()
`````````````````

No Description Set


Returns:
bool - No Description Set


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


bool IsBlind()
`````````````````

No Description Set


Returns:
bool - No Description Set


bool IsBlockDisabled()
`````````````````

No Description Set


Returns:
bool - No Description Set


bool IsCommandRestricted()
`````````````````

No Description Set


Returns:
bool - No Description Set


bool IsControllableByAnyPlayer()
`````````````````

Is this unit controlled by any non-bot player?


Returns:
bool - No Description Set


bool IsCreature()
`````````````````

Is this a Creature type NPC


Returns:
bool - No Description Set


bool IsDeniable()
`````````````````

No Description Set


Returns:
bool - No Description Set


bool IsDisarmed()
`````````````````

No Description Set


Returns:
bool - No Description Set


bool IsDominated()
`````````````````

No Description Set


Returns:
bool - No Description Set


bool IsEvadeDisabled()
`````````````````

No Description Set


Returns:
bool - No Description Set


bool IsFrozen()
`````````````````

No Description Set


Returns:
bool - No Description Set


bool IsHardDisarmed()
`````````````````

No Description Set


Returns:
bool - No Description Set


bool IsHero()
`````````````````

Is this a hero or hero illusion?


Returns:
bool - No Description Set


bool IsHexed()
`````````````````

No Description Set


Returns:
bool - No Description Set


bool IsIdle()
`````````````````

Is this creature currently idle?


Returns:
bool - No Description Set


bool IsIllusion()
`````````````````

No Description Set


Returns:
bool - No Description Set


bool IsInvisible()
`````````````````

No Description Set


Returns:
bool - No Description Set


bool IsInvulnerable()
`````````````````

No Description Set


Returns:
bool - No Description Set


bool IsLowAttackPriority()
`````````````````

No Description Set


Returns:
bool - No Description Set


bool IsMagicImmune()
`````````````````

No Description Set


Returns:
bool - No Description Set


bool IsMechanical()
`````````````````

Is the unit mechanical?


Returns:
bool - No Description Set


bool IsMovementImpaired()
`````````````````

No Description Set


Returns:
bool - No Description Set


bool IsMuted()
`````````````````

No Description Set


Returns:
bool - No Description Set


bool IsNeutralUnitType()
`````````````````

Is this a neutral?


Returns:
bool - No Description Set


bool IsNightmared()
`````````````````

No Description Set


Returns:
bool - No Description Set


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


bool IsOutOfGame()
`````````````````

No Description Set


Returns:
bool - No Description Set


bool IsOwnedByAnyPlayer()
`````````````````

Is this unit owned by any non-bot player?


Returns:
bool - No Description Set


bool IsPhantom()
`````````````````

Is this a phantom unit?


Returns:
bool - No Description Set


bool IsPhantomBlocker()
`````````````````

No Description Set


Returns:
bool - No Description Set


bool IsPhased()
`````````````````

No Description Set


Returns:
bool - No Description Set


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


bool IsRangedAttacker()
`````````````````

Is this unit a ranged attacker?


Returns:
bool - No Description Set


bool IsRealHero()
`````````````````

Returns true if the hero is a true Hero, not a creep or an Illusion of a hero


Returns:
bool - No Description Set


bool IsRooted()
`````````````````

No Description Set


Returns:
bool - No Description Set


bool IsSilenced()
`````````````````

No Description Set


Returns:
bool - No Description Set


bool IsSoftDisarmed()
`````````````````

No Description Set


Returns:
bool - No Description Set


bool IsSpeciallyDeniable()
`````````````````

No Description Set


Returns:
bool - No Description Set


bool IsStunned()
`````````````````

No Description Set


Returns:
bool - No Description Set


bool IsSummoned()
`````````````````

Is this unit summoned?


Returns:
bool - No Description Set


bool IsTower()
`````````````````

Is this a tower?


Returns:
bool - No Description Set


bool IsUnableToMiss()
`````````````````

No Description Set


Returns:
bool - No Description Set


bool IsUnselectable()
`````````````````

No Description Set


Returns:
bool - No Description Set


void Kill(handle , handle )
`````````````````

Kills this NPC, with the params Ability and Attacker


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


void MakeIllusion()
`````````````````

No Description Set




void MakePhantomBlocker()
`````````````````

No Description Set




void MakeVisibleDueToAttack(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


void MakeVisibleToTeam(int , float )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


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


void MoveToNPC(handle )
`````````````````

Move to follow a unit.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


void MoveToNPCToGiveItem(handle , handle )
`````````````````

Give an item to another unit.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


void MoveToPosition(Vector )
`````````````````

Issue a Move-To command


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector |  | No Description Set |
+-----------+--------------+--------------+


void MoveToPositionAggressive(Vector )
`````````````````

Issue an Attack-Move-To command


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector |  | No Description Set |
+-----------+--------------+--------------+


void MoveToTargetToAttack(handle )
`````````````````

Move to a target to attack.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


bool NoHealthBar()
`````````````````

No Description Set


Returns:
bool - No Description Set


bool NoTeamMoveTo()
`````````````````

No Description Set


Returns:
bool - No Description Set


bool NoTeamSelect()
`````````````````

No Description Set


Returns:
bool - No Description Set


bool NotOnMinimap()
`````````````````

No Description Set


Returns:
bool - No Description Set


bool NotOnMinimapForEnemies()
`````````````````

No Description Set


Returns:
bool - No Description Set


bool NoUnitCollision()
`````````````````

No Description Set


Returns:
bool - No Description Set


bool PassivesDisabled()
`````````````````

No Description Set


Returns:
bool - No Description Set


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


void PickupDroppedItem(handle )
`````````````````

Pick up a dropped item.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


void PickupRune(handle )
`````````````````

Pick up a rune.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


bool ProvidesVision()
`````````````````

No Description Set


Returns:
bool - No Description Set


void ReduceMana(float )
`````````````````

Remove mana from this unit, this can be used for involuntary mana loss, not for mana that is spent.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


void RemoveAbility(string )
`````````````````

Remove an ability from this unit by name.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+


void RemoveItem(handle )
`````````````````

Removes the passed item from this unit's inventory.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


void RemoveModifierByName(string )
`````````````````

Removes a modifier


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+


void RemoveModifierByNameAndCaster(string , handle )
`````````````````

Removes a modifier that was cast by the given caster


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


void RemoveNoDraw()
`````````````````

Remove the no draw flag.




void RespawnUnit()
`````````````````

Respawns the target unit if it can be respawned.




void SellItem(handle )
`````````````````

Sells the passed item in this unit's inventory.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


void SetAdditionalBattleMusicWeight(float )
`````````````````

Combat involving this creature will have this weight added to the music calcuations


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


void SetAttackCapability(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


void SetAttacking(handle )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


void SetBaseAttackTime(float )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


void SetBaseDamageMax(int )
`````````````````

Sets the minimum base damage.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


void SetBaseDamageMin(int )
`````````````````

Sets the minimum base damage.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


void SetBaseHealthRegen(float )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


void SetBaseMagicalResistanceValue(float )
`````````````````

Sets base magical armor value.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


void SetBaseManaRegen(float )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


void SetBaseMaxHealth(float )
`````````````````

Set a new base max health value.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


void SetBaseMoveSpeed(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


void SetControllableByPlayer(int , bool )
`````````````````

Set this unit controllable by the player with the passed ID.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
|  bool |  | No Description Set |
+-----------+--------------+--------------+


void SetCursorCastTarget(handle )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


void SetCursorPosition(Vector )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector |  | No Description Set |
+-----------+--------------+--------------+


void SetCursorTargetingNothing(bool )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


void SetDayTimeVisionRange(int )
`````````````````

Set the base vision range.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


void SetDeathXP(int )
`````````````````

Set the XP bounty on this unit


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


void SetForceAttackTarget(handle )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


void SetHasInventory(bool )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


void SetHullRadius(float )
`````````````````

Set the collision hull radius of this NPC


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


void SetIdleAcquire(bool )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


void SetInitialGoalEntity(handle )
`````````````````

Sets the initial waypoint goal for this NPC


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


void SetMana(float )
`````````````````

Set the mana on this unit.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


void SetMaximumGoldBounty(int )
`````````````````

Set the maximum gold bounty for this unit.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


void SetMinimumGoldBounty(int )
`````````````````

Set the minimum gold bounty for this unit.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


void SetMoveCapability(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


void SetMustReachEachGoalEntity(bool )
`````````````````

Set whether this NPC is required to reach each goal entity, rather than being allowed to 'unkink' their path


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


void SetNeverMoveToClearSpace(bool )
`````````````````

If set to true, we will never attempt to move this unit to clear space, even when it unphases.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


void SetNightTimeVisionRange(int )
`````````````````

Set the base vision range.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


void SetOriginalModel(string originalModel)
`````````````````

Sets the original model of this entity, which it will tend to fall back to anytime its state changes


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string | originalModel | No Description Set |
+-----------+--------------+--------------+


void SetPhysicalArmorBaseValue(float )
`````````````````

Sets base physical armor value.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


void SetRangedProjectileName(string )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+


void SetStolenScepter(bool )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


void SetUnitName(string )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+


bool ShouldIdleAcquire()
`````````````````

No Description Set


Returns:
bool - No Description Set


void SpendMana(float , handle )
`````````````````

Spend mana from this unit, this can be used for spending mana from abilities or item usage.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


void Stop()
`````````````````

Stop the current order.




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


float TimeUntilNextAttack()
`````````````````

No Description Set


Returns:
float - No Description Set


bool TriggerModifierDodge()
`````````````````

No Description Set


Returns:
bool - No Description Set


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


bool UnitCanRespawn()
`````````````````

No Description Set


Returns:
bool - No Description Set


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


void Buyback()
`````````````````

Spend the gold and buyback with this hero.




void CalculateStatBonus()
`````````````````

Recalculate all stats after the hero gains stats.




bool CanEarnGold()
`````````````````

Returns boolean value result of buyback gold limit time less than game time.


Returns:
bool - No Description Set


void ClearLastHitMultikill()
`````````````````

Value is stored in PlayerResource.




void ClearLastHitStreak()
`````````````````

Value is stored in PlayerResource.




void ClearStreak()
`````````````````

Value is stored in PlayerResource.




int GetAbilityPoints()
`````````````````

Gets the current unspent ability point's.


Returns:
int - No Description Set


float GetAgility()
`````````````````

No Description Set


Returns:
float - No Description Set


float GetAgilityGain()
`````````````````

No Description Set


Returns:
float - No Description Set


int GetAssists()
`````````````````

Value is stored in PlayerResource.


Returns:
int - No Description Set


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


float GetBaseAgility()
`````````````````

No Description Set


Returns:
float - No Description Set


int GetBaseDamageMax()
`````````````````

Hero damage is also affected by attributes.


Returns:
int - No Description Set


int GetBaseDamageMin()
`````````````````

Hero damage is also affected by attributes.


Returns:
int - No Description Set


float GetBaseIntellect()
`````````````````

No Description Set


Returns:
float - No Description Set


float GetBaseStrength()
`````````````````

No Description Set


Returns:
float - No Description Set


int GetBonusDamageFromPrimaryStat()
`````````````````

No Description Set


Returns:
int - No Description Set


float GetBuybackCooldownTime()
`````````````````

Return ''float'' value for the amount of time left on cooldown for this hero's buyback.


Returns:
float - No Description Set


int GetBuybackCost()
`````````````````

Return integer value for the gold cost of a buyback.


Returns:
int - No Description Set


float GetBuybackGoldLimitTime()
`````````````````

Returns the amount of time gold gain is limited after buying back.


Returns:
float - No Description Set


int GetCurrentXP()
`````````````````

Returns the amount of XP


Returns:
int - No Description Set


int GetDeathGoldCost()
`````````````````

No Description Set


Returns:
int - No Description Set


int GetDeaths()
`````````````````

Value is stored in PlayerResource.


Returns:
int - No Description Set


int GetDenies()
`````````````````

Value is stored in PlayerResource.


Returns:
int - No Description Set


int GetGold()
`````````````````

Returns gold amount for the player owning this hero


Returns:
int - No Description Set


int GetGoldBounty()
`````````````````

No Description Set


Returns:
int - No Description Set


float GetHealthRegen()
`````````````````

Hero health regen is affected by attributes.


Returns:
float - No Description Set


float GetIncreasedAttackSpeed()
`````````````````

Hero attack speed is also affected by agility.


Returns:
float - No Description Set


float GetIntellect()
`````````````````

No Description Set


Returns:
float - No Description Set


float GetIntellectGain()
`````````````````

No Description Set


Returns:
float - No Description Set


int GetKills()
`````````````````

Value is stored in PlayerResource.


Returns:
int - No Description Set


int GetLastHits()
`````````````````

Value is stored in PlayerResource.


Returns:
int - No Description Set


float GetManaRegen()
`````````````````

Hero mana regen is affected by attributes.


Returns:
float - No Description Set


float GetMostRecentDamageTime()
`````````````````

No Description Set


Returns:
float - No Description Set


int GetMultipleKillCount()
`````````````````

No Description Set


Returns:
int - No Description Set


int GetNumAttackers()
`````````````````

No Description Set


Returns:
int - No Description Set


float GetPhysicalArmorValue()
`````````````````

Hero armor is affected by attributes.


Returns:
float - No Description Set


int GetPlayerID()
`````````````````

Returns player ID of the player owning this hero


Returns:
int - No Description Set


int GetPrimaryAttribute()
`````````````````

0 = strength, 1 = agility, 2 = intelligence.


Returns:
int - No Description Set


float GetPrimaryStatValue()
`````````````````

No Description Set


Returns:
float - No Description Set


float GetRespawnTime()
`````````````````

No Description Set


Returns:
float - No Description Set


float GetStatsBasedManaRegen()
`````````````````

Returns only the regen based on Intelligence.


Returns:
float - No Description Set


int GetStreak()
`````````````````

Value is stored in PlayerResource.


Returns:
int - No Description Set


float GetStrength()
`````````````````

No Description Set


Returns:
float - No Description Set


float GetStrengthGain()
`````````````````

No Description Set


Returns:
float - No Description Set


float GetTimeUntilRespawn()
`````````````````

No Description Set


Returns:
float - No Description Set


bool HasAnyAvailableInventorySpace()
`````````````````

No Description Set


Returns:
bool - No Description Set


bool HasFlyingVision()
`````````````````

No Description Set


Returns:
bool - No Description Set


bool HasOwnerAbandoned()
`````````````````

No Description Set


Returns:
bool - No Description Set


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


void HeroLevelUp(bool )
`````````````````

Levels up the hero, true or false to play effects.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


void IncrementAssists()
`````````````````

Value is stored in PlayerResource.




void IncrementDeaths()
`````````````````

Value is stored in PlayerResource.




void IncrementDenies()
`````````````````

Value is stored in PlayerResource.




void IncrementKills(int kills)
`````````````````

Passed ID is for the victim, killer ID is ID of the current hero. Value is stored in PlayerResource.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int | kills | No Description Set |
+-----------+--------------+--------------+


void IncrementLastHitMultikill()
`````````````````

Value is stored in PlayerResource.




void IncrementLastHits()
`````````````````

Value is stored in PlayerResource.




void IncrementLastHitStreak()
`````````````````

Value is stored in PlayerResource.




void IncrementNearbyCreepDeaths()
`````````````````

Value is stored in PlayerResource.




void IncrementStreak()
`````````````````

Value is stored in PlayerResource.




bool IsBuybackDisabledByReapersScythe()
`````````````````

No Description Set


Returns:
bool - No Description Set


bool IsReincarnating()
`````````````````

No Description Set


Returns:
bool - No Description Set


void KilledHero(handle , handle )
`````````````````

Args: Hero, Inflictor


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


void ModifyAgility(float )
`````````````````

Adds passed value to base attribute value, then calls CalculateStatBonus.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


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


void ModifyIntellect(float )
`````````````````

Adds passed value to base attribute value, then calls CalculateStatBonus.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


void ModifyStrength(float )
`````````````````

Adds passed value to base attribute value, then calls CalculateStatBonus.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


void PerformTaunt()
`````````````````

No Description Set




void RecordLastHit()
`````````````````

No Description Set




void RespawnHero(bool buyback, bool unknown1, bool unknown2)
`````````````````




+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool | buyback | No Description Set |
|  bool | unknown1 | No Description Set |
|  bool | unknown2 | No Description Set |
+-----------+--------------+--------------+


void SetAbilityPoints(int )
`````````````````

Sets the current unspent ability point's.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


void SetBaseAgility(float )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


void SetBaseIntellect(float )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


void SetBaseStrength(float )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


void SetBuybackCooldownTime(float )
`````````````````

Sets the buyback cooldown time.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


void SetBuyBackDisabledByReapersScythe(bool )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


void SetBuybackGoldLimitTime(float )
`````````````````

Set the amount of time gold gain is limited after buying back.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


void SetCustomDeathXP(int )
`````````````````

Sets a custom experience value for this hero. {{tip|GameRules boolean must be set for this to work!}}


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


void SetGold(int , bool )
`````````````````

Sets the gold amount for the player owning this hero


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
|  bool |  | No Description Set |
+-----------+--------------+--------------+


void SetPlayerID(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


void SetRespawnPosition(Vector )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector |  | No Description Set |
+-----------+--------------+--------------+


void SetTimeUntilRespawn(float )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


bool ShouldDoFlyHeightVisual()
`````````````````

No Description Set


Returns:
bool - No Description Set


void SpendGold(int , int )
`````````````````

Args: ''int'' nGold, ''int'' nReason


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+


bool UnitCanRespawn()
`````````````````

No Description Set


Returns:
bool - No Description Set


void UpgradeAbility(handle )
`````````````````

This upgrades the passed ability if it exists and the hero has enough ability point's.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


bool WillReincarnate()
`````````````````

No Description Set


Returns:
bool - No Description Set


void AddItemDrop(handle )
`````````````````

Add the specified item drop to this creature


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


void CreatureLevelUp(int )
`````````````````

Level the creature up by the specified number of levels


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


bool IsChampion()
`````````````````

Is this unit a champion?


Returns:
bool - No Description Set


void SetArmorGain(float )
`````````````````

Set the armor gained per level on this creature.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


void SetAttackTimeGain(float )
`````````````````

Set the attack time gained per level on this creature.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


void SetBountyGain(int )
`````````````````

Set the bounty gold gained per level on this creature.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


void SetChampion(bool )
`````````````````

Flag this unit as a champion creature.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


void SetDamageGain(int )
`````````````````

Set the damage gained per level on this creature.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


void SetDisableResistanceGain(float )
`````````````````

Set the disable resistance gained per level on this creature.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


void SetHPGain(int )
`````````````````

Set the hit point's gained per level on this creature.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


void SetHPRegenGain(float )
`````````````````

Set the hit point's regen gained per level on this creature.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


void SetMagicResistanceGain(float )
`````````````````

Set the magic resistance gained per level on this creature.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


void SetManaGain(int )
`````````````````

Set the mana point's gained per level on this creature.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


void SetManaRegenGain(float )
`````````````````

Set the mana point's regen gained per level on this creature.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


void SetMoveSpeedGain(int )
`````````````````

Set the move speed gained per level on this creature.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


void SetXPGain(int )
`````````````````

Set the xp reward gained per level on this creature.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


int GetInvulnCount()
`````````````````

Get the invulnerability count for a building.


Returns:
int - No Description Set


void SetInvulnCount(int )
`````````````````

Set the invulnerability counter of this building.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


handle ActionState()
`````````````````

return the ActionState object for this unit.


Returns:
handle - No Description Set


void ClearMovementTarget()
`````````````````

Clear any movement target entity/position.




table FindSensedEnemies()
`````````````````

returns list of all enemy units within this unit's sight cone or sensing sphere


Returns:
table - No Description Set


float GetMaxSpeed()
`````````````````

returns unit's max speed


Returns:
float - No Description Set


float GetMaxStamina()
`````````````````

returns maximum stamina amount.


Returns:
float - No Description Set


handle GetMovementTargetEntity()
`````````````````

Returs the movement target entity, if set.


Returns:
handle - No Description Set


float GetSensingSphereRange()
`````````````````

returns range of unit's 360 degree sensing sphere


Returns:
float - No Description Set


float GetSightConeAngle()
`````````````````

returns angle in which the unit can see things up to sight range


Returns:
float - No Description Set


float GetSightConeRange()
`````````````````

returns range of unit's sight cone


Returns:
float - No Description Set


float GetStamina()
`````````````````

returns current stamina amount.


Returns:
float - No Description Set


float GetTurnRate()
`````````````````

returns unit's turn rate in degrees per second


Returns:
float - No Description Set


string GetUnitName()
`````````````````

get the unit name for this unit.


Returns:
string - No Description Set


void GrantItem(string , bool )
`````````````````

( sItemName ) - grant an item to the unit by name.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  bool |  | No Description Set |
+-----------+--------------+--------------+


bool IsBlocking()
`````````````````

is this unit blocking?


Returns:
bool - No Description Set


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


void SetBlocking(bool )
`````````````````

( bShouldBlock ) - Set the blocking state of this unit.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


void SetMaxSpeed(float )
`````````````````

( flMaxSpeed ) - sets unit's max speed


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


void SetMovementTargetEntity(handle , float )
`````````````````

( hTargetEntity, flTargetRange ) - Try to move this unit to the given range from the target entity.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


void SetMovementTargetPosition(Vector , float )
`````````````````

( vecTargetPosition, flTargetRange ) - Try to move this unit to the given range from the target point.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


void SetSensingSphereRange(float )
`````````````````

( flSightRange ) - set range of unit's 360 degree sensing sphere


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


void SetSightConeAngle(float )
`````````````````

( flAngleDegrees ) - sets angle in which the unit can see things up to sight range


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


void SetSightConeRange(float )
`````````````````

( fRange ) - set range of unit's sight cone


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


void SetTurnRate(float )
`````````````````

( flTurnRate ) - sets unit's turn rate in degrees per second


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


void ClientLoadGridNav()
`````````````````

Tell clients that they need to load gridnav information. Used for things like allowing clients to identify valid locations to place buildings.




void SetAlwaysShowPlayerInventory(bool )
`````````````````

Show the player hero's inventory in the HUD, regardless of what unit is selected.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


void SetBotThinkingEnabled(bool )
`````````````````

Enables/Disables bot thinking. Requires a very Dota PvP-like map with 3 lanes, a shop, etc.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


void SetBuybackEnabled(bool )
`````````````````

Enables or disables buyback completely


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


void SetCameraDistanceOverride(float )
`````````````````

Set a different camera distance; dota default is 1134.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


void SetCustomBuybackCooldownEnabled(bool )
`````````````````

Turns on capability to define custom buyback cooldowns.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


void SetCustomBuybackCostEnabled(bool )
`````````````````

Turns on capability to define custom buyback costs.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


void SetCustomHeroMaxLevel(int maxLevel)
`````````````````

Allows definition of the max level heroes can achieve (default is 25).


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int | maxLevel | No Description Set |
+-----------+--------------+--------------+


void SetCustomXPRequiredToReachNextLevel(handle )
`````````````````

Allows definition of a ''table'' of hero XP values.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


void SetFogOfWarDisabled(bool )
`````````````````

Turn the fog of war on or off.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


void SetGoldSoundDisabled(bool )
`````````````````

Turn the sound when gold is acquired off/on. Takes a ''bool''.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


void SetOverrideSelectionEntity(handle unit)
`````````````````

Set an override for the default selection entity, instead of each player's hero.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle | unit | No Description Set |
+-----------+--------------+--------------+


void SetRecommendedItemsDisabled(bool )
`````````````````

Turn the panel for showing recommended items at the shop off/on. Takes a ''bool''.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


void SetRemoveIllusionsOnDeath(bool )
`````````````````

Make it so illusions are immediately removed upon death, rather than sticking around for a few seconds.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


void SetTopBarTeamValue(int , int )
`````````````````

Set the team values on the top game bar.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+


void SetTopBarTeamValuesOverride(bool )
`````````````````

Override the values of the team values on the top game bar.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


void SetTopBarTeamValuesVisible(bool )
`````````````````

Turning on/off the team values on the top game bar.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


void SetTowerBackdoorProtectionEnabled(bool )
`````````````````

Enables/Disables tower backdoor protection


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


void SetUseCustomHeroLevels(bool )
`````````````````

Turn on custom-defined XP values for hero level ups. The ''table'' should be defined before switching this on.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


void AddSubquest(handle )
`````````````````

Add a subquest to this quest


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


void CompleteQuest()
`````````````````

Mark this quest complete




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


void RemoveSubquest(handle )
`````````````````

Remove a subquest from this quest


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


void SetTextReplaceString(string )
`````````````````

Set the text replace ''string'' for this quest


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+


void SetTextReplaceValue(int , int )
`````````````````

Set a quest value


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+


void CompleteSubquest()
`````````````````

Mark this subquest complete




void SetTextReplaceString(string )
`````````````````

Set the text replace ''string'' for this subquest


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+


void SetTextReplaceValue(int , int )
`````````````````

Set a subquest value


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+


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


void DeleteCreatedSpawnGroups()
`````````````````

DeleteCreatedSpawnGroups() : Deletes any spawn groups that this point_template has spawned. Note: The point_template will not be deleted by this.




void ForceSpawn()
`````````````````

ForceSpawn() : Spawns all of the entities the point_template is pointing at.




handle GetSpawnedEntities()
`````````````````

GetSpawnedEntities() : Get the list of the most recent spawned entities


Returns:
handle - No Description Set


void SetSpawnCallback(handle , handle )
`````````````````

SetSpawnCallback( hCallbackFunc, hCallbackScope, hCallbackData ) : Set a callback for when the template spawns entities. The spawned entities will be passed in as an array.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
|  handle |  | No Description Set |
+-----------+--------------+--------------+


void AddImpulseAtPosition(Vector , Vector )
`````````````````

Apply an impulse at a worldspace position to the physics


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector |  | No Description Set |
|  Vector |  | No Description Set |
+-----------+--------------+--------------+


void AddVelocity(Vector , Vector )
`````````````````

Add linear and angular velocity to the physics object


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector |  | No Description Set |
|  Vector |  | No Description Set |
+-----------+--------------+--------------+


void DetachFromParent()
`````````````````

Detach from its parent




<> GetSequence()
`````````````````

Returns the active sequence


Returns:
<> - No Description Set


bool IsAttachedToParent()
`````````````````

Is attached to parent


Returns:
bool - No Description Set


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


void SetAngularVelocity(Vector )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector |  | No Description Set |
+-----------+--------------+--------------+


void SetAnimation(string )
`````````````````

Pass ''string'' for the animation to play on this model


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+


void SetBodyGroup(string )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+


void SetMaterialGroup(utlstringtoken )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  utlstringtoken |  | No Description Set |
+-----------+--------------+--------------+


void SetVelocity(Vector velocity)
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector | velocity | No Description Set |
+-----------+--------------+--------------+


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


bool IsSequenceFinished()
`````````````````

Ask whether the main sequence is done playing


Returns:
bool - No Description Set


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


void SetBodygroup(int , int )
`````````````````

Sets a bodygroup


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+


void SetModelScale(float scale)
`````````````````

Sets the model's scale to <i>scale</i>, <br/>so if a unit had its model scale at 1, and you use <i>SetModelScale(<b>10.0</b>)</i>, it would set the scale to <b>10.0</b>.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float | scale | No Description Set |
+-----------+--------------+--------------+


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


table GetEquippedWeapons()
`````````````````

GetEquippedWeapons() : Returns an array of all the equipped weapons


Returns:
table - No Description Set


int GetWeaponCount()
`````````````````

GetWeaponCount() : Gets the number of weapons currently equipped


Returns:
int - No Description Set


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


void CreateTrackingProjectile(handle )
`````````````````

Creates a tracking projectile


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


void DestroyLinearProjectile(int )
`````````````````

Destroys the linear projectile matching the argument ID


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


void ProjectileDodge(handle )
`````````````````

Makes the specified unit dodge projectiles


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


void Disable()
`````````````````

Disable the trigger




void Enable()
`````````````````

Enable the trigger




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


void SpawnEntity()
`````````````````

Create an entity at the location of the maker




void SpawnEntityAtEntityOrigin(handle )
`````````````````

Create an entity at the location of a specified entity instance


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


void SpawnEntityAtLocation(Vector , Vector )
`````````````````

Create an entity at a specified location and orientaton, orientation is Euler angle in degrees (pitch, yaw, roll)


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  Vector |  | No Description Set |
|  Vector |  | No Description Set |
+-----------+--------------+--------------+


void SpawnEntityAtNamedEntityOrigin(string )
`````````````````

Create an entity at the location of a named entity


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+


void StartVote(handle )
`````````````````

Starts a vote, based upon a ''table'' of parameters


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


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


void AddResource(string )
`````````````````

Precaches a specific resource


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
+-----------+--------------+--------------+


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


void ReleaseParticleIndex(int particleId)
`````````````````

Frees the specified particle index


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int | particleId | No Description Set |
+-----------+--------------+--------------+


void SetParticleAlwaysSimulate(int )
`````````````````

No Description Set


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


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


table GetAllHeroes()
`````````````````

Returns all the heroes in the world


Returns:
table - No Description Set


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


int GetHeroCount()
`````````````````

Returns the number of heroes in the world


Returns:
int - No Description Set


void AddOutput(string , string )
`````````````````

Add an output


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  string |  | No Description Set |
+-----------+--------------+--------------+


void Init(int )
`````````````````

Initialize with number of outputs


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


void SetFarRange(float )
`````````````````

Set light maximum range


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


void SetLinearAttenuation(float )
`````````````````

Set light linear attenuation value


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


void SetNearRange(float )
`````````````````

Set light minimum range


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


void SetQuadraticAttenuation(float )
`````````````````

Set light quadratic attenuation value


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


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


void DisableMotion()
`````````````````

Enable motion for the prop




void EnableMotion()
`````````````````

Enable motion for the prop




void Defeated()
`````````````````

Kills the ancient, etc.




bool DidMatchSignoutTimeOut()
`````````````````

true when we have waited some time after end of the game and not received signout


Returns:
bool - No Description Set


int GetCustomGameDifficulty()
`````````````````

Returns the difficulty level of the custom game mode


Returns:
int - No Description Set


int GetDifficulty()
`````````````````

Returns difficulty level of the custom game mode


Returns:
int - No Description Set


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


handle GetGameModeEntity()
`````````````````

Get the game mode entity


Returns:
handle - No Description Set


float GetGameTime()
`````````````````

Returns the number of seconds elapsed since map start. This time doesn't count up when the game is paused


Returns:
float - No Description Set


bool GetMatchSignoutComplete()
`````````````````

Have we received the post match signout message that includes reward information


Returns:
bool - No Description Set


float GetNianFightStartTime()
`````````````````

Gets the start time for the Nian fight


Returns:
float - No Description Set


int GetNianTotalDamageTaken()
`````````````````

For New Bloom, get total damage taken by the Nian / Year Beast


Returns:
int - No Description Set


float GetTimeOfDay()
`````````````````

Get the time of day


Returns:
float - No Description Set


bool IsDaytime()
`````````````````

Is it day time.


Returns:
bool - No Description Set


void MakeTeamLose(int team)
`````````````````

Makes ths specified team lose


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int | team | No Description Set |
+-----------+--------------+--------------+


int NumDroppedItems()
`````````````````

Returns the number of items currently dropped on the ground


Returns:
int - No Description Set


void Playtesting_UpdateAddOnKeyValues()
`````````````````

Updates custom hero, unit and ability KeyValues in memory with the latest values from disk




void ResetDefeated()
`````````````````

Restart after killing the ancient, etc.




void ResetToHeroSelection()
`````````````````

Restart the game at hero selection




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


void SetCreepMinimapIconScale(float scale)
`````````````````

Scale the creep icons on the minimap.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float | scale | No Description Set |
+-----------+--------------+--------------+


void SetCustomGameDifficulty(int )
`````````````````

Set the difficulty level of the custom game mode


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


void SetFirstBloodActive(bool )
`````````````````

Sets whether First Blood has been triggered.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


void SetGameWinner(int team)
`````````````````

Makes ths specified team win


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int | team | No Description Set |
+-----------+--------------+--------------+


void SetGoldPerTick(int )
`````````````````

Set the auto gold increase per timed interval.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


void SetGoldTickTime(float )
`````````````````

Set the time ''int''erval between auto gold increases.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


void SetHeroMinimapIconSize(int iconSize)
`````````````````

(nMinimapHeroIconSize) - Set the hero minimap icon size.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int | iconSize | No Description Set |
+-----------+--------------+--------------+


void SetHeroRespawnEnabled(bool canRespawn)
`````````````````

Control if the normal DOTA hero respawn rules apply.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool | canRespawn | No Description Set |
+-----------+--------------+--------------+


void SetHeroSelectionTime(float time)
`````````````````

Sets the amount of time players have to pick their hero.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float | time | Time In Seconds |
+-----------+--------------+--------------+


void SetNianFightStartTime(float )
`````````````````

Sets the start time for the Nian fight


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


void SetOverlayHealthBarUnit(handle unit, int style)
`````````````````

Show this unit's health on the overlay health bar


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle | unit | No Description Set |
|  int | style | No Description Set |
+-----------+--------------+--------------+


void SetPostGameTime(float time)
`````````````````

Sets the amount of time players have between the game ending and the server disconnecting them.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float | time | Time in Seconds |
+-----------+--------------+--------------+


void SetPreGameTime(float time)
`````````````````

Sets the amount of time players have between picking their hero and game start.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float | time | Time In Seconds |
+-----------+--------------+--------------+


void SetRuneMinimapIconScale(float scale)
`````````````````

Scale the rune icons on the minimap.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float | scale | No Description Set |
+-----------+--------------+--------------+


void SetRuneSpawnTime(float time)
`````````````````

Sets the amount of time between rune spawns.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float | time | Time in seconds |
+-----------+--------------+--------------+


void SetSafeToLeave(bool safeToLeave)
`````````````````

Mark this game as safe to leave.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool | safeToLeave | No Description Set |
+-----------+--------------+--------------+


void SetSameHeroSelectionEnabled(bool enabled)
`````````````````

When true, players can repeatedly pick the same hero.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool | enabled | No Description Set |
+-----------+--------------+--------------+


void SetTimeOfDay(float time)
`````````````````

Set the time of day.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float | time | No Description Set |
+-----------+--------------+--------------+


void SetTreeRegrowTime(float time)
`````````````````

Sets the tree regrow time in seconds.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float | time | Time in Seconds |
+-----------+--------------+--------------+


void SetUseBaseGoldBountyOnHeroes(bool )
`````````````````

Heroes will use the basic NPC functionality for determining their bounty, rather than DOTA specific formulas.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


void SetUseCustomHeroXPValues(bool )
`````````````````

Allows heroes in the map to give a specific amount of XP (this value must be set).


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool |  | No Description Set |
+-----------+--------------+--------------+


void SetUseUniversalShopMode(bool enabled)
`````````````````

When true, all items are available at as long as any shop is in range, including Secret Shop items


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  bool | enabled | No Description Set |
+-----------+--------------+--------------+


<> State_Get()
`````````````````

Get the current Gamerules state


Returns:
<> - No Description Set


float GetBloomScale()
`````````````````

Gets bloomscale for this tonemap controller


Returns:
float - No Description Set


float GetMaxExposure()
`````````````````

Gets max exposure for this tonemap controller


Returns:
float - No Description Set


float GetMinExposure()
`````````````````

Gets min exposure for this tonemap controller


Returns:
float - No Description Set


void SetBloomScale(float )
`````````````````

Sets bloom scale for this tonemap controller


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


void SetMaxExposure(float )
`````````````````

Sets max exposure for this tonemap controller


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


void SetMinExposure(float )
`````````````````

Sets min exposure for this tonemap controller


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  float |  | No Description Set |
+-----------+--------------+--------------+


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


void EntityAttachments(ehandle , float )
`````````````````

Draws the attachments of the entity


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  ehandle |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


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


void EntitySkeleton(ehandle , float )
`````````````````

Draws the skeleton of the entity


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  ehandle |  | No Description Set |
|  float |  | No Description Set |
+-----------+--------------+--------------+


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


void PopDebugOverlayScope()
`````````````````

Pops the identifier used to group overlays. Overlays marked with this identifier can be deleted in a big batch.




void PushAndClearDebugOverlayScope(utlstringtoken )
`````````````````

Pushes an identifier used to group overlays. Deletes all existing overlays using this overlay id.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  utlstringtoken |  | No Description Set |
+-----------+--------------+--------------+


void PushDebugOverlayScope(utlstringtoken )
`````````````````

Pushes an identifier used to group overlays. Overlays marked with this identifier can be deleted in a big batch.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  utlstringtoken |  | No Description Set |
+-----------+--------------+--------------+


void RemoveAllInScope(utlstringtoken )
`````````````````

Removes all overlays marked with a specific identifier, regardless of their lifetime.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  utlstringtoken |  | No Description Set |
+-----------+--------------+--------------+


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


void UnitTestCycleOverlayRenderType()
`````````````````

Toggles the overlay render type, for unit tests




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


handle GetCurrentScene()
`````````````````

Returns the instance of the oldest active scene entity '''(if any).


Returns:
handle - No Description Set


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


void AddBroadcastTeamTarget(int )
`````````````````

Adds a team (by index) to the broadcast list


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


void Cancel()
`````````````````

Cancel scene playback




float EstimateLength()
`````````````````

Returns length of this scene in seconds.


Returns:
float - No Description Set


handle FindCamera()
`````````````````

Get the camera


Returns:
handle - No Description Set


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


bool IsPaused()
`````````````````

If this scene is currently paused.


Returns:
bool - No Description Set


bool IsPlayingBack()
`````````````````

If this scene is currently playing.


Returns:
bool - No Description Set


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


void RemoveBroadcastTeamTarget(int )
`````````````````

Removes a team (by index) from the broadcast list


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  int |  | No Description Set |
+-----------+--------------+--------------+


void Start(handle )
`````````````````

Start scene playback, takes activatorEntity as param


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  handle |  | No Description Set |
+-----------+--------------+--------------+


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


void RegrowAllTrees()
`````````````````

 




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


handle GetCommandClient()
`````````````````

GetCommandClient() : returns the player who issued this console command.


Returns:
handle - No Description Set


handle GetDOTACommandClient()
`````````````````

GetDOTACommandClient() : returns the DOTA player who issued this console command.


Returns:
handle - No Description Set


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


void SetBool(string variableName, bool value)
`````````````````

SetBool(name, val) : sets the value of the convar to the ''bool''.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string | variableName | No Description Set |
|  bool | value | No Description Set |
+-----------+--------------+--------------+


void SetFloat(string variableName, float value)
`````````````````

SetFloat(name, val) : sets the value of the convar to the ''float''.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string | variableName | No Description Set |
|  float | value | No Description Set |
+-----------+--------------+--------------+


void SetInt(string , int )
`````````````````

SetInt(name, val) : sets the value of the convar to the ''int''.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  int |  | No Description Set |
+-----------+--------------+--------------+


void SetStr(string , string )
`````````````````

SetStr(name, val) : sets the value of the convar to the ''string''.


+-----------+--------------+--------------+
|Type       |  Name        |  Description |
+-----------+--------------+--------------+
|  string |  | No Description Set |
|  string |  | No Description Set |
+-----------+--------------+--------------+


