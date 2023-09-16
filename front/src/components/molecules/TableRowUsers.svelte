<script lang='ts'>
  import Icon from '../atoms/Icon.svelte';
  import ArrowBackgroundIcon from '../../assets/icons/ArrowBackgroundIcon.svelte';

  export let selectedRowElements: any;

</script>

{#each selectedRowElements as selectedRowElement}
	<tr>
    {#if selectedRowElement.profile_pic}
      <td>
        <img
        class="profile_pic"
        src={selectedRowElement.profile_pic}
        alt="The profile picture of {selectedRowElement.fullname}"
        />
      </td>
		{/if}
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
      <a href="">
        <Icon title="arrow" color="transparent">
          <ArrowBackgroundIcon />
        </Icon> 
      </a> 
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
  .profile_pic {
    width: 40px;
    border-radius: 10px;
  }
</style>