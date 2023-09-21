<script lang="ts">
  import Margin from "../../../components/atoms/Margin.svelte";
  import NewUserForm from "../../../components/organisms/Forms/NewUserForm.svelte";
  import Text from "../../../components/atoms/Text.svelte";
  import Link from "../../../components/atoms/Link.svelte";

  import { user } from '../../../store';

  export let data;
</script>

{#if $user.role == 'superadmin'}
  <div class='card card--wide block-center'>
    <NewUserForm data={data} />
  </div>
{:else}
  <div class='card block-center'>
    <Text
      textTag='p'
      class='text-preset-4 text-center'
    >
      Vous n'avez pas accès à cette page.
    </Text>

    <Margin marginTop='var(--spacing-3)'>
      {#if $user.role == 'lead'}
        <Link linkUrl='/projects/admin-dashboard' linkColor='white' class='link--button link-center'> Retour </Link>
      {:else}
        <Link linkUrl='/projects/dahboard' linkColor='white' class='link--button link-center'> Retour </Link>
      {/if}
    </Margin>
  </div>
{/if}