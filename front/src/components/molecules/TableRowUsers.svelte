<script lang='ts'>
  import Icon from '../atoms/Icon.svelte';
  import Image from '../atoms/Image.svelte';
  import Link from '../atoms/Link.svelte';

  import ArrowBackgroundIcon from '../../assets/icons/ArrowBackgroundIcon.svelte';
  import UserIcon from '../../assets/icons/UserIcon.svelte';

  export let selectedRowElements: any;

</script>

{#each selectedRowElements as selectedRowElement}
	<tr>
    <td>
      {#if selectedRowElement.profile_pic != null }
        <Image
          imageSrc={selectedRowElement.profile_pic}
          imageAlt="The profile picture of {selectedRowElement.fullname}"
          imageWidth=50
        />
      {:else}
        <Icon name="user" width="50" height="50"> <UserIcon /> </Icon>
      {/if}
    </td>
		{#if selectedRowElement.fullname}
			<td>{selectedRowElement.fullname}</td>
		{/if}
    {#if selectedRowElement.email}
			<td>{selectedRowElement.email}</td>
		{/if}
    {#if selectedRowElement.domain}
			<td>{selectedRowElement.domain}</td>
		{/if}
    {#if selectedRowElement.role}
			<td>{selectedRowElement.role}</td>
		{/if}
    <td> 
      <Link
        linkUrl='{selectedRowElement.id}'> 
        <Icon name="details" width="20" height="20"> <ArrowBackgroundIcon /> </Icon>
      </Link>
    </td>
	</tr>
{/each}

<style>
  tr {
    white-space: nowrap;
    text-transform: capitalize;
  }
  
  td {
    border-top: 1px solid var(--grey);
    padding-bottom: var(--spacing-3);
    padding-top: var(--spacing-3);
    padding-left: var(--spacing-4);
    padding-right: var(--spacing-4);
    white-space: nowrap;
    vertical-align: middle;
  }

  td:first-child {
    padding-left: 0;
  }

  tr td:last-child {
    padding: 0;
    vertical-align: middle;
  }

</style>